import game
import Globals as G
import Word 
import Letter
import TypeTypeWars as TW


def test_set_speed():
	# set difficulty level
	G.set_difficulty_easy()

	# set current speed based on difficulty level
	TW.set_speed()

	# get current speed
	current_speed = TW.get_speed()

	#change difficulty level
	G.set_difficulty_hard()

	# update speed
	TW.set_speed()
	updated_speed = TW.get_speed()

	assert (current_speed < updated_speed), "speed didn't increase when difficulty level increased"

	current_speed = TW.get_speed()

	G.set_difficulty_medium()

	TW.set_speed()
	updated_speed = TW.get_speed()

	assert (current_speed > updated_speed), "speed didn't decrease when difficulty level decreased"


def test_add_to_attack():

	# make random word list from larger list; different lists used depending on difficulty level
	word_list = TW.make_word_list_from(G.WORDLIST)

	curr_attack_list = TW.get_attack_list()

	# add words to attack_list
	for i in range(len(word_list)):
		TW.add_to_attack(word_list[i])

	updated_attack_list = TW.get_attack_list()

	assert (len(curr_attack_list) < len(updated_attack_list)), "add_to_attack failed"
	assert (len(updated_attack_list) == (len(curr_attack_list) + len(word_list))), "all words weren't added to attack list"


def test_update_health():

	test_word1 = Word.create_word("Test1")
	test_word2 = Word.create_word("Test2")

	# get initial health of player
	current_health = TW.get_health()

	# decrement health when incorrect word is typed
	TW.update_health(test_word1.equals(test_word2))

	# get updated health
	updated_health = TW.get_health()

	assert (current_health > updated_health), "health didn't decrease with incorrectly typed word"

	current_health = TW.get_health()

	# increment health when correct word is typed
	TW.update_health(test_word2.equals(test_word2))

	updated_health = TW.get_health()

	assert (current_health < updated_health), "health didn't increase with correctly typed word"


def test_reset_attack():

	word_list = TW.make_word_list_from(G.WORDLIST)

	# add words to attack_list
	for i in range(len(word_list)):
		TW.add_to_attack(word_list[i])

	curr_attack_list = TW.get_attack_list()

	assert (len(curr_attack_list) > 0), "add_to_attack failed"

	TW.reset_attack_list()

	curr_attack_list = TW.get_attack_list()

	assert (len(curr_attack_list) == 0), "reset_attack_list failed"
	