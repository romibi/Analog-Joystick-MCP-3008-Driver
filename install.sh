#!/bin/bash
cd python-uinput
python setup.py install
rm -R build
cd ../py-spidev
python setup.py install
cd ../

installed=`grep joystick.py /etc/rc.local`
if [ "$installed" == "" ]; then
    sed -i '/^exit 0/i\'`pwd`'/joystick.py &' /etc/rc.local
fi
