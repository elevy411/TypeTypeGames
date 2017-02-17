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
    screen = P.display.set_mode(G.DEF_DIMENSIONS, 0, 32)

    menu_items = ("EASY","MEDIUM","HARD","Back","Quit")

    funcs = {  "Quit" : sys.exit,
             "MEDIUM" : G.set_difficulty_medium,
               "HARD" : G.set_difficulty_hard,
               "Back" : Settings,
               "EASY" : G.set_difficulty_easy}
    
    P.display.set_caption("Difficulty")
    
    gm = GameMenu(screen,menu_items,funcs,True,"SET DIFFICULTY")
    gm.run()

def Settings():
    

    screen = P.display.set_mode(G.DEF_DIMENSIONS, 0, 32)

    menu_items = ("Set Difficulty","Back to Main Menu","Quit")

    funcs = {  "Set Difficulty" : Difficulty,
            "Back to Main Menu" : Main,
                          "Quit": sys.exit,  
            }
    
    P.display.set_caption("Settings")
    
    gm = GameMenu(screen,menu_items,funcs,True,"SETTINGS")
    gm.run()

def Main():
    # Creating the screen
    screen = P.display.set_mode(G.DEF_DIMENSIONS, 0, 32)
    
    #menu_items = ("Start","Quit")
    menu_items = ("Start","Settings","Quit")
    
    funcs = {     "Start": BT.typing,
              "Settings" : Settings,
                   "Quit": sys.exit
    }
 
    P.display.set_caption("Game Menu")
    gm = GameMenu(screen, menu_items, funcs, True, "TYPE TYPE GAMES")
    gm.run()

if __name__ == "__main__":
    Main()