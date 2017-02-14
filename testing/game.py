
import sys
import pygame as P
from word import Word
from letter import Letter
from TypeTest import TypeTest
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
    currentWordToType = wordList[nextWord]
    currentWordLabel = currentWordToType.get_label()
    currentLetterCount = 0
    letterWidth = 0
    P.key.set_repeat(500,50) #so people can hold a key down
    BG_COLOR = G.BLACK
    LETTER_COLOR = G.DEF_LETTER_COLOR
    screenCenter = (gm.get_width()/2,gm.get_height()/2)

    centerX = screenCenter[0]
    centerY = screenCenter[1]
    lastLetter = None
    xDifferentials = []

    topCenter = (gm.get_width()/2,gm.get_height()/4)
    gm.screen.fill(BG_COLOR) # set initial background
    draw(gm, currentWordLabel, topCenter) # draw first word
    P.display.flip()
    while loop:
        for e in P.event.get():
            gm.screen.fill(BG_COLOR)
            #draw(gm,wordList[nextWord].get_label(),topCenter)
            if e.type == P.QUIT:
                # exit the loop if input is quit
                loop = False
            if e.type == P.KEYDOWN:
                # on keypress
                if e.key in G.SPECIAL_KEYS: 
                    # for special key presses   
                    if e.key == P.K_ESCAPE:
                        # exit loop if escape
                        loop = False
                        break
                    if e.key == P.K_RETURN:
                        # clear word typed so far if enter is pressed
                        screenWord.clear()
                        label = screenWord.get_label()
                        draw(gm, label, screenCenter)
                        draw(gm, currentWordLabel, topCenter)
                        currentLetterCount = 0
                        xDifferentials = []
                        P.display.update()
                    if e.key == P.K_BACKSPACE:
                        # remove letter from the word being typed if backspace
                        #if currentLetterCount <= 0:
                         #   currentLetter = 0 
                        screenWord.remove_letter()
                        label = screenWord.get_label()
                        draw(gm, label, screenCenter)
                        draw(gm, currentWordLabel, topCenter)
                        offsetCenter = centerX + ((letterWidth * screenWord.length) / 2)
                        if xDifferentials != []:
                            xDifferentials = xDifferentials[:-1]
                            print xDifferentials
                            if xDifferentials != []:
                                letterWidth = xDifferentials[len(xDifferentials)-1]
                            else:
                                letterWidth = 0
                            xDifferentials = map(lambda x: x - letterWidth, xDifferentials)
                            for pos,letter in enumerate(screenWord.get_letters()):
                                draw(gm,letter.get_label(),(offsetCenter-xDifferentials[pos],centerY-25))
                        else:
                            for pos,letter in enumerate(screenWord.get_letters()):
                                draw(gm,letter.get_label(),(screenCenter-xDifferentials[pos],centerY-25))
                        currentLetterCount -= 1
                        if currentLetterCount < 0:
                            currentLetterCount = 0
                        print xDifferentials
                        P.display.update()
                    # if e.key == P.K_SPACE:
                    #     screenWord.add_letter(Letter(' '))
                    #     label = screenWord.get_label()
                    #     draw(gm,label,screenCenter)
                    #     P.display.update()
                    else:    
                        pass
                elif e.key in range(0,255):
                    keyName = P.key.name(e.key)
                    #print P.key.get_mods()
                    if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098): #checks for left shift and right shift
                        keyName = keyName.upper()
                    
                    if currentLetterCount < currentWordToType.length and \
                       keyName == wordList[nextWord].get_text()[currentLetterCount]:
                        LETTER_COLOR = G.GREEN
                    else:
                        LETTER_COLOR = G.RED

                    #draw(gm,Letter(keyName.upper(),LETTER_COLOR).get_label(),screenCenter)
                    screenWord.add_letter( Letter(keyName,LETTER_COLOR) )
                    currentLetter = screenWord.get_letters()[currentLetterCount]

                    #print currentLetter.get_width()
                    letterWidth = currentLetter.get_width()
                    xDifferentials = map(lambda x: x + letterWidth,xDifferentials)
                    print xDifferentials
                    currentLetterCount += 1
                    #print currentLetterCount
                    xDifferentials.append(0)

                    if (screenWord.equals(wordList[nextWord])):
                        nextWord += 1
                        currentLetterCount = 0
                        letterWidth = 0
                        xDifferentials = []
                        screenWord.clear()

                    offsetCenter = centerX + ((letterWidth * screenWord.length) / 2)
                    #print centerX, offsetCenter

                    for pos,letter in enumerate(screenWord.get_letters()):
                        draw(gm,letter.get_label(),(offsetCenter - xDifferentials[pos],centerY-25))
                    
                    #newLabel = Letter(keyName,LETTER_COLOR).get_label()
                    label = screenWord.get_label()
                    draw(gm,label,screenCenter)                    
                    draw(gm,wordList[nextWord].get_label(),topCenter)
                    #draw(gm,newLabel,screenCenter)
                    P.display.update()

                    #print screenWord.metrics(screenWord.get_text())

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