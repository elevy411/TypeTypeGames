from word import Word
from letter import Letter
import Globals as G
import pygame


def test_word_constructor():
	test_word = Word.create_word('TypeType is tight!')
	assert (str(type(test_word)) == "<class \'word.Word\'>"), "Constructor Failure"
	return test_word

def test_set_position(test_word):
	for x in range(-100, 100):
		for y in range(-100, 100):
			test_word.set_position(x, y)
			assert (test_word.position == (x, y)), ("Set Position failed for " + str(x) + " " + str(y))
			assert (test_word.pos_x == x), ("Set Position failed for " + str(x))
			assert (test_word.pos_y == y), ("Set Position failed for " + str(y))

def test_set_font_color(test_word):
	for x in range(50):
		for y in range(50):
			for z in range(50):
				test_word.set_font_color((x,y,z))
				assert test_word.font_color == (x,y,z)
	try:
		test_word.set_font_color((256, 256, 256))
		assert False, "Set font color accepted errant values."
	except:
		pass

def test_set_and_get_text(test_word):
	test_word.set_text()
	assert test_word.get_text() == 'TypeType is tight!', 'Set and get text failed'

#Test for set and get label
def test_set_and_get_label(test_word, font):
	#2 phrases
	surf = font.render("TypeType is tight!", 1, test_word.font_color)
	surf2 = font.render("TypeType is not tight.", 1, test_word.font_color)

	#Set the label
	test_word.set_label()

	#Convert to bytes
	test_surf = surf.get_buffer().raw
	test_surf2 = surf2.get_buffer().raw
	checker = test_word.get_label().get_buffer().raw

	#Check assert statements
	assert (test_surf != checker), "The phrase is false"
	assert (test_surf2 != checker), "This should not be the phrase"
	#assert (surf2 == test_word.get_label()), "The phrase is wrong"

#Test to add, remove, and clear a letter from the letters list in the word
def test_add_remove_clear_letter(test_word, font, letter_a, letter_b, letter_c):

	#Add the letters into the word
	test_word.add_letter(letter_a)
	test_word.add_letter(letter_b)

	#CHECK IF THE LETTER WAS TRULY ADDED IN THE CORRECT DIRECTION (----->)
	assert (test_word.letters[-2].letter == 'a'), "Add letter failed"
	assert (test_word.letters[-1].letter == 'b'), "Add letter failed"

	#Length_of_letters_list
	len_letters = len(test_word.letters)

	#Call remove function
	removed_letter = test_word.remove_letter()

	#New length after remove is called
	new_len_letters = len(test_word.letters)

	#CHECK IF A LETTER WAS REMOVED OR NOT
	assert (new_len_letters < len_letters), "The letter is not removed"

	#Add back letters b and c
	test_word.add_letter(letter_b)
	test_word.add_letter(letter_c)

	#New length should be 3
	len_after_bc = len(test_word.letters)
	assert(len_after_bc == new_len_letters + 2), "The two letters were not added"

	#CLEAR ALL THE LETTERS
	clear_letter = test_word.clear()

	#Length of test_word AFTER clearing letters
	zero_letters = len(test_word.letters)

	#CHECK IF THE LETTERS WERE CLEARED
	assert (zero_letters == 0), "The letters are not cleared"

def test_equality(test_word):
	temp = Word.create_word("Hello")
	assert temp.equal(Word.create_word("Hello")), "Test equality failed."
	assert not Word.create_word("noooo").equal(temp), "Test equality failed."

#Test to see if the word updated
def test_update(test_word):
	#To implement
	return None

letter_a = Letter('a')
letter_b = Letter('b')
letter_c = Letter('c')
font = pygame.font.Font(None, 30)

test_word = test_word_constructor()
test_set_position(test_word)
test_set_font_color(test_word)
test_set_and_get_text(test_word)
test_set_and_get_label(test_word, font)
test_add_remove_clear_letter(test_word, font, letter_a, letter_b, letter_c)
print "Test Word Passed."
