import logging

# 带参数的装饰器
# 带参数的装饰器只需要在原来那个不带参数的装饰器基础上之上在最外层套一个函数，
# 该函数中定义一个参数，然后嵌套函数中引用该参数即可实现。从下图看出，我只是把里面那个函数改了一下名字，
# 其余和原来不带参数的装饰器是一样的。
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator


# 带参数的装饰器，level='warn'就是装饰器带的参数，他是装饰器内部的参数，控制的事装饰器的业务逻辑，也算是对原有装饰器的一种封装。
@use_logging(level="warn")
def foo_warn(name='foo_warn'):
    print("i am %s" % name)


# 也可以这样写
info = use_logging('info')


@info
def foo_info(name='foo_info'):
    print('i am %s' % name)


# foo_warn()
# foo_info()


# functools.wraps

