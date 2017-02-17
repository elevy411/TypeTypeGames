from time import sleep
import sys
import pygame as P
from word import Word
from letter import Letter
#from TypeTest import TypeTest
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu

P.init()
 
def typing():
    loop = True
    screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
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
    screenCenter = G.SCREEN_CENTER

    centerX = screenCenter[0]
    centerY = screenCenter[1]
    lastLetter = None
    xDifferentials = []

    topCenter = G.TOP_CENTER

    gm.screen.fill(BG_COLOR) # set initial background
    G.draw(gm, currentWordLabel, topCenter) # draw first word
    P.display.flip()
    while loop:
        currentWordToType = wordList[nextWord]
        currentWordLabel = currentWordToType.get_label()
        for e in P.event.get():
            gm.screen.fill(BG_COLOR)
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
                        #label = screenWord.get_label()
                        G.draw(gm, currentWordLabel, topCenter)
                        currentLetterCount = 0
                        xDifferentials = []
                        P.display.update()
                    if e.key == P.K_BACKSPACE:
                        # remove letter from the word being typed if backspace
                        #if currentLetterCount <= 0:
                         #   currentLetter = 0 
                        screenWord.remove_letter()
                        #label = screenWord.get_label()
                        G.draw(gm, currentWordToType.get_label(), topCenter)
                        offsetCenter = centerX + ((letterWidth * (screenWord.length - 1)) / 2)
                        if xDifferentials != []:
                            xDifferentials = xDifferentials[:-1]
                            if xDifferentials != []:
                                letterWidth = xDifferentials[len(xDifferentials)-1]
                            else:
                                letterWidth = 0
                            xDifferentials = map(lambda x: x - letterWidth, xDifferentials)
                            for pos,letter in enumerate(screenWord.get_letters()):
                                G.draw(gm,letter.get_label(),(offsetCenter-xDifferentials[pos],centerY-25))
                        else:
                            for pos,letter in enumerate(screenWord.get_letters()):
                                G.draw(gm,letter.get_label(),(screenCenter-xDifferentials[pos],centerY-25))
                        currentLetterCount -= 1
                        if currentLetterCount < 0:
                            currentLetterCount = 0
                        P.display.update()
                    if e.key == P.K_SPACE:
                        screenWord.add_letter(Letter(' '))
                        currentLetter = screenWord.get_letters()[currentLetterCount]
                        
                        letterWidth = currentLetter.get_width()
                        xDifferentials = map(lambda x: x + letterWidth,xDifferentials)
                        currentLetterCount += 1
                        xDifferentials.append(0)
                        

                        if (screenWord.equals(currentWordToType)):
                            nextWord += 1
                            currentLetterCount = 0
                            letterWidth = 0
                            xDifferentials = []
                            screenWord.clear()
                            if nextWord == len(wordList):
                                G.draw(gm,Word.create_word('You Win!').get_label(),screenCenter)
                                G.draw(gm,Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100))
                                P.display.update()
                                loop = False
                                break

                        offsetCenter = centerX + ((letterWidth * (screenWord.length - 1)) / 2)
                        for pos,letter in enumerate(screenWord.get_letters()):
                            G.draw(gm,letter.get_label(),(offsetCenter - xDifferentials[pos],centerY-25))
                        G.draw(gm,wordList[nextWord].get_label(),topCenter)
                        P.display.update()
                    else:    
                        pass
                elif e.key in range(0,255):
                    if currentLetterCount == len(currentWordToType.get_text()):
                        pass
                    else:
                        keyName = P.key.name(e.key)
                        if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098): #checks for left shift and right shift
                            keyName = keyName.upper()
                        
                        if currentLetterCount < currentWordToType.length and \
                           keyName == wordList[nextWord].get_text()[currentLetterCount]:
                            LETTER_COLOR = G.GREEN
                        else:
                            LETTER_COLOR = G.RED

                        screenWord.add_letter( Letter(keyName,LETTER_COLOR) )
                        currentLetter = screenWord.get_letters()[currentLetterCount]

                        letterWidth = currentLetter.get_width()
                        xDifferentials = map(lambda x: x + letterWidth,xDifferentials)
                        currentLetterCount += 1
                        xDifferentials.append(0)

                        if (screenWord.equals(currentWordToType)):
                            nextWord += 1
                            currentLetterCount = 0
                            letterWidth = 0
                            xDifferentials = []
                            screenWord.clear()
                            if nextWord == len(wordList):
                                G.draw(gm,Word.create_word('You Win!').get_label(),screenCenter)
                                G.draw(gm,Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100))
                                P.display.update()
                                loop = False
                                break

                        offsetCenter = centerX + ((letterWidth * (screenWord.length - 1)) / 2)

                        for pos,letter in enumerate(screenWord.get_letters()):
                            G.draw(gm,letter.get_label(),(offsetCenter - xDifferentials[pos],centerY-25))
                        
                        G.draw(gm,wordList[nextWord].get_label(),topCenter)
                        P.display.update()

    startOver = True
    while(startOver):
        for e in P.event.get():
            if e.type == P.QUIT:
                # exit the loop if input is quit
                startOver = False
            if e.type == P.KEYDOWN:
                startOver = False