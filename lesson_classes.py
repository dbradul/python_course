import re
import time
import json
import yaml
import dicttoxml, xmltodict

from functools import partial
from pprint import pprint as pp

class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start) * 1000
        print(self.message.format(elapsed_time))


class Q:

    def __init__(self, *, as_string='', **params):
        self._params = params
        self._as_string = as_string

    def __or__(self, other):
        self._as_string = f'({str(self)} OR {str(other)})'
        return self #Q(as_string=f'({str(self)} OR {str(other)})')

    def __and__(self, other):
        return Q(as_string=f'({str(self)} AND {str(other)})')

    def __invert__(self):
        return Q(as_string=f'NOT {str(self)}')

    def __str__(self):
        result = ''
        if self._as_string:
            result = self._as_string
        elif self._params:
            result = [f'{k}={repr(v)}' for k, v in self._params.items()][0]
        return result


filter = (Q(first_name='J') | Q(last_name='J', telephone='+38000')) & ~Q(email='test@gmail.com')
print(filter)

filter = Q(first_name='J') | (Q(last_name='J', telephone='+38000') & ~Q(email='test@gmail.com'))
print(filter)

import logging

logger = logging.getLogger(__name__)
logger2 = logging.getLogger(__name__)
print(id(logger), id(logger2))




class Attribute:

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name, id(obj))
        return obj.__dict__[self.name]  # self.val

    def __set__(self, obj, val):
        print('Updating', self.name, id(obj))
        self.val = val
        obj.__dict__[self.name] = val

    def __delete__(self, obj):
        # print('Deleting', self.name, id(obj))
        self.val = None


class A:
    attr = Attribute(name='attr')
    # attr = 'DEMO'


a = A()
print(id(a))
a.attr = 42
print(a.attr)
# del a.attr
#
# b = A()
# print(id(b))
# b.attr = 43
# print(a.attr)
# print(b.attr)