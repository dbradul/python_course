# from flusk import app
#
#
# @app.route('/hello')
# def hello():
#     return 'Hello!!!!!!!!!!!'
#
# app.run_server('127.0.0.1', 8008)



# import datetime
# import random
#
# from flask import Flask, request, Response
#
# from utils import parse_length
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# @app.route('/now')
# def get_now():
#     result = str(datetime.datetime.now())
#     return result
#
#
# # def parse_length(request, default=10):
# #     value = request.args.get('length', str(default))
# #
# #     if not value.isnumeric():
# #         raise ValueError('Not a number')
# #
# #     value = int(value)
# #     if not 3 < value < 100:
# #         raise ValueError('Out of range')
# #
# #     return value
#
#
# @app.route('/random')
# def get_random():
#     try:
#         length = parse_length(request, 10)
#     except Exception as ex:
#         return Response(ex, status=400)
#
#     try:
#         result = ''.join([
#             str(random.randint(0, 9))
#             for _ in range(length)
#         ])
#     except Exception as ex:
#         return Response(ex, status=500)
#
#     return result
#
#
# app.run('127.0.0.1', 8009, debug=True)