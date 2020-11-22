# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:24:10 2020

@author: rikus
"""

import math
from tkinter import *
import winsound
import time
import random


WIDTH = 1500
HEIGHT = 1000

LEFT_WALL = 0
RIGHT_WALL = WIDTH
FLOOR = HEIGHT
CEILING = 0


window = Tk()
# canvas is tkinter widget
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
window.title("Animation")
canvas.pack()


def beep():
    winsound.Beep(5000, 1) #params: frequency (hertz), duration (milliseconds)



class Ball(object):
    def __init__(self, timeStep):
        self.angle = math.radians(random.uniform(1,90)) # Asteet tulee muuttaa trigonometrisiä funktioita varten radiaaneiksi.
        self.velocity = random.uniform(20,30)
        self.xspeed = math.cos(self.angle) * self.velocity
        self.yspeed = math.sin(self.angle) * self.velocity
        self.timeStep = timeStep
        self.g = -9.81
        self.friction = -0.50
        self.size = 50
        self.lastBounce = time.time()
        self.wasInside = [False,False,False,False]
        self.colours = ["red", "green", "blue", "orange", "yellow", "cyan", "magenta", "dodgerblue",
           "turquoise", "grey", "gold", "pink"]
        self.colour = random.choice(colours)
        self.bounciness = 0.80
        
        # Luodaan pallo ja siirretään se vasempaan alareunaan.
        self.shape = canvas.create_oval(1, 1,self.size,self.size, fill=self.colour)
        canvas.move(self.shape, self.size, HEIGHT-self.size)
       
    def move(self):
        self.yspeed = self.yspeed + self.timeStep*self.g
        canvas.move(self.shape, self.xspeed, -self.yspeed)
        pos = canvas.coords(self.shape)
        topLeftX, topLeftY, bottomRightX, bottomRightY = pos[0], pos[1], pos[2], pos[3]
        
        if topLeftY <= CEILING and self.wasInside[0] == False:
            self.wasInside[0] = True
            self.yspeed = -(self.bounciness*self.yspeed)
            beep()
        else:
            self.wasInside[0] = False
            
            
        if bottomRightY >= FLOOR and self.wasInside[1] == False:
            currentBounce = time.time()
            sinceLastBounce = currentBounce - self.lastBounce
            self.lastBounce = currentBounce
            if sinceLastBounce > 0.1:
                self.wasInside[1] = True
                self.yspeed = -(self.bounciness*self.yspeed)
                beep()
            else:
                self.g, self.yspeed = 0, 0
                if self.xspeed > 0:
                    self.xspeed = self.xspeed + self.timeStep*self.friction
                else:
                    self.xspeed = self.xspeed - self.timeStep*self.friction
                    
        else:
            self.wasInside[1] = False
            
  
        if topLeftX <= LEFT_WALL and self.wasInside[2] == False:
            self.wasInside[2] = True
            self.xspeed = -(self.bounciness*self.xspeed)
            beep()
        else:
            self.wasInside[2] = False
            
            
        if bottomRightX >= RIGHT_WALL and self.wasInside[3] == False:
            self.wasInside[3] = True
            self.xspeed = -(self.bounciness*self.xspeed)
            beep()
        else:
            self.wasInside[3] = False


colours = ["red", "green", "blue", "orange", "yellow", "cyan", "magenta", "dodgerblue",
           "turquoise", "grey", "gold", "pink"]

timeStep = 0.03 # in seconds (0.01)

balls = []
for i in range(10):
    balls.append(Ball(timeStep))


while True:
    for ball in balls:
        ball.move()
    window.update()
    time.sleep(0.009)
    

window.mainloop()
















