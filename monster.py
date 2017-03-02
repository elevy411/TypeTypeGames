import sys
import pygame as P
from word import Word
from letter import Letter
from TypeTest import TypeTest
import Globals as G
from game import Game
from menuItem import MenuItem
from gameMenu import GameMenu

class FieldMonsters():
	def __init__(self, words, n):
		self.fieldMs = []
		self.pool = words
		self.chosen = []
		for i in range(n):
			self.fieldMs.append(self.addRandomWord())

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

	def addRandomWord(self):
		word = self.pool[Random.randint(len(self.pool))]
		while word not in self.chosen:
			word = self.pool[Random.randint(len(self.pool))]
		word.attach(self)
		self.chosen.append(word)
		return word


class Monster(Word):
	def __init__(self, word, fieldMonsters=[]):
		Word.__init__(self, [Letter(letter) for letter in word], word)
		self.head = self.get_letters[0]
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
