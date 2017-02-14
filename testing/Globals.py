import sys
import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)
SPECIAL_KEYS = [pygame.K_ESCAPE,pygame.K_BACKSPACE,pygame.K_TAB,pygame.K_RETURN,pygame.K_SPACE]
WORDLIST = []
DEF_LETTER_COLOR = WHITE
DEF_WORD_COLOR = WHITE
MONOSPACE_FONT = "./static/Anonymous_Pro.ttf"

def make_word_list():
	global WORDLIST
	with open('wordList.txt') as f:
		WORDLIST = f.read().splitlines()
	return WORDLIST

