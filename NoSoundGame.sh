#!/bin/bash
pip3 install -r requirements.txt
python3 -m venv venv
python3 source venv/vin/activate
python3 main.py
deactivate