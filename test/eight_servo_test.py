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

semaphore = {
'A': (4, 0), 'B': (4, 1), 'C': (4, 2), 'D': (4, 3), 'E': (4, 4),
'F': (3, 0), 'G': (3, 1), 'H': (3, 2), 'I': (3, 3), 'J': (3, 4),
'K': (2, 0), 'L': (2, 1), 'M': (2, 2), 'N': (2, 3), 'O': (2, 4),
'P': (1, 0), 'R': (1, 1), 'S': (1, 2), 'T': (1, 3), 'U': (1, 4),
' ': (0, 0), 'V': (0, 1), 'W': (0, 2), 'X': (0, 3), 'Y': (0, 4)}

# calibration of the 8 servos (in 250 steps) from lowest position upwards
calib_06 = [0, 63, 120, 188, 250] #fig 1 left arm
calib_05 = [250, 188, 120, 63, 0] #fig 1 right arm
calib_02 = [0, 55, 105, 170, 250] #fig 2 left arm
calib_01 = [250, 188, 120, 63, 0] #fig 2 right arm
calib_10 = [0, 60, 115, 180, 250] #fig 3 left arm
calib_09 = [250, 180, 105, 50, 0] #fig 3 right arm
calib_04 = [0, 52, 115, 188, 250] #fig 4 left arm
calib_03 = [250, 188, 110, 55, 0] #fig 4 right arm


def calibrateServos():
    servos.move(6, calib_06[2])
    servos.move(5, calib_05[2])
    servos.move(2, calib_02[2])
    servos.move(1, calib_01[2])
    servos.move(10, calib_10[2])
    servos.move(9, calib_09[2])
    servos.move(4, calib_04[2])
    servos.move(3, calib_03[2])

def up():
  servo.move(6,0)
  servo.move(5,250)
  servo.move(2,0)
  servo.move(1,250)
  servo.move(10,0)
  servo.move(9,250)
  servo.move(4,0)
  servo.move(3,250)

def down():
  servo.move(6,250)
  servo.move(5,0)
  servo.move(2,250)
  servo.move(1,0)
  servo.move(10,250)
  servo.move(9,0)
  servo.move(4,250)
  servo.move(3,0)


'''
Note: all indications of left/right are from my frontal view
Note: numeric arm ranges are from up to down
Figure 1 (top left): left_arm: s6 (0-250), right_arm s5 (250-0)
Figure 2 (top right): left_arm: s2 (0-250), right_arm s1 (250-0)
Figure 3 (bot left): left_arm: s10 (0-250), right_arm s9 (250-0)
Figure 4 (bot right): left_arm: s4 (0-250), right_arm s3 (250-0)
'''
