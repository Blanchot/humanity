# eight_servo_test2.py
# USAGE: (sudo) python3 -i eight_servo_test2.py
# using ABElectronics Servo Pi pwm controller
# based on ABElectronics PWM servo controller demo
# 23.02.2020 started adding new code
 
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

#calibration of the 8 servos and their positions (from lowest position upwards)
#renaming from calib_## to fig#_L/R to make understanding code easier
fig1_L = [0, 63, 115, 188, 250] #fig 1 left arm
fig1_R = [250, 188, 113, 63, 0] #fig 1 right arm
fig2_L = [0, 55, 100, 170, 250] #fig 2 left arm
fig2_R = [250, 188, 120, 63, 0] #fig 2 right arm
fig3_L = [0, 60, 115, 180, 250] #fig 3 left arm
fig3_R = [250, 180, 105, 50, 0] #fig 3 right arm
fig4_L = [0, 52, 115, 188, 250] #fig 4 left arm
fig4_R = [250, 188, 110, 55, 0] #fig 4 right arm

# lets make a list of lists of the 8 servos... 
# each list containing the board pin # and the list of calibrated positions
# i.e. servoList = [[pin#, fig1_L], [pin#, fig1_R], etc.]
servoList = [
[6, fig1_L], [5, fig1_R], [2, fig2_L], [1, fig2_R],
[10,fig3_L], [9, fig3_R], [4, fig4_L], [3, fig4_R]
]


def center(): #center servos
    servo.move(6, fig1_L[2])
    servo.move(5, fig1_R[2])
    servo.move(2, fig2_L[2])
    servo.move(1, fig2_R[2])
    servo.move(10, fig3_L[2])
    servo.move(9, fig3_R[2])
    servo.move(4, fig4_L[2])
    servo.move(3, fig4_R[2])


def up():
  servo.move(6, fig1_L[0])
  servo.move(5, fig1_R[0])
  servo.move(2, fig2_L[0])
  servo.move(1, fig2_R[0])
  servo.move(10, fig3_L[0])
  servo.move(9, fig3_R[0])
  servo.move(4, fig4_L[0])
  servo.move(3, fig4_R[0])


def down():
  servo.move(6, fig1_L[4])
  servo.move(5, fig1_R[4])
  servo.move(2, fig2_L[4])
  servo.move(1, fig2_R[4])
  servo.move(10, fig3_L[4])
  servo.move(9, fig3_R[4])
  servo.move(4, fig4_L[4])
  servo.move(3, fig4_R[4])


def test():
  for s in servoList:
    #print('s[0]: ',s[0])
    for p in s[1]:
      #print('servo.move(',s[0],',',p,')')
      servo.move(s[0],p)
      time.sleep(0.4)
  center()


def display(vier):
  posList= [] #create an empty list of positions
  for letter in vier:
    print(semaphore[letter]) #prints the tuple for each letter
    posList.extend(semaphore[letter]) #appends each element of the tuple to posList (Oh joy!)
  print(posList)


#INPUT AND TESTING
def entry():
  vier= input('Type a 4 letter word...').upper()
  if len(vier)!=4:
    print('Incorrect length!')
  elif vier.isalpha():
    count=0
    for letter in vier:
      if letter in semaphore:
        count= count+1
    if count==4:
      print('Word ok:', vier)
      display(vier)
    else:
      print('Some letters unavailable!')



'''
Note: all indications of left/right are from my frontal view
Note: numeric arm ranges are from up to down
Figure 1 (top left): left_arm: s6 (0-250), right_arm s5 (250-0)
Figure 2 (top right): left_arm: s2 (0-250), right_arm s1 (250-0)
Figure 3 (bot left): left_arm: s10 (0-250), right_arm s9 (250-0)
Figure 4 (bot right): left_arm: s4 (0-250), right_arm s3 (250-0)
'''
