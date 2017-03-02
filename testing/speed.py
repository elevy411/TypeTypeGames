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

'''
Michelle Things To do:

- We need to have function that keeps track of a words index in list of things to draw
ie: We have the Word "Test" but we need to actually put
["T", "E", "S", "T"] in the array if we want to do coloring of the letters as we type.

Im thinking this might be doable with a second array for the letters? The first array will
have the Word objects and then a tuple containing the indicies of the letters they contain and length? 
So like if i have the 3 words "Test", "Hello" and "Bye" then we would have 
			---- [(Test,(0,3),4), (Hello,(4,8),5), (Bye, (9,11),3)]
			-----[T,E,S,T,H,E,L,L,O,B,Y,E]

When a word gets type correctly, we can call a remove_word function that will find the word from the main list, decrement all future indicies
by length, and then delete from the, we then delete those indicies from the LetterArray.



Another idea is to have a sub-draw function that will allows us to draw the letters individually from a word given a screen location for center,
it will just go through the word and draw each letter. This seems like a much easier way to do it. We could probably just make the change in Word.py to
have a letterDraw function. It would grab the labels of all the letters in the word, and then loop over them to render in the location we feed it and with
an array of colors for the letters. This is prob the route I would take.   

- Make a function that will make sure that words generated on screen don't have the same opening 
letter. This will allow for us to have words falling on screen, and only one word is typable
at any time given a starting letter. 

	(Im thinking a while loop on a produce random funciton that takes in a list of bad letters)

- Clean up stuff is last thing.     
'''
def testingSpeed():
	mainLoop = True
	screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
	gm = GameMenu(screen,[],G.SKY_BLUE)
	words = G.make_word_list('speedWords.txt')
	wordList = map(lambda listword: Word.create_word(listword),words)

	##thingsToDO
	##spawn a word every x milliseconds (function of difficulty)
	##set spawn position to different lanes (start with 3)
	##call an update function that will print screen
	##will also move every word on screen down
	clock = P.time.Clock()
	P.time.set_timer(P.USEREVENT, 16)
	centerX = G.SCREEN_CENTER[0]
	centerY = G.TOP_CENTER[1]
	topY = 0
	lanes = [centerX-200,centerX-100,centerX,centerX+100,centerX+200]
	testWord = Word.create_word("test").get_label()
	thingsToDraw = []
	# for x in lanes:
	# 	thingsToDraw.append((testWord,(x,centerY)))
	milliCounter = 0 
	def drawList(thingsToDraw):
		for (label,(x,y)) in thingsToDraw:
			G.draw(gm,label,(x,y))

	def moveDown(things):
		newList = []
		for i in range(len(things)):
			#print things[i]
			newList.append((things[i][0],(things[i][1][0],things[i][1][1]+0.25*G.DIFFICULTY_LEVEL)))
			#print things[i][1]
		return newList
	
	def checkDrawList(things): #checks for the word crossing bottom boundary (decrease score etc)
		for (label,(x,y)) in things:
			if y > G.D_HEIGHT:
				#print 'deleted'
				return thingsToDraw[1:] # removes the word from the screen
		return thingsToDraw

	gm.screen.fill(G.BLACK)
	P.display.flip()
	while(mainLoop):
		for e in P.event.get():
			gm.screen.fill(G.BLACK)
			if e.type == P.QUIT:
				mainLoop = False
				break
			
			if e.type == P.USEREVENT:
				milliCounter += 1
				if milliCounter % (300/G.DIFFICULTY_LEVEL) == 0:
					thingsToDraw.append((G.getRandom(wordList).get_label(),(G.getRandom(lanes),topY)))
				thingsToDraw = moveDown(thingsToDraw)
				thingsToDraw = checkDrawList(thingsToDraw)
				drawList(thingsToDraw)
				P.display.update()

			if e.type == P.KEYDOWN:
				if e.key == P.K_ESCAPE:
					mainLoop = False
					break
				else:
					pass
		drawList(thingsToDraw)
		P.display.update()