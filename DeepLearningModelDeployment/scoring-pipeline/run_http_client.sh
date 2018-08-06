#!/usr/bin/env bash

set -e

#
# This example script demonstrates how to communicate with the Driverless AI Scoring Service via HTTP.
# The protocol used is JSON-RPC 2.0.
#

# -----------------------------------------------
# Name           Type      Range                 
# -----------------------------------------------
# L3_S30_D3521   float64   [0.4, 1718.39] or None
# -----------------------------------------------

echo "Scoring individual rows..."

curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 1,
  "method": "score",
  "params": {
    "row": {
      "L3_S30_D3521": 864.69274373311
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 2,
  "method": "score",
  "params": {
    "row": {
      "L3_S30_D3521": 1513.0393848084004
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 3,
  "method": "score",
  "params": {
    "row": {
      "L3_S30_D3521": 429.60212749658035
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 4,
  "method": "score",
  "params": {
    "row": {
      "L3_S30_D3521": 1146.7383575406232
    }
  }
}
EOF
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 5,
  "method": "score",
  "params": {
    "row": {
      "L3_S30_D3521": 1567.7482893538406
    }
  }
}
EOF

echo "Scoring multiple rows..."

curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id": 1,
  "method": "score_batch",
  "params": {
    "rows": [
      {
        "L3_S30_D3521": 864.69274373311
      },
      {
        "L3_S30_D3521": 1513.0393848084004
      },
      {
        "L3_S30_D3521": 429.60212749658035
      },
      {
        "L3_S30_D3521": 1146.7383575406232
      },
      {
        "L3_S30_D3521": 1567.7482893538406
      }
    ]
  }
}
EOF

echo "Get the input columns"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_column_names",
  "params":{}
}
EOF

echo "Get the transformed columns"
curl http://localhost:9090/rpc --header "Content-Type: application/json" --data @- <<EOF
{
  "id":1,
  "method":"get_transformed_column_names",
  "params":{}
}
EOF
