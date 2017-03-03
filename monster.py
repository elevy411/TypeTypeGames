from time import sleep
import sys
import pygame as P
from word import Word
from letter import Letter
#from TypeTest import TypeTest
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu


class FieldMonsters():
	def __init__(self, words, n):
		self.fieldMs = []
		self.pool = words
		self.chosen = []
		angles = list(0, math.pi/2, math.pi, 3 * math.pi/2)
		r = 1
		while (2 << r) < n:
			a = math.pi/(2 << r)
			while a < 2 * math.pi:
				angles.append(a)
				a += 2 * math.pi/(2 << r)
			r += 1
		for i in range(n):
			self.fieldMs.append(self.addRandomWord(angles[n]))

	def tryLetter(self, letter):
		for i in self.fieldMs:
			if letter == i.getHead():
				i_len = i.updateWord()

	def resetChosen(self):
		self.chosen = []

	def delete(self, monster):
		for i in range(len(self.fieldMs)):
			if self.fieldMs[i] == monster:
				self.fieldMs[i].detach()
				del self.fieldMs[i]

	def addRandomWord(self, angle):
		word = self.pool[Random.randint(len(self.pool))]
		while word not in self.chosen:
			word = self.pool[Random.randint(len(self.pool))]
		self.chosen.append(word)
		return Monster(word, self, angle)


class Monster(Word):
	def __init__(self, word, parent, angle):
		Word.__init__(self, [Letter(letter) for letter in word], word)
		self.head = self.get_letters[0]
		self.angle = angle
		self.parent = parent

	def getHead(self):
		return self.head

	#Assume that word will update when a letter has been typed?
	def updateWord(self):
		self.pop()
		if len(self.get_letters) > 0:
			self.head = self.get_letters[0]
		else:
			self.parent.delete(self)

	def attach(self, monster_list):
		self.parent = parent

	def detach(self):
		self.parent = []

	def get_pos(radius):
		self.set_position(math.cos(angle) * radius, math.sin(angle) * radius)
		return math.cos(angle) * radius, math.sin(angle) * radius




P.init()

SCREEN_CENTER = (320,240)


def typing():
	draw_count = 0
	r = 200
	fm_Count = 4
	polarWordPos = math.pi/2.0
	loop = True
	startOver = True
	screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
	gm = GameMenu(screen,[],G.BLACK)

	#Initialize screenwords to eventually fill words into
	screenWord = []
	for i in range(8):
		screenWord[i] = Word([])
	words = G.make_word_list()
	wordList = map(lambda listword: Word.create_word(listword),words)
	currentLetterCount = []
	topCenter = TOP_CENTER
	leftCenter = LEFT_CENTER
	rightCenter = RIGHT_CENTER
	bottomCenter = BOTTOM_CENTER

	#Get 4 words at a time

	fieldMsLabel = []



	centerX = screenCenter[0]
	centerY = screenCenter[1]

	def draw_list(thingsToDraw):
		for (label,(x,y)) in thingsToDraw:
			G.draw(gm,label,(x,y))

	thingsToDraw = []
	lastLetter = None
	xDifferentials = []


	P.time.set_timer(P.USEREVENT, 1000)
	difficulty_setting = G.DIFFICULTY_LEVEL


	timeCount = 60.0
	originaltimeCount = timeCount
	timeText = "1:00"

	if difficulty_setting == 1:
		fm_Count = 3
	elif difficulty_setting == 2:
		fm_Count = 5
	else:
		fm_Count = 8

	score = G.SCORE


	gm.screen.fill(BG_COLOR) # set initial background

	thingsToDraw = [(fieldMsLabel[i].get_label(), fieldMsLabel[i].get_pos(r)) for i in range(fm_Count)]

	#This will be our tracker to see which letter count that all our words are on
	currentLetterCount[i] = 0

	thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))
	thingsToDraw.append((Word.create_word('Score: {}'.format(score)).get_label(),topLeft))
	draw_list(thingsToDraw)
	P.display.flip()

	while loop:
		thingsToDraw = [(fieldMsLabel[i].get_label(), fieldMsLabel[i].get_pos(r)) for i in range(fm_Count)]


		for e in P.event.get():
			gm.screen.fill(BG_COLOR)
			if e.type == P.QUIT:
				# exit the loop if input is quit
				loop = False
				startOver = False
				break
			if e.type == P.USEREVENT:
				timeCount -= 1.0

				#For the loop, while the time counts down every second, we will inch the position of the words closer to the center
				thingsToDraw = [(fieldMsLabel[i].get_label(), fieldMsLabel[i].get_pos(r*(timeCount / originaltimeCount))) for i in range(fm_Count)]
				for i in range(fm_Count):
					draw_count += 1
					fieldMsLabel[i] = fieldMs[i].get_label()
					xyWordPos = convertPos(r*(timeCount / originaltimeCount))
					thingsToDraw.append(fieldMsLabel[i], xyWordPos)

				#Just the time counter..
				if timeCount >= 10:
					timeText = "0:{}".format(timeCount)
				elif timeCount >= 0:
					timeText = "0:0{}".format(timeCount)
				else:
					#If the time counter is out, then end the game.
					gm.screen.fill(BG_COLOR)
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
				thingsToDraw[draw_count+1] = (timeWord.get_label(),topRight)
				draw_list(thingsToDraw)
				P.display.update()

			if e.type == P.KEYDOWN:
				if e.key in G.SPECIAL_KEYS:
					# for special key presses
					if e.key == P.K_ESCAPE:
						# exit loop if escape
						loop = False
						startOver = False
						break

				#IF PRESS KEY THAT IS NOT A SPECIAL KEY (AKA JUST A REGULAR KEY)
				elif e.key in range(0,255):
						#CHECKS TO SEE IF THE LETTER COUNT OF THE WORD TYPED IN = THE LETTER COUNT OF THE WORD WE HAVE TO TYPE
						keyName = P.key.name(e.key)

						#Simply updates the key name to uppercase if shift + key is pressed
						if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098): #checks for left shift and right shift
							keyName = keyName.upper()

						#Will check all monsters in fieldmonsters
						for wordmonster in fieldMs:

							#Compare keyname with the first letter of the word, and if it ==, then update the word and add +10
							if keyName == wordmonster.getHead():
								wordmonster.update()
								score += 10
								#Also, now that we have updated, we want to check if the len is 0. If it is 0, then we will +30 on the sore
								#And also detach the wordmonster from the list
								if len(wordmonster.word) == 0:
									score += 30
									wordmonster.detach()

								#Now let's update the image...
								thingsToDraw[draw_count+2] = (Word.create_word('Score: {}'.format(score)).get_label(),topLeft)
								thingsToDraw = thingsToDraw[0:len(thingsToDraw)-1]
								draw_list(thingsToDraw)
								P.display.update()

#KEEP WORKING ON CODE FROM THIS POINT ON...

						screenletter = Letter(keyName,LETTER_COLOR)

						letterWidth = screenletter.get_width()
						xDifferentials = map(lambda x: x + letterWidth,xDifferentials)


						offsetCenter = centerX + ((letterWidth * (screenWord.length - 1)) / 2)

						thingsToDraw = thingsToDraw[0:3]
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
