import sys
import pygame
from word import Word
from letter import Letter
import Globals as G
import menuItem

def test_constructor():
    test_item = menuItem.MenuItem("testing!")
    assert test_item.text == "testing!","text not set properly"
    assert test_item.pos_x == 0,"pos_x not set properly"
    assert test_item.pos_y == 0,"pos_y not set properly"
    assert test_item.font_color == (255,255,255),"color not set properly"
    assert test_item.font_size == 30, "font size not initialized properly"
    return test_item


def test_set_position(test_item):
    test_item.set_position(1,2)
    assert test_item.pos_x == 1, "set_position fails on x"
    assert test_item.pos_y == 2, "set_position fails on y"
    assert test_item.position == (1,2), "set_position failed to set tuple position"

def test_set_font_color(test_item):
    test_item.set_font_color(G.GREEN)
    assert test_item.font_color == (0,255,0),"set_font_color fails"
    test_item.set_font_color((0,100,200))
    assert test_item.font_color == (0,100,200),"set_font_color fails"

    
def test_get_set_text(test_item):
    assert test_item.get_text() == "testing!","get_text fails"
    test_item.set_text("bonkers dude!")
    assert test_item.text == "bonkers dude!","set_text fails"
    assert test_item.get_text() == "bonkers dude!","get_text fails"


if __name__ == "__main__":
    test_item = test_constructor()
    test_set_position(test_item)
    test_set_font_color(test_item)
    test_get_set_text(test_item)

