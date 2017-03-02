from word import Word
from letter import Letter
import math

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

	def set_pos(radius):
		self.set_position(math.cos(angle) * radius, math.sin(angle) * radius)
