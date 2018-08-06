# Copyright 2018 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import sys

sys.path.append('gen-py')

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from h2oai_scoring import ScoringService
from h2oai_scoring.ttypes import Row

# -----------------------------------------------
# Name           Type      Range                 
# -----------------------------------------------
# L3_S30_D3521   float64   [0.4, 1718.39] or None
# -----------------------------------------------

socket = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = ScoringService.Client(protocol)
transport.open()

server_hash = client.get_hash()
print('Scoring server hash: '.format(server_hash))

print('Scoring individual rows...')
row1 = Row()
row1.l3S30D3521 = 1660.7575097837375  # L3_S30_D3521

row2 = Row()
row2.l3S30D3521 = 757.5741980572641  # L3_S30_D3521

row3 = Row()
row3.l3S30D3521 = 13.270270645952209  # L3_S30_D3521

row4 = Row()
row4.l3S30D3521 = 1565.4475937279708  # L3_S30_D3521

row5 = Row()
row5.l3S30D3521 = 1614.0547447809731  # L3_S30_D3521

score1 = client.score(row1, pred_contribs=False, output_margin=False)
print(score1)
score2 = client.score(row2, pred_contribs=False, output_margin=False)
print(score2)
score3 = client.score(row3, pred_contribs=False, output_margin=False)
print(score3)
score4 = client.score(row4, pred_contribs=False, output_margin=False)
print(score4)
score5 = client.score(row5, pred_contribs=False, output_margin=False)
print(score5)

print('Scoring multiple rows...')
rows = [row1, row2, row3, row4, row5]
scores = client.score_batch(rows, pred_contribs=False, output_margin=False)
print(scores)

print('Retrieve column names')
print(client.get_column_names())

print('Retrieve transformed column names')
print(client.get_transformed_column_names())

transport.close()


