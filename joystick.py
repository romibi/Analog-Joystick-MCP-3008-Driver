#!/usr/bin/python
#--------------------------------------   
# This script reads data from a 
# MCP3008 ADC device using the SPI bus.
#
# Analogue joystick version!
#
# Author : Matt Hawkins
# Date   : 17/04/2014
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import spidev
import time
import os
import uinput

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Define sensor channels
# (channels 3 to 7 unused)
swt_channel = 0
vrx_channel = 1
vry_channel = 2

# Define delay between readings (s)
delay = 0.01

# Config
enable_debug = False

# Calibration values (somewhat precalibrated)
swt_split = 500

device = uinput.Device((
  uinput.BTN_JOYSTICK,
  uinput.ABS_X+(0,1024,0,0),
  uinput.ABS_Y+(0,1024,0,0),
))

while True:

# Read the joystick position data
  vrx_pos = ReadChannel(vrx_channel)
  vry_pos = ReadChannel(vry_channel)
  
# Read switch state
  swt_val = ReadChannel(swt_channel)

  # Calculate Button
  #if swt_val<swt_split:
    #button_pressed=1
  #else:
    #button_pressed=0
  
# Print out results
  if enable_debug:
    os.system('clear')
    print("X : {}  Y : {}  Switch : {}".format(vrx_pos,vry_pos,swt_val))

# Handle Calculated Values
  device.emit(uinput.ABS_X, vrx_pos, syn=False)
  device.emit(uinput.ABS_Y, vry_pos)
  btn_pressed=0
  if swt_val < swt_split:
    btn_pressed=1
  device.emit(uinput.BTN_JOYSTICK,btn_pressed)

  time.sleep(delay)
