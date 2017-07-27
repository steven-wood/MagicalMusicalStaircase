import time, sys
import stair
import pygame
import photocell
import sched
import RPi.GPIO as GPIO
import os

average = 0
const = 0.1
pins = [23, 22, 27, 18, 17, 4, 19, 13, 6, 5, 25, 24]
baseNote = 50
x = int(sys.argv[1])

pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
runningStair = stair.Stair(pins[x], pygame.mixer.Sound("/home/pi/PROJECT/PianoFiles/"+str(39148+baseNote+x)+"__jobro__piano-ff-0"+str(baseNote+x)+".wav"))
counter = 0


def restartProgram():
    GPIO.cleanup()
    python = sys.executable
    os.execl(python, python, *sys.argv)


while True:
    time.sleep(0.05)
    light = photocell.getLightLevel(pins[x])
    average = const*light+(1-const)*average
    if light < 0:
        restartProgram()
    runningStair.checkTriggered(light, average)
