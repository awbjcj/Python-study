import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def decorator(*args, **kwargs):
#         start_time = time.time()
#         res = fn(*args, **kwargs)
#         print('%s executed in %s ms' % (fn.__name__, time.time() - start_time))
#         return res
#     return decorator

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


def log(*text):
    def decor(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            print('%s beigin call, log text:%s' % (func.__name__, text))
            res = func(*args, **kwargs)
            print('%s end call, log text:%s' % (func.__name__, text))
            return res
        return new_func
    return decor
    

@log()
def f1():
    print(time.time())

@log('execute')
def f2():
    print(time.time())

f1()
f2()
