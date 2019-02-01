# 类装饰器


# 类装饰器要继承__call__,方法当使用 @ 形式将装饰器附加到函数上时，就会调用此方法
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


# 使用类装饰器的好处是可以用到类的灵活度大、高内聚、封装性等优点，把装饰器当成一个对象来生成，被装饰得函数被单程__init__(arg),
# 参数传入装饰器类里，处理加工要在__call__内部。
@Foo
def bar():
    print('bar')


bar()
