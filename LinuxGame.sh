#!/bin/bash
sudo apt-get install libsdl1.2-dev libsdl-image1.2 libsdl-mixer1.2 libsdl-ttf2.0
python3 -m venv venv
python3 source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
deactivate
