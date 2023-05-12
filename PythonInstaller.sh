#!/bin/bash
os_name=$(uname -s)
if [ "$os_name" == "Linux" ]; then
    sudo apt update
    sudo apt install -y python3
elif [ "$os_name" == "Darwin" ]; then
    brew install python
else
    echo "Unsupported operating system"
fi
