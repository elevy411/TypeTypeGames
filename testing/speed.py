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
	gameOver = False
	screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
	gm = GameMenu(screen,[],G.SKY_BLUE)
	words = G.make_word_list('speedWords.txt')
	P.key.set_repeat(500,50) #so people can hold a key down
	clock = P.time.Clock()
	P.time.set_timer(P.USEREVENT, 16)
	centerX = G.SCREEN_CENTER[0]
	centerY = G.TOP_CENTER[1]
	topY = 0
	
	topLeft = (G.TOP_CENTER[0]-225,G.TOP_CENTER[1]-50)
	topLeft2 = (topLeft[0],topLeft[1]+25)

	lanes = [centerX-200,centerX-100,centerX,centerX+100,centerX+200]
	# testWord = Word.create_word("test").get_label()
	thingsToDraw = []
	wordsOnScreen = []
	# for x in lanes:
	# 	thingsToDraw.append((testWord,(x,centerY)))
	milliCounter = 0 

	difficulty = G.DIFFICULTY_LEVEL
	score = G.SCORE
	health = 5

	scoreWord = Word([],"Score: {}".format(score),G.RED,G.MONOSPACE_FONT,25).get_label()
	healthWord = Word([],"Health: {}".format(health),G.RED,G.MONOSPACE_FONT,25).get_label()	

	userStats = [(scoreWord,topLeft),(healthWord,topLeft2)]

	thingsToDraw.append(userStats)

	gm.screen.fill(G.BLACK)
	P.display.flip()

	currently_typing = None
	current_word_idx = -1
	curr_idx_in_drawlist = 0
	first_letters = []

	#P.mixer.init()
	# sound_hit_bottom = P.mixer.Sound("./static/HitsBottom.ogg")
	# sound_correct_word = P.mixer.Sound("./static/SpeedCorrectWord.ogg")
	#sound_wrong_letter = P.mixer.Sound("./static/SpeedWrongLetter.ogg")


	def updateScore():
		userStats[0] = (Word([],"Score: {}".format(score),G.RED,G.MONOSPACE_FONT,25).get_label(),topLeft)
		thingsToDraw[0] = userStats

	def updateHealth():
		userStats[1] = (Word([],"Health: {}".format(health),G.RED,G.MONOSPACE_FONT,25).get_label(),topLeft2)
		thingsToDraw[0] = userStats

	def drawList(thingsToDraw):
		scr,(tlx,tly) = thingsToDraw[0][0]
		hlt,(tlx2,tly2) = thingsToDraw[0][1]
		G.draw(gm,scr,(tlx,tly))
		G.draw(gm,hlt,(tlx2,tly2))
		for (letters, (x, y)) in thingsToDraw[1:]:
			G.draw_letter_list(gm, letters, (x, y))

	def moveDown(things):
		newList = []
		for i in range(len(things)):
			if i != 0:
				newList.append((things[i][0],(things[i][1][0],things[i][1][1]+0.20*G.DIFFICULTY_LEVEL)))
		return [things[0]] + newList
	
	def checkDrawList(things, curr): #checks for the word crossing bottom boundary (decrease score etc)
		for (letters,(x,y)) in things[1:]:
			if y > G.D_HEIGHT:
				P.mixer.Sound.play(sound_hit_bottom)
				if letters == curr:
					print "currently typing the word that died"
					currently_typing = None
				return things[2:] # removes the word from the screen
		return things


	def findWordByLetter(c, thingsToDraw):
		# find the first word in the list of words on screen that starts with given letter
		for idx, (letters, (x, y)) in enumerate(thingsToDraw):
			if idx != 0:
				if letters[0].letter == c:
					return (letters, idx)
		return (None, -1)

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
				if e.key == P.K_RETURN: #lets you stop typing a word and start another
					if currently_typing is not None:
						while current_word_idx >= 0:
							currently_typing[current_word_idx].set_font_color(G.WHITE)
							current_word_idx -= 1
						currently_typing = None
					else:
						pass
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
								# play the sound for completing the word
								# P.mixer.Sound.play(sound_correct_word)
								# remove from draw list 
								thingsToDraw.pop(curr_idx_in_drawlist)

								# remove its first letter from the first letters list
								first_letters.remove(currently_typing[0].letter)
								currently_typing = None

								# if there aren't other things to draw, set the counter to 0 so we spawn a new one
								if len(thingsToDraw) == 0:
									milliCounter = 0

								score += 10*difficulty
								updateScore()
						pass
						
					else:
						if currently_typing[current_word_idx + 1].letter == key_name:
							# if the letter is the next in the word currently being typed, color it
							current_word_idx += 1
							currently_typing[current_word_idx].set_font_color(G.GREEN)
							if current_word_idx == len(currently_typing) - 1:
								# play the sound for completing the word
								# P.mixer.Sound.play(sound_correct_word)
								# remove from draw list
								thingsToDraw.pop(curr_idx_in_drawlist)
								
								# remove its first letter from the first letters list
								first_letters.remove(currently_typing[0].letter)
								currently_typing = None

								if len(thingsToDraw) == 0:
									milliCounter = 0

								score += 10*difficulty
								updateScore()
								# this was the last letter of the word. Remove the word from the list of things to draw
						else: 
							#P.mixer.Sound.play(sound_wrong_letter)
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

		#changing list size while going through causes error so do outside loop
		removeFirst = False
		for i in range(len(thingsToDraw)):
			if i != 0:
				(letters,(x,y)) = thingsToDraw[i]
				if y > G.D_HEIGHT:
					removeFirst = True
					# P.mixer.Sound.play(sound_hit_bottom)
					if letters == currently_typing:
						print "currently typing the word that died"
						currently_typing = None
					break
		if removeFirst:
			first_letters = first_letters[1:]
			thingsToDraw = [thingsToDraw[0]] + thingsToDraw[2:] # removes the word from the screen
			curr_idx_in_drawlist -= 1
			removeFirst = False
			health -= 1
			updateHealth()
			if health == 0:
				gameOver = True
				mainLoop = False

		thingsToDraw = checkDrawList(thingsToDraw, currently_typing)
		drawList(thingsToDraw)
		P.display.update()
		clock.tick(60)

	while gameOver:
		gm.screen.fill(G.BLACK)
		G.draw(gm,Word.create_word("GAME OVER").get_label(),(centerX,centerY))
		G.draw(gm,Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100))
		G.draw(gm,Word.create_word('Final Score: {}'.format(score)).get_label(),(centerX,centerY+100))
		P.display.update()

		for e in P.event.get():

			if e.type == P.QUIT:
				gameOver = False
				break

			if e.type == P.KEYDOWN:
				
				if e.key == P.K_ESCAPE:
					gameOver = False
					break
			else:
				pass