import time
import threading
import multiprocessing
import itertools
import os
import logging
import random
import string
import requests
from functools import partial
from multiprocessing import Queue
from multiprocessing.pool import ThreadPool

from PIL import Image
from io import BytesIO

from typing import List

class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        print(self.message.format(elapsed_time))
#
#
# ### THREADS
# DATA_SIZE = 1
#
# def long_running_task(n=1):
#     # print(threading.current_thread())
#     time.sleep(n)
#
# with timer('Elapsed: {}s'):
#     long_running_task()
#     long_running_task()
#
# with timer('Elapsed: {}s'):
#     t1 = threading.Thread(target=countdown, args=(DATA_SIZE // 2,))
#     t2 = threading.Thread(target=countdown, args=(DATA_SIZE // 2,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
#
# def run_threads(data, workers):
#     threads = [
#         threading.Thread(target=countdown, args=(data // workers, ))
#         for _ in range(workers)
#     ]
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#
# workers = 20
# with timer('Elapsed: {}s'):
#     run_threads(DATA_SIZE, workers)
#
# with timer('Elapsed: {}s'):
#     with ThreadPool(workers) as pool:
#         input_data = [DATA_SIZE // workers for _ in range(workers)]
#         pool.map(long_running_task, input_data)
#
#
# ### IO-BOUND
#
# def fetch_pic(num_pic):
# # def fetch_pic(num_pic, path):
#     url = 'https://picsum.photos/400/600'
#     path = './pics'
#     for _ in range(num_pic):
#         random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
#         response = requests.get(url)
#         if response.status_code == 200:
#             with open(f'{path}/{random_name}.jpg', 'wb') as f:
#                 f.write(response.content)
#                 print(f"Fetched pic [{os.getpid()}]: {f.name}")
#         else:
#             print(f"Error {response.status_code}")
#
# with timer('Elapsed: {}s'):
#     fetch_pic(100)
#
#
# DATA_SIZE = 100
# workers = 10
#
# with timer('Elapsed: {}s'):
#     with ThreadPool(workers) as pool:
#         input_data = [DATA_SIZE // workers for _ in range(workers)]
#         pool.map(fetch_pic, input_data)
#
#
# ### CPU-BOUND
#
#
# DATA_SIZE = 10000000
#
# def fill_data(n, lst):
#     # print(threading.current_thread())
#     while n > 0:
#         n -= 1
#         lst.append(random.randint(1, 100))
#
#
# lst = []
# with timer('Elapsed: {}s'):
#     # fill_data(DATA_SIZE, lst)
#     fill_data(DATA_SIZE, lst)
#
#
# with timer('Elapsed: {}s'):
#     t1 = threading.Thread(target=fill_data, args=(DATA_SIZE // 2, lst))
#     t2 = threading.Thread(target=fill_data, args=(DATA_SIZE // 2, lst))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
# print(os.cpu_count())
#
# workers = 4
# with timer('Elapsed: {}s'):
#     with ThreadPool(workers) as pool:
#         input_data = [DATA_SIZE // workers for _ in range(workers)]
#         pool.map(partial(fill_data, lst=lst), input_data)
#
# workers = 8
# with timer('Elapsed: {}s'):
#     with multiprocessing.Pool(workers) as pool:
#         input_data = [DATA_SIZE // workers for _ in range(workers)]
#         pool.map(partial(fill_data, lst=lst), input_data)


image = Image.open('pics/0Ay6r.jpg').convert('L')
image.save('pics/0Ay6r_greyscale.jpg')


def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"

# single-threaded version
result = {}
data = [n for n in range(1000000)]

with timer('Elapsed: {}s'):
    for n in data:
        result[n] = factorize_naive(n)

# def factorize_numbers(lst):
#     for n in lst:
#         result[n] = factorize_naive(n)

def factorize_number(n):
    result[n] = factorize_naive(n)

workers = 8
with timer('Elapsed: {}s'):
    # with multiprocessing.Pool(workers) as pool:
    with ThreadPool(workers) as pool:
        input_data = [n for n in range(1000000)] #[DATA_SIZE // workers for _ in range(workers)]
        pool.map(factorize_number, input_data)