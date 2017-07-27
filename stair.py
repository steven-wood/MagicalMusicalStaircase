import pygame
import photocell

class Stair:

    def __init__(self, PiPin, sound):
        self.PiPin = PiPin
        self.sound = sound
        self.lastWasTrigger = False

    def checkTriggered(self, val, average):
        triggered = val-average > 20
        if(triggered == True and self.lastWasTrigger == False):
            self.playSound()
            self.lastWasTrigger = True
        elif(triggered == False):
            self.lastWasTrigger = False

    #def checkForLaser(self):
    #    return Photocell.getLightLevel(self.PiPin) > 50

    def playSound(self):
        pygame.mixer.Sound.play(self.sound)
        pygame.mixer.music.stop()

    
        
