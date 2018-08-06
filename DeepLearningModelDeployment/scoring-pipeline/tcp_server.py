# Copyright 2018 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import sys

sys.path.append('gen-py')

from h2oai_scoring import ScoringService
from h2oai_scoring.ttypes import Row
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from tornado.options import define, options, parse_command_line
import pandas as pd
from numpy import nan
from numpy import ma
from scoring_h2oai_experiment_dovudusu import Scorer

scoring_module_hash = 'h2oai_experiment_dovudusu'

def _convert(a):
    return a.item() if isinstance(a, np.generic) else a


class TCPHandler(object):
    def __init__(self):
        self.scorer = Scorer()

    def get_hash(self):
        return scoring_module_hash

    def score(self, row, output_margin=False, pred_contribs=False):
        return self.scorer.score([
            row.l3S30D3521 if hasattr(row, 'l3S30D3521') else nan,  # L3_S30_D3521
        ], output_margin, pred_contribs)

    def score_batch(self, rows, output_margin=False, pred_contribs=False):
        columns = [
            pd.Series(ma.masked_invalid([r.l3S30D3521 if hasattr(r, 'l3S30D3521') else nan for r in rows]), name='L3_S30_D3521', dtype='float64'),
        ]
        pr = self.scorer.score_batch(pd.concat(columns, axis=1), output_margin, pred_contribs).values
        return pr.tolist()

    def get_target_labels(self):
        return self.scorer.get_target_labels()

    def get_transformed_column_names(self):
        return self.scorer.get_transformed_column_names()

    def get_column_names(self):
        return self.scorer.get_column_names()


def start_tcp_server(port):
    scoring_handler = TCPHandler()
    server = TServer.TSimpleServer(
        ScoringService.Processor(scoring_handler),
        TSocket.TServerSocket(port=port),
        TTransport.TBufferedTransportFactory(),
        TBinaryProtocol.TBinaryProtocolFactory(),
    )
    print('TCP scoring service listening on port {}...'.format(port))
    server.serve()


define('port', default=9090, help='Port to run scoring server on.', type=int)

def main():
    parse_command_line()
    start_tcp_server(options.port)


if __name__ == "__main__":
    main()

