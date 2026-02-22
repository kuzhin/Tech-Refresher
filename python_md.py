class father:
    def __init__(self, param):
        self.a = param

class child(father):
    def __init__(self, param):
        super().__init__(param)
        self.b = param

obj = child(22)
print("%d %d" % (obj.a, obj.b))

def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

# @memoize
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(4))
# pass
