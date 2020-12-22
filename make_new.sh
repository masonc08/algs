#!/bin/bash

TYPE=$1
NUMBER=$2
NAME=$3

cat > ./algorithms/$NAME.py <<EOL
"""
$TYPE $NUMBER

"""


EOL
