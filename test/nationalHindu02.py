# nationalHindu02 (stripped down due to low memory)

from collection import *
import time
import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4)) #initialize i2c

#initialize servos
import pca9685
import servo
servos = servo.Servos(i2c)

#initialize oled display
import ssd1306
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
button_A = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
button_B = machine.Pin(16, machine.Pin.IN)
button_C = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
oled.fill(0)
oled.text('National Hindu', 0, 0)
oled.text('Version 1', 0, 10)
oled.text('Words: ' + str(len(eights)), 0, 20)
oled.show()

# seeded list of past five strings for updateDisplay()
pastStr = ['        ', '        ', '        ', '        ', '        ']

semaphore = {'A': (4, 0), 'B': (4, 1), 'C': (4, 2), 'D': (4, 3), 'E': (4, 4),
'F': (3, 0), 'G': (3, 1), 'H': (3, 2), 'I': (3, 3), 'J': (3, 4),
'K': (2, 0), 'L': (2, 1), 'M': (2, 2), 'N': (2, 3), 'O': (2, 4),
'P': (1, 0), 'R': (1, 1), 'S': (1, 2), 'T': (1, 3), 'U': (1, 4),
' ': (0, 0), 'V': (0, 1), 'W': (0, 2), 'X': (0, 3), 'Y': (0, 4)}

# calibration of servos in microseconds from lowest position upwards
calib15 = [2400, 1850, 1350, 950, 600]
calib14 = [600, 1050, 1500, 2050, 2400]
calib13 = [2400, 1950, 1450, 950, 600]
calib12 = [600, 1000, 1475, 2000, 2400]
calib11 = [2400, 2075, 1550, 1050, 600]
# calib11 = [2400, 2025, 1500, 1000, 600] # alternative settings...
calib10 = [600, 950, 1425, 1950, 2400]
calib9 = [2400, 2000, 1475, 950, 600]
calib8 = [600, 1050, 1500, 2000, 2400]
calib7 = [2400, 2050, 1500, 1050, 600]
calib6 = [600, 870, 1330, 1900, 2400]
calib5 = [2400, 2000, 1500, 1030, 600]
calib4 = [600, 950, 1385, 1850, 2300]
calib3 = [2400, 2000, 1450, 950, 600]
calib2 = [600, 970, 1350, 1800, 2400]
calib1 = [2400, 2050, 1525, 1050, 600]
calib0 = [600, 1050, 1525, 2050, 2400]

# lets make a list of lists
servoList = [calib0, calib1, calib2, calib3, calib4, calib5, calib6, calib7, calib8,
calib9, calib10, calib11, calib12, calib13, calib14, calib15]

def calibrateServos():
    servos.position(0, us=calib0[2])
    servos.position(1, us=calib1[2])
    servos.position(2, us=calib2[2])
    servos.position(3, us=calib3[2])
    servos.position(4, us=calib4[2])
    servos.position(5, us=calib5[2])
    servos.position(6, us=calib6[2])
    servos.position(7, us=calib7[2])
    servos.position(8, us=calib8[2])
    servos.position(9, us=calib9[2])
    servos.position(10, us=calib10[2])
    servos.position(11, us=calib11[2])
    servos.position(12, us=calib12[2])
    servos.position(13, us=calib13[2])
    servos.position(14, us=calib14[2])
    servos.position(15, us=calib15[2])

def releaseServos():
    for i in range(16):
        servos.release(i)

def updateDisplay(s):
    i = len(pastStr) # get index length of pastStr
    oled.fill(0)
    oled.text(pastStr[i-5].lower() + pastStr[i-4].upper(), 0, 0) # top line
    oled.text(pastStr[i-3].upper() + pastStr[i-2].lower(), 0, 10) # middle line
    oled.text(pastStr[i-1].lower() + s.upper(), 0, 20) # bottom line
    pastStr.append(s) # add current string to list
    oled.show()

def inputStr(s):
    calibrateServos() # set all 8 figures in the 'm' position
    time.sleep(2) # wait a moment before setting row of new positions
    s = s.upper()
    # print(s)
    let0 = s[0]
    let1 = s[1]
    let2 = s[2]
    let3 = s[3]
    let4 = s[4]
    let5 = s[5]
    let6 = s[6]
    let7 = s[7]
    servos.position(15, us=calib15[semaphore[let0][0]])
    time.sleep(.2)
    servos.position(14, us=calib14[semaphore[let0][1]])
    time.sleep(.2)
    servos.position(13, us=calib13[semaphore[let1][0]])
    time.sleep(.2)
    servos.position(12, us=calib12[semaphore[let1][1]])
    time.sleep(.2)
    servos.position(11, us=calib11[semaphore[let2][0]])
    time.sleep(.2)
    servos.position(10, us=calib10[semaphore[let2][1]])
    time.sleep(.2)
    servos.position(9, us=calib9[semaphore[let3][0]])
    time.sleep(.2)
    servos.position(8, us=calib8[semaphore[let3][1]])
    time.sleep(.2)
    servos.position(7, us=calib7[semaphore[let4][0]])
    time.sleep(.2)
    servos.position(6, us=calib6[semaphore[let4][1]])
    time.sleep(.2)
    servos.position(5, us=calib5[semaphore[let5][0]])
    time.sleep(.2)
    servos.position(4, us=calib4[semaphore[let5][1]])
    time.sleep(.2)
    servos.position(3, us=calib3[semaphore[let6][0]])
    time.sleep(.2)
    servos.position(2, us=calib2[semaphore[let6][1]])
    time.sleep(.2)
    servos.position(1, us=calib1[semaphore[let7][0]])
    time.sleep(.2)
    servos.position(0, us=calib0[semaphore[let7][1]])
    updateDisplay(s)
    time.sleep(1)
    # releaseServos()

def getEight():
    r = urandom.getrandbits(10) # 0 to 1023
    if r < len(eights):
        s = eights[r]
        return s
    else:
        return getEight()

def randStrTimer(ms, sd):
    urandom.seed(sd)
    print('Seed: ' + str(sd))
    print('Updates: ' + str(ms) + ' secs')
    while True:
        inputStr(getEight())
        time.sleep(ms)
