import pygame
import random

class person ():
    def __init__(self,display,color):
        self.display=display
        self.color=color
        if self.color=='green':
            self.color=(0,200,0)
        elif self.color=='red':
            self.color=(255,0,0)
        elif self.color=='amber':
            self.color=(255,255,0)
    def wander_around(self,random_x,random_y):
        pygame.draw.circle(self.display,self.color,[random_x,random_y],6,1)
