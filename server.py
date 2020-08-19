# from http.server import BaseHTTPRequestHandler, HTTPServer
# import functools
#
# path2func_map = {}
#
# class HandleRequests(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         _, path, _ = self.requestline.split(' ')
#         if path in path2func_map:
#             result = path2func_map[path]()
#             self.wfile.write(f"{result}".encode())
#
#         # if path == '/hello':
#         #     self.wfile.write(b"hello !")
#         # elif path == '/bye':
#         #     self.wfile.write(b"bye!")
#         # elif path == '/purpose':
#         #     self.wfile.write(b"42")
#         else:
#             self.wfile.write(b"Unknown request :(")
#
#
# # def route(path="/"):
# #     def internal(f):
# #         path2func_map[path] = f
# #         @functools.wraps(f)
# #         def deco(*args):
# #             result = f(*args)
# #             return result
# #         return deco
# #     return internal
# #
# #
# # @route('/hello')
# # def hello():
# #     return 'Hello!'
# #
# #
# # @route('/bye')
# # def hello():
# #     return 'Bye!'
#
#
# host = '127.0.0.1'
# port = 8001
# HTTPServer((host, port), HandleRequests).serve_forever()
#

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run('127.0.0.1', 8011)