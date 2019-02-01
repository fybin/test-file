# functools.wraps


def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)     # 输出 'with_logging'
        print(func.__doc__ )     # 输出 None
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
   """does some math"""
   return x + x * x


f(1)
print(f.__name__)
# 这是返回值，我们看到f的name成了with_logging, 这有些疑惑，我们不想被装饰了的函数换成了别的函数的名，所以使用function.wraps
# f
# does some math
# with_logging


from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
   """does some math"""
   return x + x * x


f(1)
print(f.__name__)