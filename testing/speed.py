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

To implement still

- Scoring

- Feedback for when words are successfully typed? Sound? Animation?

- Make a function that will make sure that words generated on screen don't have the same opening 
letter. This will allow for us to have words falling on screen, and only one word is typable
at any time given a starting letter. 

	(Im thinking a while loop on a produce random funciton that takes in a list of bad letters)


- Clean up stuff is last thing.  
     (but let's make it as clean as possible as we go along!!)   
'''
def testingSpeed():
	mainLoop = True
	screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
	gm = GameMenu(screen,[],G.SKY_BLUE)
	words = G.make_word_list('speedWords.txt')
	P.key.set_repeat(500,50) #so people can hold a key down
	clock = P.time.Clock()
	P.time.set_timer(P.USEREVENT, 16)
	centerX = G.SCREEN_CENTER[0]
	centerY = G.TOP_CENTER[1]
	topY = 0
	lanes = [centerX-200,centerX-100,centerX,centerX+100,centerX+200]
	# testWord = Word.create_word("test").get_label()
	thingsToDraw = []
	wordsOnScreen = []
	# for x in lanes:
	# 	thingsToDraw.append((testWord,(x,centerY)))
	milliCounter = 0 
	def drawList(thingsToDraw):
		for (letters, (x, y)) in thingsToDraw:
			G.draw_letter_list(gm, letters, (x, y))

	def moveDown(things):
		newList = []
		for i in range(len(things)):
			newList.append((things[i][0],(things[i][1][0],things[i][1][1]+0.25*G.DIFFICULTY_LEVEL)))

		return newList
	
	def checkDrawList(things): #checks for the word crossing bottom boundary (decrease score etc)
		for (letters,(x,y)) in things:
			if y > G.D_HEIGHT:
				return thingsToDraw[1:] # removes the word from the screen
		return thingsToDraw


	def findWordByLetter(c, thingsToDraw):
		# find the first word in the list of words on screen that starts with given letter
		for idx, (letters, (x, y)) in enumerate(thingsToDraw):
			if letters[0].letter == c:
				return (letters, idx)
		return (None, -1)

	gm.screen.fill(G.BLACK)
	P.display.flip()

	currently_typing = None
	current_word_idx = -1

	first_letters = []


	while(mainLoop):
		for e in P.event.get():
			gm.screen.fill(G.BLACK)
			if e.type == P.QUIT:
				mainLoop = False
				break

			if e.type == P.KEYDOWN:
				if e.key == P.K_ESCAPE:
					mainLoop = False
					break
				if e.key == P.K_BACKSPACE:
					if currently_typing is not None:
						currently_typing[current_word_idx].set_font_color(G.WHITE)
						current_word_idx -= 1
						if current_word_idx < 0:
							currently_typing = None
					else:
						pass 
						# remove the last typed in currently_typing
						# if it's empty, then set currently_typing to none
				elif e.key in range(0,255):
					key_name = P.key.name(e.key)
					if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098): #checks for left shift and right shift
						key_name = key_name.upper()

					if currently_typing is None:
						# find if there's a word on screen starting with this
						currently_typing, curr_idx_in_drawlist = findWordByLetter(key_name, thingsToDraw)
						if currently_typing is not None:
							# if this word is found, color the first letter green
							currently_typing[0].set_font_color(G.GREEN)
							current_word_idx = 0

							# check if the word is already done being typed
							if current_word_idx == len(currently_typing) - 1:
								# remove from draw list 
								thingsToDraw.pop(curr_idx_in_drawlist)

								# remove its first letter from the first letters list
								first_letters.remove(currently_typing[0].letter)
								currently_typing = None

								# if there aren't other things to draw, set the counter to 0 so we spawn a new one
								if len(thingsToDraw) == 0:
									milliCounter = 0


						pass
						
					else:
						if currently_typing[current_word_idx + 1].letter == key_name:
							# if the letter is the next in the word currently being typed, color it
							current_word_idx += 1
							currently_typing[current_word_idx].set_font_color(G.GREEN)
							if current_word_idx == len(currently_typing) - 1:
								thingsToDraw.pop(curr_idx_in_drawlist)
								
								# remove its first letter from the first letters list
								first_letters.remove(currently_typing[0].letter)

								# set currently typing to none
								currently_typing = None
								current_word_idx = -1

								if len(thingsToDraw) == 0:
									milliCounter = 0
								# this was the last letter of the word. Remove the word from the list of things to draw

						pass
						# check if this is the next letter in the words
							# if it is, update and color it
							# if it's not, don't do it

				else:
					pass
		
		if milliCounter % (300/G.DIFFICULTY_LEVEL) == 0 or len(thingsToDraw) == 0:
			new_word = G.get_random_no_dups(words, first_letters)
			new_word_obj = Word.create_word(new_word)
			thingsToDraw.append((new_word_obj.letters, (G.getRandom(lanes),topY)))
			first_letters.append(new_word[0])
			milliCounter = 0
		milliCounter += 1

		thingsToDraw = moveDown(thingsToDraw)
		thingsToDraw = checkDrawList(thingsToDraw)
		drawList(thingsToDraw)
		P.display.update()
		clock.tick(60)
