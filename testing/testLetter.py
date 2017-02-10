import sys
from word import Word
from letter import Letter
import pygame
import Globals as G

test_letter = Letter('a', G.WHITE, font, 30, (20, 20)) #Letter constuctor based on pygame Font which takes in (text,color,font,size,(posx,posy))
font = pygame.font.Font(None, 30)


def test_set_get_letter():
	assert (test_letter.get_letter() == 'a')

	test_letter.set_letter('B')

	assert (test_letter.get_letter() == 'B')

	test_letter.set_letter('a')

def test_set_get_label():
	letter1 = font.render('a', 1, G.RED)
	letter2 = font.render('a', 1, G.WHITE)

	# test with changing the render color when setting label
	# used to be white, but now it's red
	test_letter1.set_label(G.RED)

	letter1_buffer = letter1.get_buffer.raw
	letter2_buffer = letter2.get_buffer.raw
	test_letter_buffer = test_letter.get_label().get_buffer.raw

	assert (letter1_buffer == test_letter_buffer)
	assert (letter2_buffer != test_letter_buffer)

def test_set_position():
	assert (test_letter.pos_x == 20 and test_letter.pos_y == 20)

	test_letter.set_position(0, 10)

	assert (test_letter.pos_x == 0 and test_letter.pos_y == 10)

def test_font_color():
	assert (test_letter.font_color == G.WHITE)

	test_letter.set_font_color("#404040")

	assert (test_letter.font_color == pygame.Color("#404040"))

def test_equals():
	letter1 = Letter('a', G.RED, font, 20, (50, 50))
	letter2 = Letter('b', G.WHITE, font, 30, (20, 20))

	assert (test_letter.equals(letter1))
	assert (test_letter.equals(letter2) == False)
	


