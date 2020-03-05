# awater_01.py code for final humanity piece (running on 'awater')
# USAGE: (sudo) python3 -i awater_01.py
# using ABElectronics Servo Pi pwm controller
# based on ABElectronics PWM servo controller demo
# 04.03.2020 initial calibration of servos and verb list
from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals


import time, random
import sys # to import verb list(s)
sys.path.append("..") #stored in 'humanity directory' (so I can access these with from the test directory)
from shortestList import verbs


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
# for AWATER
fig1_L = [250, 170, 107, 50, 0] #fig 1 left arm (servo 1)
fig1_R = [0, 50, 115, 188, 250] #fig 1 right arm (servo 2)
fig2_L = [250, 195, 127, 60, 0] #fig 2 left arm (servo 7)
fig2_R = [0, 55, 120, 180, 250] #fig 2 right arm (servo 8)
fig3_L = [230, 175, 112, 50, 0] #fig 3 left arm (servo 11)
fig3_R = [0, 50, 120, 180, 230] #fig 3 right arm (servo 12)
fig4_L = [250, 187, 125, 60, 10] #fig 4 left arm (servo 15)
fig4_R = [0, 57, 118, 180, 250] #fig 4 right arm (servo 16)


# lets make a list of lists of the 8 servos... 
# each list containing the board pin # and the list of calibrated positions
# i.e. servoList = [[pin#, fig1_L], [pin#, fig1_R], etc.]
'''
Fig. 1L board pin: 1
Fig. 1R board pin: 2
Fig. 2L board pin: 7
Fig. 2R board pin: 8
Fig. 3L board pin: 11
Fig. 3R board pin: 12
Fig. 4L board pin: 15
Fig. 4R board pin: 16
'''
servoList = [
[1, fig1_L], [2, fig1_R], [7, fig2_L], [8, fig2_R],
[11,fig3_L], [12, fig3_R], [15, fig4_L], [16, fig4_R]
]


def center(): #center servos
    servo.move(1, fig1_L[2])
    servo.move(2, fig1_R[2])
    servo.move(7, fig2_L[2])
    servo.move(8, fig2_R[2])
    servo.move(11, fig3_L[2])
    servo.move(12, fig3_R[2])
    servo.move(15, fig4_L[2])
    servo.move(16, fig4_R[2])


def down():
  servo.move(1, fig1_L[0])
  servo.move(2, fig1_R[0])
  servo.move(7, fig2_L[0])
  servo.move(8, fig2_R[0])
  servo.move(11, fig3_L[0])
  servo.move(12, fig3_R[0])
  servo.move(15, fig4_L[0])
  servo.move(16, fig4_R[0])


def up():
  servo.move(1, fig1_L[4])
  servo.move(2, fig1_R[4])
  servo.move(7, fig2_L[4])
  servo.move(8, fig2_R[4])
  servo.move(11, fig3_L[4])
  servo.move(12, fig3_R[4])
  servo.move(15, fig4_L[4])
  servo.move(16, fig4_R[4])


def test():
  for s in servoList:
    #print('s[0]: ',s[0])
    for p in s[1]:
      #print('servo.move(',s[0],',',p,')')
      servo.move(s[0],p)
      time.sleep(0.4)
      #time.sleep(3) #for testing
  center()


def display(vier):
  posList= [] #create an empty list of positions
  for letter in vier:
    #print(semaphore[letter]) #TESTING: prints the tuple for each letter
    posList.extend(semaphore[letter]) #appends each element of the tuple to posList (Oh joy!)
  #print(posList) #TESTING: prints the list of positions
  center()
  time.sleep(2)
  for i in range(0,8):
    #print('Servo #:', servoList[i][0], 'Pos #:', servoList[i][1][posList[i]]) #TESTING
    servo.move(servoList[i][0], servoList[i][1][posList[i]])
    time.sleep(0.4)


# MANUAL INPUT
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


def run():
  vier= random.choice(verbs).upper()
  print('Humanity i',vier,'you.')
  display(vier)
  time.sleep(30)
  run()

