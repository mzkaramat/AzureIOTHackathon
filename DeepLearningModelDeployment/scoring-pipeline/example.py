# Copyright 2018 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy.special._ufuncs import expit
from scoring_h2oai_experiment_dovudusu import Scorer
from flask import request
import json
#
# The format of input record to the Scorer.score() method is as follows:
#

# -----------------------------------------------
# Name           Type      Range                 
# -----------------------------------------------
# L3_S30_D3521   float64   [0.4, 1718.39] or None
# -----------------------------------------------


#
# Create a singleton Scorer instance.
# For optimal performance, create a Scorer instance once, and call score() or score_batch() multiple times.
#

from flask import Flask
app = Flask(__name__)


scorer = Scorer()

@app.route("/")
def hello():
    print("request")
    par1 = request.args.get('par1')
    resp = scorer.score([par1])
    print(resp.index(min(resp)))
    print(type(resp.index(min(resp))))
    return ""+str(resp.index(min(resp)))

    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)