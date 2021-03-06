#!/usr/bin/env python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from mstat.fstat.base_stat import BaseStat
from mstat.fstat.interpolation import Interpolation

from mstat.fstat.extended_stat import ExtendedStat

class ApiServer(BaseHTTPRequestHandler):
    handlers = {
        "mean" : BaseStat.get_mean,
        "std"  : BaseStat.get_std,
        "autocorrelation" : BaseStat.get_autocorrelation,
        "mnk" : ExtendedStat.get_mnk,
        "lin_interpolation" : Interpolation.interpolate_linear,
        "spline_interpolation" : Interpolation.interpolate_spline,
        "newton_interpolation" : Interpolation.interpolate_newton
    }

    def do_POST(self):
        try:
            data_size = int(self.headers['content-length'])
            data = json.loads(self.rfile.read(data_size).decode())
            payload = [val for val in data["data"] if isinstance(val, int) or isinstance(val, float)]
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
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(resp, "utf8"))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(bytes(str(e), "utf8"))
            return
        return


def __main__():
    server_address = ('0.0.0.0', 9999)
    httpd = HTTPServer(server_address, ApiServer)
    print('running server...')
    httpd.serve_forever()
