class Tiger(object):
    def __init__(self):
        print(self.__class__)
        print('this is tiger')
    def run(self):
        pass


class TigerSun(Tiger):
    def __init__(self):
        super(TigerSun, self).__init__()

print(TigerSun)
tiger = Tiger()
tigersun = TigerSun()
print(Tiger.__class__)
print(TigerSun.__class__)
print(issubclass(TigerSun, Tiger))
