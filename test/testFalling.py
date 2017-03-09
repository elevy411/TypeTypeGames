
import game
import Globals as G
import Word 
import Letter
import TypeTypeFalling as T


test_word = Word.create_word("TestWord")
test_word.set_position(G.TOP_CENTER[0],G.TOP_CENTER[1])

def test_word_fall(word):
	# get the position of the word created
	x, y = word.get_position()

	# lower the word by 15 pixels
	word.fall(15)

	# verify that the word has dropped 15 pixels

	x2, y2 = word.get_position()

	# verify that the x coordinates stay the same
	# and that the y coordinate has dropped 15 pixels

	assert x == x, "x value changes during word drop"
	assert y == y2 - 15, "y value incorrect during word drop"
	print "word falling test passes"


def test_level_up():
	# get the current speed at which words will drop from the top
	current_speed = T.get_speed()
	current_level = T.get_level()

	#call level_up on the game and expect the speed to increase
	T.level_up()

	updated_speed = T.get_speed()
	updated_level = T.get_level()

	assert current_speed < updated_speed, "speed does not increase with level up"
	assert current_level + 1 == updated_level, "level not incremented"
	print "speed change test passes"


def test_decrement_score():
	# get current score of the game
	current_score = T.get_score()

	# create a test word and add it to the game
	test_word = Word.create_word("TestWord")
	test_word.set_position(G.TOP_CENTER[0],G.TOP_CENTER[1])
	T.add_word(test_word)

	# move the word past the bottom of the play screen
	test_word.fall(3000)

	# ensure that the score has dropped by 1
	assert T.get_score() == curren_score - 1, "Score incorrect after word drop"
	print "Decrement score test passed"


def test_increment_score():
	# get current score of the game
	current_score = T.get_score()

	# call T.score_add(1), which will be called when a word is completed
	T.score_add(1)


	# ensure that the score has been incremented by 1
	assert T.get_score() == curren_score + 1, "Score incorrect after word completion"
	print "Increment score test passed"

