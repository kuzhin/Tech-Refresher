class father:
    def __init__(self, param):
        self.a = param

class child(father):
    def __init__(self, param):
        super().__init__(param)
        self.b = param

obj = child(22)
print("%d %d" % (obj.a, obj.b))