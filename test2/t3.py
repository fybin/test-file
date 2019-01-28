# from test2 import test_imp



class c_test(object):
    def __init__(self):
        print('c_test is object')

    def run(self):
        print('this is c_test')


class Factory(object):
    pass


if not hasattr(Factory, "run"):
    setattr(Factory, 'll_run', c_test)


factory = Factory()
# 实例化c_test
ft = factory.ll_run()
ft.run()
# print(factory.ll_run())
# Factory.ll_run.run()