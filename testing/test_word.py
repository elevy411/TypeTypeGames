import sys
from word import Word
from letter import Letter
import pygame
import Globals as G

testword = Word([], text="TypeType is tight!")
letter_a = Letter('a')
letter_b = Letter('b')
letter_c = Letter('c')
font = pygame.font.Font(None, 30)

#Test for set and get label
def test_set_and_get_label():
	#2 phrases
	surf = font.render("TypeType is tight!", 1, G.WHITE)
	surf2 = font.render("TypeType is not tight.", 1, G.WHITE)

	#Set the label
	testword.set_label()

	#Convert to bytes
	test_surf = surf.get_buffer().raw 
	test_surf2 = surf2.get_buffer().raw
	test_word = testword.get_label().get_buffer().raw 

	#Check assert statements
	assert (test_surf == test_word), "The phrase is false"
	assert (test_surf2 != test_word), "This should not be the phrase"
	#assert (surf2 == testword.get_label()), "The phrase is wrong"
	
#Test to add, remove, and clear a letter from the letters list in the word
def test_add_remove_clear_letter():
	#Rendered Letter 'a' and 'b'
	rendered_letter_a = font.render('a', 1, G.WHITE)
	rendered_letter_b = font.render('b', 1, G.WHITE)

	#Add the letter 'a' into the word
	added_letter = testword.add_letter(letter_a)
	added_letter_2 = testword.add_letter(letter_b)
	#Byte version of rendered Letter 'a' and 'b'
	byte_test_a = rendered_letter_a.get_buffer().raw
	byte_test_b = rendered_letter_b.get_buffer().raw

	#Convert the letter in the word to bytes
	test_letter_in_word = testword.letters[0].get_label().get_buffer().raw
	test_letter2_in_word = testword.letters[1].get_label().get_buffer().raw

	#CHECK IF THE LETTER WAS TRULY ADDED IN THE CORRECT DIRECTION (----->)
	assert (test_letter_in_word == byte_test_a), "The letter is wrong"
	assert (test_letter2_in_word == byte_test_b), "The letter is wrong"
	assert (test_letter_in_word != byte_test_b), "This should not be the letter"
	assert (test_letter2_in_word != byte_test_a), "This should not be the letter"

	#Length_of_letters_list
	len_letters = len(testword.letters)

	#Call remove function
	removed_letter = testword.remove_letter()

	#New length after remove is called
	new_len_letters = len(testword.letters)

	#CHECK IF A LETTER WAS REMOVED OR NOT
	assert (new_len_letters < len_letters), "The letter is not removed"

	#Add back letters b and c
	testword.add_letter(letter_b)
	testword.add_letter(letter_c)

	#New length should be 3
	len_after_bc = len(testword.letters)
	assert(len_after_bc == 3), "The two letters were not added"

	#CLEAR ALL THE LETTERS
	clear_letter = testword.clear()

	#Length of testword AFTER clearing letters
	zero_letters = len(testword.letters)

	#CHECK IF THE LETTERS WERE CLEARED
	assert (zero_letters == 0), "The letters are not cleared"

#Test to see if the word updated
def test_update():
	#To implement
	return None



test_set_and_get_label()	
test_add_remove_clear_letter()