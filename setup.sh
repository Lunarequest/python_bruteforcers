#!/bin/bash
[ "$UID" -eq 0 ] || exec sudo "$0" "$@"
sudo python3 -m pip install colorama
sudo python3 -m pip install paramiko

echo "


required packages installed"