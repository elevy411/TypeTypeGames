from time import sleep
import sys, os
import pygame as P
from word import Word
from letter import Letter
#from TypeTest import TypeTest
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu
import basicTyping as BT
import speed as SP
import TypeWars as TW
import typeTypeRevolution as TTR
import monster as M
import psutil

openf = []

def Difficulty():

    screen = P.display.set_mode(G.DEF_DIMENSIONS, 0, 32)

    menu_items = ("Set Difficulty - EASY","Set Difficulty - MEDIUM","Set Difficulty - HARD","Back","Quit")

    funcs = {                   "Quit" : sys.exit,
             "Set Difficulty - MEDIUM" : G.set_difficulty_medium,
               "Set Difficulty - HARD" : G.set_difficulty_hard,
                                "Back" : Settings,
               "Set Difficulty - EASY" : G.set_difficulty_easy}

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

def Main(from_sett=True):
    if from_sett:
        G.cleanup(G.openf)
    else:
        p = psutil.Process()
        G.openf = p.open_files()

    # Creating the screen
    screen = P.display.set_mode(G.DEF_DIMENSIONS, 0, 32)

    #menu_items = ("Basic Typing","Quit")
    menu_items = ("Basic Typing","Settings","Falling Words",
                  "TypeWars","Type Type Revolution","Type Vs Monster","Quit")

    funcs = {     "Basic Typing": BT.typing,
              "Settings" : Settings,
             "Falling Words": SP.testingSpeed,
             "TypeWars" : TW.type_war,
             "Type Type Revolution" : TTR.typing,
             "Type Vs Monster" : M.typing,
                   "Quit": sys.exit
    }

    P.display.set_caption("Game Menu")
    gm = GameMenu(screen, menu_items, funcs, True, "TYPE TYPE GAMES")
    gm.run()

if __name__ == "__main__":
    Main(False)
