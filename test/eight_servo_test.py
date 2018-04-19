# eight_servo_test
# using ABElectronics Servo Pi pwm controller
# based on ABElectronics PWM servo controller demo

from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
import time

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

# SETUP
servo = Servo(0x40)
servo.set_low_limit(0.6) #was 1.0 
servo.set_high_limit(2.4) #was 2.0
servo.output_enable()

'''
Note: all indications of left/right are from my frontal view
Note: numeric arm ranges are from up to down
Figure 1 (top left): left_arm: s6 (0-250), right_arm s5 (250-0)
Figure 2 (top right): left_arm: s2 (0-250), right_arm s1 (250-0)
Figure 3 (bot left): left_arm: s10 (0-250), right_arm s9 (250-0)
Figure 4 (bot right): left_arm: s4 (0-250), right_arm s3 (250-0)
'''
