# This is a sample application that configures the BNO085 using
# the Complex Arts micropython firmware
#
#     https://github.com/CompleArts/SensorBoardPython
#
# It prints out accelerometer readings every 50ms over serial.
#
# Great for checking if gravity is still around!
#
# As a bonus, it also blinks the onboard user LEDs.

import uasyncio as asyncio
from machine import Pin
from utime import ticks_diff
from bno085 import BNO085, Sensor

# create event asyncio event loop
loop = asyncio.get_event_loop()

# create BNO085 object
bno085 = BNO085(loop=loop)

# create GPIO pin objects to control LED
led1 = Pin(12, Pin.OUT)

# define coroutines to be run in the loop

# toggle LED coroutine
async def toggle_led(delay=1):

    # repeat forever
    while True:

        # toggle LEDs
        if led1.value():
            led1.off()
        else:
            led1.on()

        # sleep for delay seconds
        await asyncio.sleep(delay)

# add to event loop
loop.create_task(toggle_led())

# print accelerometer coroutine
async def print_accelerometer():

    # create and get queue from bno085 for reading accelerometer
    queue = bno085.get_sensor_input_queue(Sensor.ACCELEROMETER)

    # wait for first packet
    start_ms, packet = await queue.get()

    # initialize time count
    ticks_ms = start_ms

    # repeat forever
    while True:

        # print acceleration
        print('accel @ {:6.2f}s: {:+10.4f} {:+10.4f} {:+10.4f}'.format( ticks_diff(ticks_ms, start_ms) / 1000,
                                                                        packet['accel_x'],
                                                                        packet['accel_y'],
                                                                        packet['accel_z']), end='\r' )

        # wait for another packet to arrive
        ticks_ms, packet = await queue.get()

# add to event loop
loop.create_task(print_accelerometer())

# coroutine that initializes bno085, sleeps for 20s, then stops bno085
async def main():

    # wait 2 seconds to let bno085 initialize
    await asyncio.sleep(2)

    # request and print product id
    print('requesting product id...')
    product_id = await bno085.get_product_id()
    print(product_id)

    # set accelerometer feature set to produce reading every 50ms
    print('requesting accelerometer feature set...')
    accel = await bno085.get_feature_request(Sensor.ACCELEROMETER)
    accel['report_interval'] = 50000
    accel = await bno085.set_feature_command(**accel)
    print(accel)

    # sleeps for 20 seconds
    print('sleeping...')
    await asyncio.sleep(20)

    # reset accelerometer features
    print('reset features...')
    accel['report_interval'] = 0
    await bno085.set_feature_command(**accel)

    # terminate program
    print('terminating...')

# run main coroutine until it exits
loop.run_until_complete(main())