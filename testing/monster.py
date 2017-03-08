from time import sleep
import sys, os
import pygame as P
from word import Word
from letter import Letter
import math, random
#from TypeTest import TypeTest
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu
import psutil

BG_PATH = "TTM_Files/Monster_Background.jpg"
BG_WAND = "TTM_Files/wand2.png"


class Image(P.sprite.Sprite):
    def __init__(self, filepath, coord):
        P.sprite.Sprite.__init__(self)
        self.image = P.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = coord
        self.w, self.h = self.image.get_size()
    def scale(self, factor):
		self.image = P.transform.scale(self.image, ((int)(self.w * factor), (int)(self.h*factor)))

class FieldMonsters():
	def __init__(self, words, n):
		self.fieldMs = []
		self.pool = words
		self.chosen = []
		self.toDelete = []
		angles = [0, math.pi/2, math.pi, 3 * math.pi/2]
		r = 1
		while (2 << r) < n:
			a = math.pi/(2 << r)
			while a < 2 * math.pi:
				angles.append(a)
				a += 2 * math.pi/(2 << r)
			r += 1
		for i in range(n):
			self.fieldMs.append(self.addRandomWord(angles[i]))

	def tryLetter(self, letter):
		changed = False
		for i in self.fieldMs:
			if letter.lower() == i.getHead():
				i.updateWord()
				changed = True
		for i in self.toDelete:
			self.delete(i)
		self.toDelete = []
		return changed

	def get_field(self):
		return self.fieldMs

	def resetChosen(self):
		self.chosen = []

	def queue_delete(self, monster):
		self.toDelete.append(monster)

	def delete(self, monster):
		for i in range(len(self.fieldMs)):
			if self.fieldMs[i] == monster:
				self.fieldMs[i].detach()
				del self.fieldMs[i]
				return

	def addRandomWord(self, angle):
		word = self.pool[random.randint(0, len(self.pool) - 1)]
		while word in self.chosen:
			word = self.pool[random.randint(0, len(self.pool) - 1)]
		self.chosen.append(word)
		return Monster(word, self, angle)


class Monster():
	def __init__(self, word, parent, angle):
		self.word = word
		self.head = word.get_letters()[0]
		self.angle = angle
		self.parent = parent

	def getHead(self):
		return self.head.letter.lower()

	#Assume that word will update when a letter has been typed?
	def updateWord(self):
		self.word.pop()
		if self.word.length > 0:
			self.head = self.word.get_letters()[0]
		else:
			self.parent.queue_delete(self)

	def attach(self, monster_list):
		self.parent = parent

	def detach(self):
		self.parent = []

	def get_pos(self, radius):
		return math.cos(self.angle) * radius + 320, math.sin(self.angle) * radius + 240


P.init()

SCREEN_CENTER = (320,240)

