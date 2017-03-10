import monster
import Globals as G
from word import Word

#Checks to see if the monster has retrieved the head letter
def test_getHead(test_monster):
	test_word = test_monster.word.letters[0]
	monster_head = test_monster.getHead()
	assert (monster_head == test_word.letter), "The letter should be" + test_word.letters[0].letter

def test_updateWord(test_monster):
	save_word = test_monster.word.letters[1:len(test_monster.word.letters)]
	test_monster.updateWord()
	assert (save_word == test_monster.word.letters),  "Word was not updated for" + str(test_monster.letters)

def test_tryLetter(letter, fm):
	assert (fm.tryLetter(letter)), "Try Letter failed"

def test_resetChosen(fm):
	fm.resetChosen()
	assert (fm.chosen == []), "Reset chosen failed"

def test_delete(fm, monster):
	fm.delete(monster)
	for i in fm.get_field():
		if i == monster:
			print "Delete failed"
			return False

words = G.make_word_list()
wordList = map(lambda listword: Word.create_word(listword),words)

fm = monster.FieldMonsters(wordList, 4)
test_getHead(fm.get_field()[0])
test_updateWord(fm.get_field()[0])
test_tryLetter(fm.get_field()[0].word.text[0], fm)
test_resetChosen(fm)
if len(fm.get_field()) > 0:
	test_delete(fm, fm.get_field()[0])
print "Test Monster Passed."
