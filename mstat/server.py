#!/usr/bin/env python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from mstat.fstat.base_stat import BaseStat


class ApiServer(BaseHTTPRequestHandler):
    handlers = {
        "mean" : BaseStat.get_mean,
        "std"  : BaseStat.get_std
    }

    def do_POST(self):
        try:
            data_size = int(self.headers['content-length'])
            data = json.loads(self.rfile.read(data_size).decode())
            payload = data["data"]
            methods = data["methods"]
            resp = {}
            for method in methods:
                if method in self.handlers:
                    resp[method] = self.handlers[method](payload, **methods[method])
                else:
                    resp[method] = None
            resp = json.dumps(resp)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(resp, "utf8"))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(str(e), "utf8"))
            return
        return


def __main__():
    server_address = ('0.0.0.0', 9999)
    httpd = HTTPServer(server_address, ApiServer)
    print('running server...')
    httpd.serve_forever()
