import sys
import pygame
from word import Word
from letter import Letter
import Globals as G

pygame.init()

letters = []
for x in "abcde":
	letters.append(Letter(x,None,30,G.BLUE))

for x in letters:
	print x.get_letter()

abcde = Word(letters)

print abcde.get_text()