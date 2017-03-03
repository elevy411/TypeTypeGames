import Globals
import sys
import pygame


##Globals will simply be a file with some useful functions like creating the master wordlist to use

def test_make_word_list():
    test_list = Globals.make_word_list() #if wordList.txt is equal to this list
    expected_list = ["What","Hello","Amazing","Cool","Project",
        "Super","Awesome","Bingo","Damn","Flavorful"]
    assert len(test_list) == len(expected_list),"output list is not same length as expected list"
    for i in range(len(test_list)):
        assert test_list[i] == expected_list[i],"returned list indices do not match"
        assert Globals.WORDLIST[i] == expected_list[i],"global list indices do not match"
    print "no errors in make_word_list"


#This was added recently because of the addition of the global function
def test_set_difficulty():
	Globals.set_difficulty_medium()
	assert (Globals.DIFFICULTY_LEVEL == 2), ("set_difficulty_medium failed")

	Globals.set_difficulty_hard()
	assert (Globals.DIFFICULTY_LEVEL == 3), ("set_difficulty_hard failed")

	Globals.set_difficulty_easy()
	assert (Globals.DIFFICULTY_LEVEL == 1), ("set_difficulty_easy failed")


if __name__ == "__main__":
    test_make_word_list()
    test_set_difficulty()
