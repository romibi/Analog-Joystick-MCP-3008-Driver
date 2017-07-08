#!/bin/bash
cd python-uinput
python setup.py install
cd ../py-spidev
python setup.py install
# todo add joystick.py to rc.local
