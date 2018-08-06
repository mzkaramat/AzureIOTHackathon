# Copyright 2018 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import sys
import json
import traceback

from tornado import ioloop
from tornado.options import define, options, parse_command_line
import tornado.httpserver
import tornado.web
import tornado.escape
import pandas as pd
from numpy import nan
from numpy import ma
from scoring_h2oai_experiment_dovudusu import Scorer

scoring_module_hash = 'h2oai_experiment_dovudusu'

def _convert(a):
    return a.item() if isinstance(a, np.generic) else a

class HTTPHandler(object):
    def __init__(self):
        self.scorer = Scorer()

    def get_hash(self):
        return scoring_module_hash

    def score(self, row, output_margin=False, pred_contribs=False):
        return self.scorer.score([row['L3_S30_D3521'] if row['L3_S30_D3521'] != None else nan ,], output_margin, pred_contribs)

    def score_batch(self, rows, output_margin=False, pred_contribs=False):
        columns = [
            pd.Series([r['L3_S30_D3521'] if r['L3_S30_D3521'] != None else nan for r in rows], name='L3_S30_D3521', dtype='float64'),
        ]
        pr = self.scorer.score_batch(pd.concat(columns, axis=1), output_margin, pred_contribs).values
        return pr.tolist()

    def get_target_labels(self):
        return self.scorer.get_target_labels()

    def get_transformed_column_names(self):
        return self.scorer.get_transformed_column_names()

    def get_column_names(self):
        return self.scorer.get_column_names()

def json_rpc_success(id, result):
    return dict(jsonrpc='2.0', id=id, result=result)


def json_rpc_error(id, code, message):
    return dict(jsonrpc='2.0', id=id, error=dict(code=code, message=message))


def handle_json_rpc_request(api_methods, scoring_handler, request):
    if 'id' not in request:
        return json_rpc_error(0, 1, "Bad request: want 'id' in RPC request.")

    request_id = request['id']

    if 'method' not in request:
        return json_rpc_error(request_id, 1, "Bad request: want 'method' in RPC request.")

    method = request['method']

    if not isinstance(method, str):
        return json_rpc_error(request_id, 1, "Bad request: want string 'method', got {}".format(type(method)))

    if method not in api_methods:
        return json_rpc_error(request_id, 1, "Method not found: {}".format(method))

    if 'params' not in request:
        return json_rpc_error(request_id, 1, "Bad request: want 'params' in RPC request.")

    params = request['params']

    if not isinstance(params, dict):
        return json_rpc_error(request_id, 1, "Bad request: want 'params' by-name, got {}".format(type(params)))

    func = getattr(scoring_handler, method)

    try:
        return json_rpc_success(request_id, func(**params))
    except:
        return json_rpc_error(request_id, 1, traceback.format_exc())


class JSONRPCHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def post(self, *args, **kwargs):
        if not self.request.body:
            self.set_status(400)  # Bad request
            return

        scoring_handler = self.application.scoring_handler
        api_methods = self.application.api_methods

        req = json.loads(tornado.escape.to_basestring(self.request.body))

        res = handle_json_rpc_request(api_methods, scoring_handler, req)

        self.write(json.dumps(res, allow_nan=False))


class Server(tornado.web.Application):
    def __init__(self, scoring_handler):
        self.scoring_handler = scoring_handler
        self.api_methods = set(dir(scoring_handler))
        handlers = [
            (r'/rpc', JSONRPCHandler),
        ]
        super(Server, self).__init__(handlers)


def start_http_server(port):
    scoring_handler = HTTPHandler()
    http_server = tornado.httpserver.HTTPServer(Server(scoring_handler))

    print('HTTP scoring service listening on port {}...'.format(port))
    http_server.listen(port)
    ioloop.IOLoop.instance().start()

define('port', default=9090, help='Port to run scoring server on.', type=int)

def main():
    parse_command_line()
    start_http_server(options.port)

if __name__ == "__main__":
    main()

