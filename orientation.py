# This is a sample application that configures the BNO085 using
# the Complex Arts micropython firmware
#
#     https://github.com/CompleArts/SensorBoardPython
#
# It prints out orientation readings every 50ms over serial.
#
# Great for the ones in need of some orientation!
#
# As a bonus, it also blinks the onboard user LEDs.

import uasyncio as asyncio
from machine import Pin
from bno085 import BNO085, Sensor, Orientation

# create event asyncio event loop
loop = asyncio.get_event_loop()

# create BNO085 object
bno085 = BNO085(loop=loop)

# create GPIO pin objects to control LEDs
led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)

# define coroutines to be run in the loop

# toggle LED coroutine
async def toggle_leds(delay=1):

    # repeat forever
    while True:

        # toggle LEDs
        if led1.value():
            led1.off()
            led2.on()
        else:
            led1.on()
            led2.off()

        # sleep for delay seconds
        await asyncio.sleep(delay)

# add to event loop
loop.create_task(toggle_leds())

# print orientation coroutine
async def print_orientation():

    # create and get queue from bno085 for reading rotation vector
    queue = bno085.get_sensor_input_queue(Sensor.ROTATION_VECTOR)

    # wait for first packet
    start_ms, packet = await queue.get()

    # initialize time count
    ticks_ms = start_ms

    # repeat forever
    while True:
        
        # create orientation object from packet 
        orient = Orientation(**packet)
        
        # convert quaternion to Euler angles in degrees
        roll, pitch, yaw = [Orientation.RAD_TO_DEG * x for x in orient.to_euler()]
        
        # print orientation
        print('quat @ {:6.2f}s: {:+10.4f} {:+10.4f} {:+10.4f}'.format( (ticks_ms - start_ms) / 1000,
                                                                       roll, pitch, yaw ), end='\r' )

        # wait for another packet to arrive
        ticks_ms, packet = await queue.get()
        
# add to event loop
loop.create_task(print_orientation())

# coroutine that initializes bno085, sleeps for 20s, then stops bno085
async def main():

    # wait 2 seconds to let bno085 initialize
    await asyncio.sleep(2)

    # request and print product id
    print('requesting product id...')
    product_id = await bno085.get_product_id()
    print(product_id)

    # set rotation vector feature set to produce reading every 50ms
    print('requesting orientation feature set...')
    orient = await bno085.get_feature_request(Sensor.ROTATION_VECTOR)
    orient['report_interval'] = 50000
    orient = await bno085.set_feature_command(**orient)

    # sleeps for 20 seconds
    print('sleeping...')
    await asyncio.sleep(20)

    # reset orienterometer features
    print('reset features...')
    orient['report_interval'] = 0
    await bno085.set_feature_command(**orient)

    # terminate program
    print('terminating...')

# run main coroutine until it exits
loop.run_until_complete(main())