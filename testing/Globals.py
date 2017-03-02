import sys
import pygame as P
import random
import hashlib as HL

P.init()
P.font.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)
SKY_BLUE = (230, 247, 247)
OCEAN_BLUE = (0,31,75)
JUNGLE_GREEN = (0,75,42)
CRIMSON = (126, 0, 0)

SPECIAL_KEYS = [P.K_ESCAPE,P.K_BACKSPACE,P.K_TAB,P.K_RETURN,P.K_SPACE]
WORDLIST = []
DEF_LETTER_COLOR = WHITE
DEF_WORD_COLOR = WHITE
MONOSPACE_FONT = "./static/Anonymous_Pro.ttf"
SCORE = 0
D_WIDTH  = 640
D_HEIGHT = 480
DEF_DIMENSIONS = (D_WIDTH,D_HEIGHT)
DIFFICULTY_LEVEL = 1
TOP_CENTER = (320,120)
SCREEN_CENTER = (320,240) 

def make_word_list(wordList='wordList.txt'):
	global WORDLIST
	with open(wordList) as f:
		WORDLIST = f.read().splitlines()
	return WORDLIST

def draw(gm,label,center):
    label_rect = label.get_rect(center=center)
    gm.screen.blit(label,label_rect)

def set_difficulty_easy():
	global DIFFICULTY_LEVEL
	DIFFICULTY_LEVEL = 1
	print "Difficulty level is -- {}".format(DIFFICULTY_LEVEL)

def set_difficulty_medium():
	global DIFFICULTY_LEVEL
	DIFFICULTY_LEVEL = 3
	print "Difficulty level is -- {}".format(DIFFICULTY_LEVEL)

def set_difficulty_hard():
	global DIFFICULTY_LEVEL
	DIFFICULTY_LEVEL = 5
	print "Difficulty level is -- {}".format(DIFFICULTY_LEVEL)

def get_hash_id(string):
		return int(HL.md5(string).hexdigest(),16)

def get_random(inputList):
	return (random.choice(inputList))

def get_random_no_dups(inputList,firstLetters):
	if len(inputList) == len(firstLetters):
		return False
	
	filtered = filter(lambda x: x[0] not in firstLetters,inputList)
	if len(filtered) == 0:
		return False
	else:
		return random.choice(filtered)
