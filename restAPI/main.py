from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import APIKeyHeader
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import secrets
from typing import Dict

# Хранилище в памяти (в реальности — заменить на БД)
# {api_key: user_id}
API_KEYS: Dict[str, str] = {}

# Для генерации уникальных user_id
user_counter = 0

# Rate limiter: лимит по API-ключу
def get_api_key_from_request(request: Request) -> str:
    key = request.headers.get("X-API-Key")
    if not key or key not in API_KEYS:
        # Возвращаем специальный ключ, чтобы slowapi не ломался
        # raise HTTPException(status_code=403, detail="Invalid or missing API key")
        return "invalid"
    return key

limiter = Limiter(key_func=get_api_key_from_request)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def validate_api_key(request: Request) -> str:
    key = request.headers.get("X-API-Key")
    if not key or key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
    return key

# Эндпоинт для генерации нового API-ключа
@app.post("/generate-key")
def generate_key():
    global user_counter
    user_counter += 1
    user_id = f"user_{user_counter}"
    new_key = secrets.token_urlsafe(32)  # 256-bit secure token
    API_KEYS[new_key] = user_id
    return {"api_key": new_key, "user_id": user_id}

# Защищённый эндпоинт с rate limiting: 50 запросов в минуту на ключ
@app.get("/predict")
@limiter.limit("50/minute")
def predict(request: Request, api_key: str = Depends(validate_api_key)):
    # Здесь может быть ваш ML-код
    return {
        "message": "Prediction successful!",
        "user_id": API_KEYS[api_key],
        "note": "This is a demo — no real ML here yet."
    }

# Эндпоинт для отладки: показывает, сколько ключей выдано
@app.get("/stats")
def stats():
    return {"total_keys_issued": len(API_KEYS)}