# Complex Arts Sensor Board

This project has sample code for the 
[Complex Arts Sensor Board](http://complexarts.net/home/products:sensor_board)
written in Python.

You might also want to take a look at our [Arduino](https://github.com/ComplexArts/SensorBoardArduino) 
demos for the Sensor Board. 

## Installation

You will need to download our custom binary version of the 
excellent [micropython](https://micropython.org) firmware that 
supports the BNO085 on the Sensor Board.

You will find the latest firmware binary in the latest 
[releases](https://github.com/ComplexArts/SensorBoardPython/releases). 
The firmware binary is the file `firmware.bin`. 

Installation is done with the `epstool.py` as described in 
[here](https://micropython.org/download#esp32).

First erase the ESP32 flash

    esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

Then program the firmware starting at address 0x1000:

    esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 firmware.bin

Replace `/dev/ttyUSB0` by whatever serial port your board is connected to.
This can vary depending on the operating system you're using.

## Demos

Two demos are provided:

1. [accelerometer.py](https://github.com/ComplexArts/SensorBoardPython/tree/master/accelerometer.py)  
   Initializes the BNO085 and prints accelerometer readings over serial while blinking one of the user LEDs.

2. [orientation.py](https://github.com/ComplexArts/SensorBoardPython/tree/master/orientation.py)  
   Initializes the BNO085 and prints orientation readings over serial while blinking one of the user LEDs.

The easiest way to install these programs on a board running the micropython 
firmware is by using a tool such as 
[adafruit's ampy](https://pypi.org/project/adafruit-ampy/0.6.3/).

For example:

    ampy -p /dev/ttyUSB0 put accelerometer.py

will copy the file `accelerometer.py` to the board.

You can run the program by connecting to the board using a serial
monitor program such as `picocom` or `minicom` and simply importing

    import accelerometer
    
after the REPL prompt. You might need to reset the board after using
`ampy`.

## Documentation

Detailed documentation for the module `bno085`, including a discussion 
of the above demos, is available 
[here](http://complexarts.net/docs/bno085/).
                                                         
                                                         
                                                         
                                                         
                                                         
)