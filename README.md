# Complex Arts Sensor Board

This project has sample code for the [Complex Arts Sensor Board](http://complexarts.net/home/products:sensor_board).

## Installation

The code is written using Python.

You will need to download our custom binary version of the 
excellent [micropython](https://micropython.org) firmware that 
supports the BNO085 on the Sensor Board.

You might also want to take a look at our [Arduino](https://github.com/ComplexArts/SensorBoardArduino) 
demos for the Sensor Board. 

## Demos

Two demos are provided:

1. [accelerometer.py](https://github.com/ComplexArts/SensorBoardPython/tree/master/accelerometer.py)  
   Initializes the BNO085 and prints accelerometer readings over serial while blinking the user LEDs.

2. [orientation.py](https://github.com/ComplexArts/SensorBoardPython/tree/master/orientation.py)  
   Initializes the BNO085 and prints orientation readings over serial while blinking the user LEDs.
