import sys
import pygame as P
from word import Word
from letter import Letter
from TypeTest import TypeTest
import Globals as G
from game import Game
from menuItem import MenuItem
from gameMenu import GameMenu



#Checks to see if the monster has retrieved the head letter
def test_getHead(test_monster):
	test_word = test_monster.word.letters[0]
	monster_head = test_monster.getHead()
	assert (monster_head == test_word), "The letter should be" + test_word.letters[0]

def test_updateWord(test_monster):
	test_word = test_monster.word
	save_word = test_word.letters[1:len(test_word)]
	test_word.updateWord()
	assert (save_word[:len(save_word)] == test_word.letters[:len(test_word.letters)]), 
	"Word was not updated for" + str(test_word.letters)


#Given a list of monsters, checks to see if successfully attache a monster to a list of monsters
def test_attach(test_fieldmonsters, test_monster):
	new_length = len(test_fieldmonsters) + 1
	check_attach = test_fieldmonsters.attach(test_monster)
	assert (new_length == len(check_attach)), "The monster did not successfully attach. The length is still %d" % (check_attach)


#Given a monster, will check to see if a letter has been detached from the word that is associated with the monster
def test_detachletter(test_monster):
	updated_num = len(test_monster.word.letters) - 1
	new_monster = test_monster.detach()

	assert (updated_num == len(new_monster.word.letters)), "The letter was not detached. The length of the word is still %d" % (len(new_monster.word.letters))




#Checks status of notification to see if letter notification was truly sent or not
def test_notify(test_monster):
	monster_notify = test_monster.notify()
	assert (monster_notify == True), "The notification should be true"


#FieldMonsters tests...

#Tests to see if a letter that was tried is in fact a valid or invalid letter
def test_tryLetter(test_fieldmonsters, expected_letter):
	test_letter = test_fieldmonsters.tryLetter()
	assert (test_letter == expected_letter), "The letter was not the expected letter" + expected_letter


#Given a list of monsters, checks to see if successfully detached a monster from a list of monsters
def test_detachmonster(test_fieldmonsters):
	new_length = len(test_fieldmonsters) - 1
	check_detach = test_fieldmonsters.detach()
	#Check the very first monster and check the length to check if detached
	#Checking to see if the length of monster_detach is the same
	assert (new_length == len(check_detach)), "The monster did not successfully detach. Current length is still %d" % (check_detach)


#Given a monster_list for a user, checks to see what the cumulative score is
def test_computeScore(test_fieldmonsters, expected_score):
	check_score = test_fieldmonsters.computeScore()
	assert (check_score == expected_score), 
	"The score was incorrect. The input score was %d, but should've been %d" % (check_score, expected_score)


#Given a list of monsters, adds an additional monster with a random word to the list of monsters
def test_addRandomWord(test_fieldmonsters, test_word):
	check_wordAdded = test_fieldmonsters.addRandomWord(test_word)
	assert (check_wordAdded == True), "The word was not successfully added"


#Not sure how you want me to consolidate these/whether we should still keep these or leave these as additional parameters for the monster list (Monsters)
def test_createFM():
def test_destroyFM():