def typing():
	bkg = Image(BG_PATH, [0,0])
	wand = Image(BG_WAND, [290, 180])
	wand.scale(0.1)


	r = 200
	polarWordPos = math.pi/2.0
	loop = True
	startOver = True
	screen = P.display.set_mode((G.D_WIDTH,G.D_HEIGHT),0,32)
	BG_COLOR = G.BLACK
	gm = GameMenu(screen,[],G.BLACK)

	#Initialize screenwords to eventually fill words into
	words = G.make_word_list()
	wordList = map(lambda listword: Word.create_word(listword),words)
	currentLetterCount = []
	#Get 4 words at a time
	screenCenter = G.SCREEN_CENTER
	screenWord = Word([])
	topCenter = G.TOP_CENTER
	topLeft = (topCenter[0]-200,topCenter[1]-50)
	topRight = (topCenter[0]+200,topCenter[1]-50)
	LETTER_COLOR = G.DEF_LETTER_COLOR

	fieldMsLabel = []

	centerX = screenCenter[0]
	centerY = screenCenter[1]

	def draw_list(thingsToDraw):
		for (label,(x,y)) in thingsToDraw:
			G.draw(gm,label,(x,y))

	thingsToDraw = []
	lastLetter = None
	xDifferentials = []

	P.time.set_timer(P.USEREVENT, 10)
	difficulty_setting = G.DIFFICULTY_LEVEL


	if difficulty_setting == 1:
		fieldMsLabel = FieldMonsters(wordList, 2)
		timeCount = 5.00
		timeText = "0:05"
	elif difficulty_setting == 3:
		fieldMsLabel = FieldMonsters(wordList, 4)
		timeCount = 7.00
		timeText = "0:07"
	else:
		fieldMsLabel = FieldMonsters(wordList, 8)
		timeCount = 10.00
		timeText = "0:10"

	originaltimeCount = timeCount
	score = G.SCORE


	gm.screen.fill(BG_COLOR) # set initial background

	#This will be our tracker to see which letter count that all our words are on
	# currentLetterCount[i] = 0

	thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))
	thingsToDraw.append((Word.create_word('').get_label(), topRight))
	monsters = [(i.word.get_label(), i.get_pos(r)) for i in fieldMsLabel.get_field()]
	draw_list(thingsToDraw + monsters)
	P.display.flip()

	scalar = 0
	while loop:
		# P.display.update()
		for e in P.event.get():
			gm.screen.fill(BG_COLOR)
			screen.blit(bkg.image, bkg.rect)
			screen.blit(wand.image, wand.rect)
			if e.type == P.QUIT:
				# exit the loop if input is quit
				loop = False
				startOver = False
				break
			if e.type == P.USEREVENT:
				timeCount -= 0.01
				scalar += 1
				monsters = [(i.word.get_label(), i.get_pos(r * timeCount/originaltimeCount)) for i in fieldMsLabel.get_field()]
				draw_list(thingsToDraw + monsters)
				P.display.update()
				#Just the time counter..

				if scalar % 100 == 0:
					timeWord = Word.create_word(timeText[:4])
					thingsToDraw[0] = ((timeWord.get_label(),topRight))
					draw_list(thingsToDraw + monsters)
					P.display.update()

				if timeCount >= 10:
					timeText = "0:{}".format(timeCount)
				elif timeCount >= 0:
					timeText = "0:0{}".format(timeCount)

				else:
					#If the time counter is out, then end the game.
					gm.screen.fill(BG_COLOR)
					screen.blit(bkg.image, bkg.rect)
					thingsToDraw = []
					thingsToDraw.append((Word.create_word('Game Over! You Lose').get_label(),screenCenter))
					thingsToDraw.append((Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100)))
					thingsToDraw.append((Word.create_word('Your Score was {}'.format(score)).get_label(),(centerX,centerY+100)))
					draw_list(thingsToDraw)
					P.display.update()
					loop = False
					sleep(0.5)
					break

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

						LETTER_COLOR_CENTER = G.RED
						#Will check all monsters in fieldmonsters
						length = len(fieldMsLabel.get_field())
						tried = fieldMsLabel.tryLetter(keyName)
						if tried:
							score += 10
							LETTER_COLOR_CENTER = G.GREEN
							#Also, now that we have updated, we want to check if the len is 0. If it is 0, then we will +30 on the sore
							#And also detach the wordmonster from the list
							if len(fieldMsLabel.get_field()) < length:
								score += 30

							monsters = [(i.word.get_label(), i.get_pos(r * (timeCount / originaltimeCount))) for i in fieldMsLabel.get_field()]
							# P.display.update()

						thingsToDraw[1] = ((Letter(keyName, LETTER_COLOR_CENTER).get_label(),(320, 240)))
						draw_list(thingsToDraw + monsters)
						P.display.update()

						if len(fieldMsLabel.fieldMs) == 0:
							gm.screen.fill(BG_COLOR)
							screen.blit(bkg.image, bkg.rect)
							thingsToDraw = []
							thingsToDraw.append((Word.create_word('Game Over! You Win').get_label(), screenCenter))
							thingsToDraw.append((Word.create_word('Press Any Key To Continue').get_label(), (centerX, centerY-100)))
							thingsToDraw.append((Word.create_word('Your Score was {}'.format(score)).get_label(),(centerX,centerY+100)))
							draw_list(thingsToDraw)
							P.display.update()
							loop = False
							sleep(0.5)
							break

	while(startOver):
		sleep(0.5)
		for e in P.event.get():
			if e.type == P.QUIT:
				# exit the loop if input is quit
				p = psutil.Process()
				startOver = False
			if e.type == P.KEYDOWN:
				p = psutil.Process()
				startOver = False
