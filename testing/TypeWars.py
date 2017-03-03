from time import sleep
import sys
import pygame as P
from word import Word
from letter import Letter
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu


P.init()

class Player():
    def __init__(self, index=0, counter=0, health=100):
        self.index = index
        self.counter = counter
        self.health = health

    def modifyHealth(self, value):
        if self.health == 0 or value > 0:
            pass
        else:
            value = self.health + value
            if value < 0:
                self.health = 0
            else:
                self.health = value

    def resetHealth(self):
        self.health = 100

    def modifyIndex(self, value):
        if value < 0:
            pass
        else:
            value = self.index + value
            self.index = value

    def resetIndex(self):
        self.index = 0

    def calculateWPM(self):
        time_elapsed = float(self.counter) / 60
        return self.index / time_elapsed

    def updateCounter(self, value):
        self.counter = value


def typing():
    loop = True
    startOver = True
    screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
    gm = GameMenu(screen,[],G.BLACK)   
    screenWord = Word([])
    words = G.make_word_list()  #change to certain list based on difficulty level
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

    player1 = Player()
    player2 = Player()

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

    #score = G.SCORE

    gm.screen.fill(BG_COLOR) # set initial background
    thingsToDraw.append((currentWordLabel,topCenter))
    thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))
    thingsToDraw.append((Word.create_word('Health: {}'.format(player1.health)).get_label(),topLeft))
    thingsToDraw.append((Word.create_word('Player 1').get_label(),(topCenter[0]-200,topCenter[1]-80)))
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
                    thingsToDraw = []
                    thingsToDraw.append((Word.create_word('Round Over!').get_label(),screenCenter))
                    thingsToDraw.append((Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100)))
                    thingsToDraw.append((Word.create_word('Your Health was {}'.format(player1.health)).get_label(),(centerX,centerY+100)))
                    thingsToDraw.append((Word.create_word('You typed {} words'.format(player1.index)).get_label(),(centerX,centerY+150)))
                    draw_list(thingsToDraw)
                    P.display.update()
                    loop = False
                    sleep(0.5)

                timeWord = Word.create_word(timeText)
                thingsToDraw[1] = (timeWord.get_label(),topRight)
                draw_list(thingsToDraw)
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
                        currentLetterCount = 0
                        xDifferentials = []
                        thingsToDraw = thingsToDraw[0:4]
                        draw_list(thingsToDraw)
                        P.display.update()
                    if e.key == P.K_BACKSPACE:
                        # remove letter from the word being typed if backspace
                        #if currentLetterCount <= 0:
                         #   currentLetter = 0 
                        player1.modifyHealth(-2)
                        thingsToDraw[2] = (Word.create_word('Health: {}'.format(player1.health)).get_label(),topLeft)
                        screenWord.remove_letter()
                        #label = screenWord.get_label()
                        offsetCenter = centerX + ((letterWidth * (screenWord.length - 1)) / 2)
                        if xDifferentials != []:
                            xDifferentials = xDifferentials[:-1]
                            if xDifferentials != []:
                                letterWidth = xDifferentials[len(xDifferentials)-1]
                            else:
                                letterWidth = 0
                            xDifferentials = map(lambda x: x - letterWidth, xDifferentials)
                            
                            thingsToDraw = thingsToDraw[0:4]
                            for pos,letter in enumerate(screenWord.get_letters()):
                                thingsToDraw.append((letter.get_label(),(offsetCenter-xDifferentials[pos],centerY-25)))
                            
                            draw_list(thingsToDraw)
                            P.display.update()
                        else:
                            thingsToDraw = thingsToDraw[0:4]
                            for pos,letter in enumerate(screenWord.get_letters()):
                                thingsToDraw.append((letter.get_label(),(screenCenter-xDifferentials[pos],centerY-25)))
                                draw_list(thingsToDraw)
                                P.display.update()
       
                        currentLetterCount -= 1
                        if currentLetterCount < 0:
                            currentLetterCount = 0
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
                        thingsToDraw = thingsToDraw[0:4]
                        draw_list(thingsToDraw)
                        P.display.update()
                    else:
                        keyName = P.key.name(e.key)
                        if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098): #checks for left shift and right shift
                            keyName = keyName.upper()
                        
                        if currentLetterCount < currentWordToType.length and \
                           keyName == wordList[nextWord].get_text()[currentLetterCount]:
                            LETTER_COLOR = G.GREEN
                            thingsToDraw[2] = (Word.create_word('Health: {}'.format(player1.health)).get_label(),topLeft)
                        else:
                            LETTER_COLOR = G.RED
                            player1.modifyHealth(-5)
                            thingsToDraw[2] = (Word.create_word('Health: {}'.format(player1.health)).get_label(),topLeft)

                        screenWord.add_letter( Letter(keyName,LETTER_COLOR) )
                        currentLetter = screenWord.get_letters()[currentLetterCount]

                        letterWidth = currentLetter.get_width()
                        xDifferentials = map(lambda x: x + letterWidth,xDifferentials)
                        currentLetterCount += 1
                        xDifferentials.append(0)

                        if (screenWord.equals(currentWordToType)):
                            player1.modifyIndex(1)
                            thingsToDraw[2] = (Word.create_word('Health: {}'.format(player1.health)).get_label(),topLeft)
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
                            
                        thingsToDraw = thingsToDraw[0:4]
                        for pos,letter in enumerate(screenWord.get_letters()):
                            thingsToDraw.append((letter.get_label(),(offsetCenter - xDifferentials[pos],centerY-25)))
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
