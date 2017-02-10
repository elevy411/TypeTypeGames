import Globals
import sys
import pygame

def test_make_word_list():
    test_list = Globals.make_word_list()
    expected_list = ["What","Hello","Amazing","Cool","Project",
        "Super","Awesome","Bingo","Damn","Flavorful"]
    assert len(test_list) == len(expected_list),"output list is not same length as expected list"
    for i in range(len(test_list)):
        assert test_list[i] == expected_list[i],"indices do not match"
        assert Globals.WORDLIST[i] == expected_list[i],"global indices do not match"
    print "no errors in make_word_list"

if __name__ == "__main__":
    test_make_word_list()
