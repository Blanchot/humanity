#!/usr/bin/env python
"""
================================================
ABElectronics Servo Pi pwm controller | PWM servo controller demo
run with: python demo_servomove.py
================================================
This demo shows how to set the limits of movement on a servo
and then move between those positions
"""

from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
import time
import sys # added because it I get the first import error below
sys.path.append('usr/local/lib/python3.5/dist-packages/ServoPi')

try:
    from ServoPi import Servo
except ImportError:
    print("Failed to import ServoPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append("..")
        from ServoPi import Servo
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")


# My testing mods

servo = Servo(0x40)
servo.set_low_limit(1.0)
servo.set_high_limit(2.0)
servo.output_enable()

'''    
def main():
    """
    Main program function
    """
    # create an instance of the servo class on I2C address 0x40
    servo = Servo(0x40)

    # set the servo minimum and maximum limits in milliseconds
    # the limits for a servo are typically between 1ms and 2ms.

    servo.set_low_limit(1.0)
    servo.set_high_limit(2.0)

    # Enable the outputs
    servo.output_enable()
    
    # move the servo across its full range in increments of 10
    while True:
        for i in range(0, 250, 10):
            servo.move(1, i)
            time.sleep(1) #was 0.05

        for i in range(250, 0, -10):
            servo.move(1, i)
            time.sleep(1)

if __name__ == "__main__":
    main()

'''
