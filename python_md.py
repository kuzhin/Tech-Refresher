class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity
        self.is_moving = False

    def start(self):
        self.capacity = True

    def stop(self):
        self.stoped = True

    def info(self):
        print("The vehicle is moving on {} km/s speed".format(self.speed))

    def __enter__(self):
        pass

# Дочерний класс
class Car(Transport):
    def __init__(self, speed, capacity, brand, fuel_type):
        # Вызвали __init__ чтобы не тащить переменные из родительского
        super().__init__(speed, capacity)
        # Можем добавлять свои свойства
        self.brand = brand
        self.fuel_type = fuel_type
        self.amount = 50
        self.fuel_level = 100

    def refuel(self, amount):
        self.fuel_level = min(100, self.fuel_level + amount)
        print('Refuel a vehicle on {0} and now fuel level is {1}'.format(self.amount, self.fuel_level))


# def memoize(func):
#     cache = {}
#
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#
#     return wrapper

# @memoize
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(4))
# pass
