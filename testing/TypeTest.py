import pygame
from word import Word
from letter import Letter
from typeGame import TypeGame
import pygame
import Globals as G

class TypeTest(TypeGame): 

    def __init__(self, screen):
        TypeGame.__init__(self, screen, pygame.Color('#ff33ff'))

    