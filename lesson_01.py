import inspect
import time
#
# ##############################################################
# # Generators
# ##############################################################
# def bar():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 2
#     print('step 3')
#     yield 3
#
# def foo():
#     for i in range(10**1000):
#         yield i
#
# gen = bar()
# for x in gen:
#     print(x)
#
#
# gen = (i for i in range(10**100))
#
# def foo2():
#     for i in range(10**100):
#         yield i
#
# for i in foo2():
#     print(i)
#
#
#
# def foo():
#     for i in range(10**1000):
#         yield(i)
#
# for i in foo():
#     print(i)
#
#
# lst = []
# for i in range(100):
#     lst.append(i)
#
# lst = [i for i in range(100)]
#
#
# path_from = '/home/dbhost/Downloads/1GB.bin'
# path_to = '/home/dbhost/Downloads/dest.bin'
#
# def read_file(filepath):
#     with open(filepath, 'r+b') as f:
#         chunk_size = 4*1024
#         chunk = f.read(chunk_size)
#
#         while chunk:
#             yield chunk
#             chunk = f.read(chunk_size)
#
#
# f = open(path_to, 'w+b')
# for chunk in read_file(path_from):
#     f.write(chunk)
# f.close()
#
#
# def func(*args, **kwargs):
#     print(locals())
#
# def hand_made_gen(start, stop, cb, *cb_args, **cb_kwargs):
#     while start < stop:
#         cb(start, *cb_args, **cb_kwargs)
#         start += 1
#
# hand_made_gen(0, 10 ** 100, func)
#
#
#
# ##############################################################
# # Decorators
# ##############################################################
# def profile(f):
#     def inner(*args, **kwargs):
#         start = time.time()
#         ret = f(*args, **kwargs)
#         elapsed = time.time() - start
#         print(f'Elapsed: {elapsed}s')
#         return ret
#
#     return inner
#
#
# def cache(f):
#     def inner(*args, **kwargs):
#         key = (args, frozenset(kwargs.items()))
#         if key not in inner.cache:
#             inner.cache[key] = f(*args, **kwargs)
#         return inner.cache[key]
#     inner.cache = {}
#
#     return inner
#
# @profile
# def foo():
#
#     time.sleep(2)
#
#     return 42
#
# # foo_decorated = profile(foo)
#
# # @profile
# @cache
# def fib(n):
#     result = 1 if n <= 2 else fib(n-1) + fib(n-2)
#     return result
#
# print(fib(140))


class coloured_print():

    def __init__(self):  # , colour="31;40m"):
        self.old_print = None

    def __enter__(self):
        def my_print(*args):
            self.old_print('\x1B[31;40m', *args, '\x1B[0m')

        global print
        self.old_print = print
        print = my_print

    def __exit__(self, type, value, traceback):
        global print
        print = self.old_print


print('BEFORE')
with coloured_print() as aa:
    print('Hello')
    print('Hello')
print('AFTER')