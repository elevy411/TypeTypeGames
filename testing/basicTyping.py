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
    startOver = True
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
    topCenter = G.TOP_CENTER
    topLeft = (topCenter[0]-200,topCenter[1]-50)
    topRight = (topCenter[0]+200,topCenter[1]-50)
    
    centerX = screenCenter[0]
    centerY = screenCenter[1]

    def draw_list(thingsToDraw):
        for (label,(x,y)) in thingsToDraw:
            G.draw(gm,label,(x,y))

    thingsToDraw = []
    lastLetter = None
    xDifferentials = []
    
    P.time.set_timer(P.USEREVENT, 1000) # timer set for each second
    difficulty_setting = G.DIFFICULTY_LEVEL
    
    if difficulty_setting == 1:
        timeCount = 60
        timeText = "1:00"
    elif difficulty_setting == 2:
        timeCount = 30
        timeText = "0:30"
    else:
        timeCount = 15
        timeText = "0:15"

    score = G.SCORE

    gm.screen.fill(BG_COLOR) # set initial background
    thingsToDraw.append((currentWordLabel,topCenter))
    thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))
    thingsToDraw.append((Word.create_word('Score: {}'.format(score)).get_label(),topLeft))
    #G.draw(gm, currentWordLabel, topCenter) # draw first word
    draw_list(thingsToDraw)
    P.display.flip()
    while loop:
        
        currentWordToType = wordList[nextWord]
        currentWordLabel = currentWordToType.get_label()
        thingsToDraw[0] = (currentWordLabel,topCenter)
        
        for e in P.event.get():
            gm.screen.fill(BG_COLOR)
            if e.type == P.QUIT:
                # exit the loop if input is quit
                loop = False
                startOver = False
                break
            if e.type == P.USEREVENT:
                timeCount -= 1
                if timeCount >= 10:
                    timeText = "0:{}".format(timeCount)
                elif timeCount >= 0:
                    timeText = "0:0{}".format(timeCount)
                else:
                    gm.screen.fill(BG_COLOR)
                    #P.display.update()
                    thingsToDraw = []
                    thingsToDraw.append((Word.create_word('Game Over!').get_label(),screenCenter))
                    thingsToDraw.append((Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100)))
                    thingsToDraw.append((Word.create_word('Your Score was {}'.format(score)).get_label(),(centerX,centerY+100)))
                    draw_list(thingsToDraw)
                    P.display.update()
                    loop = False
                    sleep(0.5)
                    break

                timeWord = Word.create_word(timeText)
                #G.draw(gm,timeWord.get_label(),(topCenter[0]+50,topCenter[1]))
                thingsToDraw[1] = (timeWord.get_label(),topRight)
                draw_list(thingsToDraw)
                #P.display.update()
                P.display.update()

            if e.type == P.KEYDOWN:
                # on keypress
                if e.key in G.SPECIAL_KEYS: 
                    # for special key presses   
                    if e.key == P.K_ESCAPE:
                        # exit loop if escape
                        loop = False
                        startOver = False
                        break
                    if e.key == P.K_RETURN:
                        # clear word typed so far if enter is pressed
                        screenWord.clear()
                        #label = screenWord.get_label()
                        #G.draw(gm, currentWordLabel, topCenter)
                        currentLetterCount = 0
                        xDifferentials = []
                        thingsToDraw = thingsToDraw[0:3]
                        draw_list(thingsToDraw)
                        P.display.update()
                        #P.display.update()
                    if e.key == P.K_BACKSPACE:
                        # remove letter from the word being typed if backspace
                        #if currentLetterCount <= 0:
                         #   currentLetter = 0 
                        score -= 10
                        thingsToDraw[2] = (Word.create_word('Score: {}'.format(score)).get_label(),topLeft)
                        screenWord.remove_letter()
                        #label = screenWord.get_label()
                        #G.draw(gm, currentWordToType.get_label(), topCenter)
                        offsetCenter = centerX + ((letterWidth * (screenWord.length - 1)) / 2)
                        if xDifferentials != []:
                            xDifferentials = xDifferentials[:-1]
                            if xDifferentials != []:
                                letterWidth = xDifferentials[len(xDifferentials)-1]
                            else:
                                letterWidth = 0
                            xDifferentials = map(lambda x: x - letterWidth, xDifferentials)
                            
                            thingsToDraw = thingsToDraw[0:3]
                            for pos,letter in enumerate(screenWord.get_letters()):
                                #G.draw(gm,letter.get_label(),(offsetCenter-xDifferentials[pos],centerY-25))
                                thingsToDraw.append((letter.get_label(),(offsetCenter-xDifferentials[pos],centerY-25)))
                            
                            draw_list(thingsToDraw)
                            P.display.update()
                        else:
                            thingsToDraw = thingsToDraw[0:3]
                            for pos,letter in enumerate(screenWord.get_letters()):
                                #G.draw(gm,letter.get_label(),(screenCenter-xDifferentials[pos],centerY-25))
                                thingsToDraw.append((letter.get_label(),(screenCenter-xDifferentials[pos],centerY-25)))
                                draw_list(thingsToDraw)
                                P.display.update()
       
                        currentLetterCount -= 1
                        if currentLetterCount < 0:
                            currentLetterCount = 0
                        #P.display.update()
                    # if e.key == P.K_SPACE:
                    #     screenWord.add_letter(Letter(' '))
                    #     currentLetter = screenWord.get_letters()[currentLetterCount]
                        
                    #     letterWidth = currentLetter.get_width()
                    #     xDifferentials = map(lambda x: x + letterWidth,xDifferentials)
                    #     currentLetterCount += 1
                    #     xDifferentials.append(0)
                        

                    #     if (screenWord.equals(currentWordToType)):
                    #         nextWord += 1
                    #         currentLetterCount = 0
                    #         letterWidth = 0
                    #         xDifferentials = []
                    #         screenWord.clear()
                    #         if nextWord == len(wordList):
                    #             G.draw(gm,Word.create_word('You Win!').get_label(),screenCenter)
                    #             G.draw(gm,Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100))
                    #             P.display.update()
                    #             loop = False
                    #             break

                    #     offsetCenter = centerX + ((letterWidth * (screenWord.length - 1)) / 2)
                        
                    #     thingsToDraw = thingsToDraw[0:3]
                    #     for pos,letter in enumerate(screenWord.get_letters()):
                            
                    #         thingsToDraw.append((letter.get_label(),(offsetCenter - xDifferentials[pos],centerY-25)))
                    #     thingsToDraw[0] = (wordList[nextWord].get_label(),topCenter)
                    #     draw_list(thingsToDraw)
                    #     P.display.update()
                    else:    
                        pass
                elif e.key in range(0,255):
                    if currentLetterCount == len(currentWordToType.get_text()):
                        screenWord.clear()
                        xDifferentials = []
                        nextWord += 1
                        currentLetterCount = 0
                        letterWidth = 0
                        thingsToDraw = thingsToDraw[0:3]
                        draw_list(thingsToDraw)
                        P.display.update()
                    else:
                        keyName = P.key.name(e.key)
                        if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098): #checks for left shift and right shift
                            keyName = keyName.upper()
                        
                        if currentLetterCount < currentWordToType.length and \
                           keyName == wordList[nextWord].get_text()[currentLetterCount]:
                            LETTER_COLOR = G.GREEN
                            score += 10
                            thingsToDraw[2] = (Word.create_word('Score: {}'.format(score)).get_label(),topLeft)
                        else:
                            LETTER_COLOR = G.RED
                            score -= 10
                            thingsToDraw[2] = (Word.create_word('Score: {}'.format(score)).get_label(),topLeft)

                        screenWord.add_letter( Letter(keyName,LETTER_COLOR) )
                        currentLetter = screenWord.get_letters()[currentLetterCount]

                        letterWidth = currentLetter.get_width()
                        xDifferentials = map(lambda x: x + letterWidth,xDifferentials)
                        currentLetterCount += 1
                        xDifferentials.append(0)

                        if (screenWord.equals(currentWordToType)):
                            score += 30
                            thingsToDraw[2] = (Word.create_word('Score: {}'.format(score)).get_label(),topLeft)
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
                            
                        thingsToDraw = thingsToDraw[0:3]
                        for pos,letter in enumerate(screenWord.get_letters()):
                            #G.draw(gm,letter.get_label(),(offsetCenter - xDifferentials[pos],centerY-25))
                            thingsToDraw.append((letter.get_label(),(offsetCenter - xDifferentials[pos],centerY-25)))
                        #G.draw(gm,wordList[nextWord].get_label(),topCenter)
                        thingsToDraw[0] = (wordList[nextWord].get_label(),topCenter)
                        draw_list(thingsToDraw)
                        P.display.update()

    while(startOver):
        sleep(0.5)
        for e in P.event.get():
            if e.type == P.QUIT:
                # exit the loop if input is quit
                startOver = False
            if e.type == P.KEYDOWN:
                startOver = False