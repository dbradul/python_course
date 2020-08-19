from http.server import BaseHTTPRequestHandler, HTTPServer

__all__ = ['route']

path2func_map = {}

class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        _, path, _ = self.requestline.split(' ')
        if path in path2func_map:
            result = path2func_map[path]()
            self.wfile.write(f"{result}".encode())
        else:
            self.wfile.write(b"Unknown request :(")


def run_server(host='127.0.0.1', port=8002):
    HTTPServer((host, port), HandleRequests).serve_forever()


def route(path="/"):
    def internal(f):
        path2func_map[path] = f
        return f
    return internal
