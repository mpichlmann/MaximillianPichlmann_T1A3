#!/bin/bash
python3 -m venv venv
python3 source venv/vin/activate
python3 -m pip install -r requirements.txt
python3 main.py
deactivate