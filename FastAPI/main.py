from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Создаем экземпляр приложения
app = FastAPI()

# Модель данных с валидацией
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# Простой GET-эндпоинт
@app.get("/")
def read_root():
    return {"Hello": "World"}

# GET с параметром пути
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# POST-эндпоинт с телом запроса
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}

# Асинхронный эндпоинт
@app.get("/async-example/")
async def async_endpoint():
    # Асинхронные операции (запросы к БД, API и т.д.)
    return {"message": "Это асинхронный эндпоинт"}

if __name__ == "__main__":
    uvicorn.run("E/Git/Learning/FastAPI/main:app", host="0.0.0.0", port=8000, reload=True)
# def __main__():
#     app = FastAPI()
#     app.include_router(router)

# Запуск через терминал:
# PS E:\Git> cd E:/Git/Learning/FastAPI/
# PS E:\Git\Learning\FastAPI> uvicorn main:app --reload