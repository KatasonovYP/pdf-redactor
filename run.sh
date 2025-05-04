#!/bin/bash

python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 example.py <input.pdf >output.pdf
