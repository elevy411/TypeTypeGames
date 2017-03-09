import monster

#Checks to see if the monster has retrieved the head letter
def test_getHead(test_monster):
	test_word = test_monster.word.letters[0]
	monster_head = test_monster.getHead()
	assert (monster_head == test_word), "The letter should be" + test_word.letters[0]

def test_updateWord(test_monster):
	test_word = test_monster.word
	save_word = test_word.letters[1:len(test_word)]
	test_word.updateWord()
	assert (save_word == test_word.letters),  "Word was not updated for" + str(test_word.letters)

#Given a list of monsters, checks to see if successfully attache a monster to a list of monsters
def test_attach(test_fieldmonsters, test_monster):
	check_attach = test_fieldmonsters.attach(test_monster)


#Given a monster, will check to see if a letter has been detached from the word that is associated with the monster
def test_detach(test_monster):
	new_monster = test_monster.detach()



#Checks status of notification to see if letter notification was truly sent or not
def test_notify(test_monster):
	monster_notify = test_monster.notify()
	assert (monster_notify == True), "The notification should be true"


#Given a list of monsters, adds an additional monster with a random word to the list of monsters
def test_addRandomWord(test_fieldmonsters, test_word):
	check_wordAdded = test_fieldmonsters.addRandomWord(test_word)
	assert (check_wordAdded != None), "The word was not successfully added"

def test_tryLetter(letter, fm):
	x = fm.get_field()[0]
	fm.tryLetter(letter)
	assert (fm.get_field()[0] == fm.get_field[1:]), "Try Letter failed"

def test_get_field(fm):
	assert (type(fm.get_field()) != type([])), "Could not get field"

def test_resetChosen(fm):
	fm.resetChosen()
	assert (fm.chosen == []), "Reset chosen failed"

def test_delete(fm, monster):
	fm.delete(monster)
	for i in fm.get_field():
		if i == monster:
			print "Delete failed"
			return False
