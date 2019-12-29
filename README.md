# Complex Arts Sensor Board

This project has sample code for the [Complex Arts Sensor Board](http://complexarts.net/home/products:sensor_board).

You might also want to take a look at our [Arduino](https://github.com/ComplexArts/SensorBoardArduino) 
demos for the Sensor Board. 

## Installation

The code is written using Python.

You will need to download our custom binary version of the 
excellent [micropython](https://micropython.org) firmware that 
supports the BNO085 on the Sensor Board.

You will find the latest firmware binary in the latest 
[releases](https://github.com/ComplexArts/SensorBoardPython/releases).

Installation is done with the `epstool.py` as described in 
[here](https://micropython.org/download#esp32).

First erase the ESP32 flash

    esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

Then program the firmware starting at address 0x1000:

    esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 firmware.bin

## Demos

Two demos are provided:

1. [accelerometer.py](https://github.com/ComplexArts/SensorBoardPython/tree/master/accelerometer.py)  
   Initializes the BNO085 and prints accelerometer readings over serial while blinking the user LEDs.

2. [orientation.py](https://github.com/ComplexArts/SensorBoardPython/tree/master/orientation.py)  
   Initializes the BNO085 and prints orientation readings over serial while blinking the user LEDs.

The easiest way to install these programs is using a tool such as 
[adafruit's ampy](https://pypi.org/project/adafruit-ampy/0.6.3/).
