class Dj(object):
    def __init__(self):
        print('回来继承Dj的初始化')

    def route(self):
        print('回来继承Dj的route')

class Dapa(Dj):
    def __init__(self):
        print('iam Dapa')
        super(Dapa, self).__init__()

    def route(self):
        print("iam Dapa route")
        super(Dapa, self).route()

da = Dapa()
da.route()