# Analog-Joystick-MCP-3008-Driver
Python script to use "[Adafruit Analog 2-axis Thumb Joystick with Button](https://www.adafruit.com/product/512)" with "[MCP3008](https://www.adafruit.com/product/856)" A/D converter.

I used this instead of the [Cupcade Adapter](https://www.adafruit.com/product/1916) in my [Super Game Pi](https://learn.adafruit.com/super-game-pi/overview) Build.

# Wiring
See: http://www.raspberrypi-spy.co.uk/2014/04/using-a-joystick-on-the-raspberry-pi-using-an-mcp3008/

# For Raspberry pi 3 the Wiring 
| Joystick | MCP3008       | Pi           |
|----------|---------------|--------------|
| Sel      | Pin 1 (CH0)   | -            |
| Xout     | Pin 2 (CH1)   | -            |
| Yout     | Pin 3 (CH2)   | -            |
| -        | Pin 10 (CS)   | Pin 24       |
| -        | Pin 11 (DIN)  | Pin 19       |
| -        | Pin 12 (DOUT) | Pin 21       |
| -        | Pin 13 (CLK)  | Pin 23       |
| GND      | Pin 9 (GND)   | GND          |
|          | Pin 14 (AGND) | GND          |
| VCC      | Pin 15 (VREF) | Pin 1 (3.3V) |
|          | Pin 16 (VDD)  | Pin 1 (3.3V) |

+ (10k) Resistor between VCC & Sel/CH0

# Clone
Don't forget to
```
git submodule init
git submodule update
```
... if you want to use the install-script to automatically install py-spidev & python-uinput

# Install
```
sudo ./install.sh
```
... or manually add joystick.py to rc.local if you installed py-spidev and python-uinput spearately
