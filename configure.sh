#!/bin/bash

apt update && pkg update && apt upgrade && pkg upgrade
apt install python && pkg install python
pip install requests
pip install pyfiglet
python3 nextsign.py