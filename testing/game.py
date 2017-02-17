from time import sleep
import sys
import pygame as P
from word import Word
from letter import Letter
#from TypeTest import TypeTest
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu
import basicTyping as BT


def Difficulty():
    print 'hello'

def Settings():
    

    screen = P.display.set_mode(G.DEF_DIMENSIONS, 0, 32)

    menu_items = ("Set Difficulty","Back to Main Menu","Quit")

    funcs = {"Set Difficulty" : Difficulty,
            "Back to Main Menu" : Main,
            "Quit" : sys.exit}
    
    P.display.set_caption("Settings")
    
    gm = GameMenu(screen,funcs.keys(),funcs,True,"SETTINGS")
    gm.run()

def Main():
    # Creating the screen
    screen = P.display.set_mode(G.DEF_DIMENSIONS, 0, 32)
    
    #menu_items = ("Start","Quit")
    menu_items = ("Start","Settings","Quit")
    funcs = {"Start": BT.typing,
             "Quit": sys.exit,
             "Settings" : Settings
            }
 
    P.display.set_caption("Game Menu")
    gm = GameMenu(screen, funcs.keys(), funcs, True, "TYPE TYPE GAMES")
    gm.run()

if __name__ == "__main__":
    Main()