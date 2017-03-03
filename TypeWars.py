import sys
import pygame as P
from word import Word
from letter import Letter
import Globals as G


P.init()

class Player():
    def __init__(self, index=0, counter=0, health=100):
        self.index = index
        self.counter = counter
        self.health = health

    def modifyHealth(self, value):
        if self.health == 0 or value > 0:
            pass
        else:
            value = self.health + value
            if value < 0:
                self.health = 0
            else:
                self.health = value

    def resetHealth(self):
        self.health = 100

    def modifyIndex(self, value):
        if value < 0:
            pass
        else:
            value = self.index + value
            self.index = value

    def resetIndex(self):
        self.index = 0

    def calculateWPM(self):
        time_elapsed = float(self.counter) / 60
        return self.index / time_elapsed

    def updateCounter(self, value):
        self.counter = value
