
"""
Python装饰器（decorator）在实现的时候，
被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），
为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用.
"""


from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)
example()
