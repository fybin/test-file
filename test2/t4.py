#  第一种
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


# 装饰器维护一个字典对象instances，缓存了所有单例类，只要单例不存在则创建，已经存在直接返回该实例对象。
@singleton
class Foo(object):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)


# 第二种，基类
# __new__是真正创建实例对象的方法，所以重写基类的__new__方法，以此来保证创建对象的时候只生成一个实例
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        # 我们将类的实例和一个类变量 _instance 关联起来
        if not hasattr(cls, '_instance'):
            # 如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)


# 第三种，元类
# 拦截类的创建
# 修改类的定义
# 返回修改后的类
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass


foo1 = MyClass()
foo2 = MyClass()

print(foo1 is foo2)

# 或
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    pass

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)