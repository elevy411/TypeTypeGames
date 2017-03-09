import sys
from word import Word
from letter import Letter
import pygame
import Globals as G

test_letter = Letter('a', G.WHITE, G.MONOSPACE_FONT, 30, (20, 20)) #Letter constuctor based on pygame Font which takes in (text,color,font,size,(posx,posy))
font = pygame.font.Font(None, 30)

def test_set_get_letter():
	assert (test_letter.get_letter() == 'a')
	test_letter.set_letter('B')
	assert (test_letter.get_letter() == 'B')
	test_letter.set_letter('a')

def test_set_get_label():
	test_letter.set_label(G.WHITE)
	assert (test_letter.label == test_letter.get_label())

def test_set_position():
	assert (test_letter.pos_x == 20 and test_letter.pos_y == 20)

	test_letter.set_position(0, 10)

	assert (test_letter.pos_x == 0 and test_letter.pos_y == 10)

def test_font_color():
	assert (test_letter.font_color == G.WHITE)

	test_letter.set_font_color((1,1,1))

	assert (test_letter.font_color == (1,1,1))

def test_equals():
	letter1 = Letter('a', G.WHITE, G.MONOSPACE_FONT, 20, (50, 50))
	letter2 = Letter('b', G.WHITE, G.MONOSPACE_FONT, 30, (20, 20))

	assert (test_letter.equals(letter1))
	assert (test_letter.equals(letter2) == False)

test_set_get_letter()
test_set_get_label()
test_set_position()
test_font_color()
test_equals()
print "Test Letter Passed."
