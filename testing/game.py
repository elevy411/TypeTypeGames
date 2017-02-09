
import sys
import pygame as P
from word import Word
from letter import Letter
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu

P.init()
 
def typing():
    loop = True
    screen = P.display.set_mode((640,480),0,32)
    gm = GameMenu(screen,[],G.BLACK)   
    screenWord = Word([])
    words = G.make_word_list()
    wordList = map(lambda listword: Word.create_word(listword),words)
    nextWord = 0
    P.key.set_repeat(500,50) #so people can hold a key down
    BG_COLOR = G.BLACK
    screenCenter = (gm.get_width()/2,gm.get_height()/2)
    topCenter = (gm.get_width()/2,gm.get_height()/4)
    gm.screen.fill(BG_COLOR) # set initial background
    draw(gm,wordList[nextWord].get_label(),topCenter) # draw first word
    P.display.flip()
    while loop:
        for e in P.event.get():
            gm.screen.fill(BG_COLOR)
            draw(gm,wordList[nextWord].get_label(),topCenter)
            if e.type == P.QUIT:
                loop = False
            if e.type == P.KEYDOWN:
                if e.key in G.SPECIAL_KEYS:    
                    if e.key == P.K_ESCAPE:
                        loop = False
                        break
                    if e.key == P.K_RETURN:
                        screenWord.clear()
                        label = screenWord.get_label()
                        draw(gm,label,screenCenter)
                        P.display.flip()
                    if e.key == P.K_BACKSPACE:
                        screenWord.remove_letter()
                        label = screenWord.get_label()
                        draw(gm,label,screenCenter)
                        P.display.flip()
                    # if e.key == P.K_SPACE:
                    #     screenWord.add_letter(Letter(' '))
                    #     label = screenWord.get_label()
                    #     draw(gm,label,screenCenter)
                    #     P.display.flip()
                    else:    
                        pass
                elif e.key in range(0,255):
                    if P.key.get_mods() in (4097,4098): #checks for left shift and right shift
                        screenWord.add_letter( Letter(P.key.name(e.key).upper()) )
                    else:
                        screenWord.add_letter( Letter(P.key.name(e.key)) )
                    
                    label = screenWord.get_label()
                    draw(gm,label,screenCenter)                    
                    P.display.flip()

def draw(gm,label,center):
    label_rect = label.get_rect(center=center)
    gm.screen.blit(label,label_rect)

if __name__ == "__main__":
 
    # Creating the screen
    screen = P.display.set_mode((640, 480), 0, 32)
 
    menu_items = ('Start', 'Quit')
    funcs = {'Start': typing,
             'Quit': sys.exit}
 
    P.display.set_caption('Game Menu')
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()