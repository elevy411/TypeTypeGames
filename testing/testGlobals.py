import Globals
import sys
import pygame


##Globals will simply be a file with some useful functions like creating the master wordlist to use

def test_make_word_list():
    test_list = Globals.make_word_list()
    expected_list = ["What","Hello","Amazing","Cool","Project",
        "Super","Awesome","Bingo","Damn","Flavorful"]
    assert len(test_list) == len(expected_list),"output list is not same length as expected list"
    for i in range(len(test_list)):
        assert test_list[i] == expected_list[i],"returned list indices do not match"
        assert Globals.WORDLIST[i] == expected_list[i],"global list indices do not match"
    print "no errors in make_word_list"


def test_set_difficulty():
	Globals.set_difficulty('MEDIUM')
	assert (Globals.DIFFICULTY_LEVEL == 2), ("set_difficulty to MEDIUM failed")

	Globals.set_difficulty('HARD')
	assert (Globals.DIFFICULTY_LEVEL == 3), ("set_difficulty to HARD failed")

	Globals.set_difficulty('EASY')
	assert (Globals.DIFFICULTY_LEVEL == 1), ("set_difficulty to EASY failed")


if __name__ == "__main__":
    test_make_word_list()
    test_set_difficulty()
