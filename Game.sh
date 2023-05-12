#!/bin/bash
os_name=$(uname -s)
if [ "$os_name" == "Linux" ]; then
    sudo apt update
    sudo apt install -y python3
    sudo apt-get install libsdl1.2-dev libsdl-image1.2 libsdl-mixer1.2 libsdl-ttf2.0
    python3 -m venv venv
    python3 source venv/bin/activate
    python3 -m pip install -r requirements.txt
    python3 main.py
    deactivate
elif [ "$os_name" == "Darwin" ]; then
    brew install python
    brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
    python3 -m venv venv
    python3 source venv/vin/activate
    python3 -m pip install -r requirements.txt
    python3 main.py
    deactivate
else
    echo "Unsupported operating system"
fi