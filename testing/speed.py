import hashlib as HL
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
lockedOnWord = ''
currentHash = -1
lockedOn = False
current_letter_idx = 0

def testingSpeed():
	global lockedOn,currentHash,lockedOnWord,current_letter_idx
	mainLoop = True
	screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
	gm = GameMenu(screen,[],G.SKY_BLUE)
	words = G.make_word_list('speedWords.txt')
	#wordList = map(lambda listword: Word.create_word(listword),words)

	##thingsToDO
	##spawn a word every x milliseconds (function of difficulty)
	##set spawn position to different lanes (start with 3)
	##call an update function that will print screen
	##will also move every word on screen down
	clock = P.time.Clock()
	P.key.set_repeat(500,50) #so people can hold a key down
	P.time.set_timer(P.USEREVENT, 16)
	centerX = G.SCREEN_CENTER[0]
	centerY = G.TOP_CENTER[1]
	topY = 0
	lanes = [centerX-200,centerX-100,centerX,centerX+100,centerX+200]
	difficulty = G.DIFFICULTY_LEVEL
	
	# for x in lanes:
	# 	thingsToDraw.append((testWord,(x,centerY)))
	milliCounter = 0 
	def drawList(thingsToDraw):
		for obj in thingsToDraw:
			if type(obj) == tuple:
				letter,(x,y),hashVal = obj
				G.draw(gm,letter.get_label(),(x,y))
			elif type(obj) == list:
				for (letter,(x,y),hashVal) in obj:
					G.draw(gm,letter.get_label(),(x,y))

	def moveDown(things):
		newList = []
		for i in range(len(things)):
			#print things[i]
			obj = things[i]
			if type(obj) == tuple:
				label,(x,y),hashVal = obj
				newList.append((label,(x,y+0.25*difficulty),hashVal))
			elif type(obj) == list:
				tList = []
				for (label,(x,y),hashVal) in obj:
					tList.append((label,(x,y+0.25*difficulty),hashVal))
				newList.append(tList)
		return newList
	
	def checkDrawList(things): #checks for the word crossing bottom boundary (decrease score etc)
		for obj in things:		
			if type(obj) == tuple:
				label,(x,y),hashVal = obj
				if y > G.D_HEIGHT:
					return thingsToDraw[1:] # removes the word from the screen
			if type(obj) == list:
				letter,(x,y),hashVal = obj[0]
				if y > G.D_HEIGHT:
					return thingsToDraw[1:]
		return thingsToDraw

	def findByHash(thingsToDraw,hashID):
		for idx,obj in enumerate(thingsToDraw):
			if type(obj) == tuple:
				label,(x,y),hashVal = obj
				if hashID == hashVal:
					return idx
			if type(obj) == list:
				letter,(x,y),hashVal = obj[0]
				if hashID == hashVal:
					return idx
		return -1

	def removeByHash(wordsOnScreen,hashID):
		badIdx = -1
		for idx,(word,wordHash) in enumerate(wordsOnScreen):
			if wordHash == hashID:
				badIdx = idx
				break
		
		if badIdx == 0:
			return wordsOnScreen[1:]
		else:
			return wordsOnScreen[0:badIdx]+wordsOnScreen[badIdx+1:]
	#returns the hash id of the word based on val, otherwise -1
	def checkFirsts(wordsOnScreen,val): 
		for word,hashID in wordsOnScreen:
			if val == word[0]:
				return (word,hashID)
		return ('',-1)

	def resetVals():
		global lockedOn,currentHash,lockedOnWord,current_letter_idx
		lockedOn = False
		currentHash = -1
		lockedOnWord = ''
		current_letter_idx = 0

	gm.screen.fill(G.BLACK)
	P.display.flip()
	firstLetters = []
	wordsOnScreen = [] #words with hashes
	thingsToDraw = []
	scoreCount = 0
	multiplier = 1
	while(mainLoop):
		for e in P.event.get():
			gm.screen.fill(G.BLACK)
			if e.type == P.QUIT:
				mainLoop = False
				break
			
			if e.type == P.USEREVENT:
				milliCounter += 1
				if milliCounter % (300/round(difficulty)) == 0:
					possibleWord = G.get_random_no_dups(words,firstLetters)
					if possibleWord == False: #no possible words to generate
						break
					newWord = Word.create_word(possibleWord)
					newText = newWord.get_text()
					wordsOnScreen.append((newText,G.get_hash_id(newText)))
					firstLetters.append(newText[0])
					newLetters = newWord.draw_by_letters((G.get_random(lanes),topY))
					thingsToDraw.append(newLetters)
					drawList(thingsToDraw)
					P.display.update()
				#print len(thingsToDraw)
				thingsToDraw = moveDown(thingsToDraw)
				thingsToDraw = checkDrawList(thingsToDraw)
				drawList(thingsToDraw)
				P.display.update()

			if e.type == P.KEYDOWN:
				if e.key in G.SPECIAL_KEYS:	
					if e.key == P.K_ESCAPE:
						mainLoop = False
						break
					elif e.key == P.K_SPACE:
						possibleWord = G.get_random_no_dups(words,firstLetters)
						if possibleWord == False: #no possible words to generate
							break
						newWord = Word.create_word(possibleWord)
						newText = newWord.get_text()
						wordsOnScreen.append((newText,G.get_hash_id(newText)))
						firstLetters.append(newText[0])
						newLetters = newWord.draw_by_letters((G.get_random(lanes),topY))
						thingsToDraw.append(newLetters)
						drawList(thingsToDraw)
						P.display.update()
					elif e.key == P.K_BACKSPACE:
						if lockedOn: #we know that hash and locked are set
							current_letter_idx -= 1
							thingsToDraw[findByHash(thingsToDraw,currentHash)][current_letter_idx][0].uncolor()
							drawList(thingsToDraw)
							P.display.update()
							if current_letter_idx == 0:
							# 	firstLetters.remove(lockedOnWord[0])
							  	resetVals()
						else:
							break
					else:
						break
				else:
					keyName = P.key.name(e.key)
					if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098):
						keyName = keyName.upper()
					if not lockedOn:
						lockedOnWord,currentHash = checkFirsts(wordsOnScreen,keyName)
						#print 'WOS = {}'.format(wordsOnScreen)
						if currentHash == -1:
							pass
						else: #assuming that all words are drawn letter by letter
							lockedOn = True
							thingsToDraw[findByHash(thingsToDraw,currentHash)][0][0].recolor()
							current_letter_idx += 1
							if current_letter_idx == len(lockedOnWord): #word only has one letter
								print 'one letter word removal'
								del thingsToDraw[findByHash(thingsToDraw,currentHash)]
								wordsOnScreen = removeByHash(wordsOnScreen,currentHash)
								firstLetters.remove(lockedOnWord[0])
								resetVals()
								scoreCount += 1
								if scoreCount % 3 == 0:
									multiplier += 0.05
									difficulty = difficulty*multiplier
									print 'difficulty increasing'								
								break
							break
					if lockedOn: #this means hash, locked on word are set
						#print "locked on word is -- " + lockedOnWord
						if keyName == lockedOnWord[current_letter_idx]:
							thingsToDraw[findByHash(thingsToDraw,currentHash)][current_letter_idx][0].recolor()
							current_letter_idx += 1
							if current_letter_idx == len(lockedOnWord):
								print 'larger word removal'
								del thingsToDraw[findByHash(thingsToDraw,currentHash)]
								wordsOnScreen = removeByHash(wordsOnScreen,currentHash)
								firstLetters.remove(lockedOnWord[0])
								resetVals()
								scoreCount += 1
								if scoreCount % 3 == 0:
									multiplier += 0.05
									difficulty = difficulty*multiplier
									print 'difficulty increasing'
						else:
							print 'wrong letter'

		drawList(thingsToDraw)
		P.display.update()
	print 'broke out of loop ---- oops'