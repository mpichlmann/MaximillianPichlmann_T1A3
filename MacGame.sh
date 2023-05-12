#!/bin/bash
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
python3 -m venv venv
python3 source venv/vin/activate
python3 -m pip install -r requirements.txt
python3 main.py
deactivate