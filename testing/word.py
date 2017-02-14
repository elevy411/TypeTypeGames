import sys
import pygame
from letter import Letter
import Globals as G

pygame.init()

class Word(pygame.font.Font):
    def __init__(self,letters,text='',font_color=G.WHITE,font=G.MONOSPACE_FONT,font_size=30,(pos_x,pos_y)=(0,0)):

        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font = font
        self.letters = letters
        self.font_color = font_color
        self.font_size = font_size
        self.label = self.render(self.text,1,self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        for i in rgb_tuple:
            if i > 255 or i < 0:
                raise Exception('RGB bounds violated')
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

    def set_text(self):
    	text = ''
    	for val in map(lambda let: let.get_letter(),self.letters):
    		text += val
    	self.text = text

    def get_text(self):
    	self.update()
        return self.text

    def set_label(self):
        self.label = self.render(self.text,1,self.font_color)

    def get_label(self):
        return self.label

    def add_letter(self,let):
    	self.letters.append(let)
    	self.update()

    def remove_letter(self):
    	self.letters = self.letters[:-1]
    	self.update()

    def get_letters(self):
        return self.letters

    def clear(self):
    	self.letters = []
    	self.update()

    def update(self):
    	self.set_text()
    	self.set_label()

    @staticmethod
    def create_word(stringWord):
        letters = []
        for letter in stringWord:
            letters.append(Letter(letter))
        return Word(letters,stringWord)

    def equals(self,otherWord):
        if self.text == otherWord.get_text():
            return True
        else:
            return False

    def print_facts(self):
        print "Value -- {}\n".format(self.text)
        print "Width -- {}\n".format(self.width)
        print "Height -- {}\n".format(self.height)
        print "Pos -- ({},{})\n".format(self.pos_x,self.pos_y)

    def print_letter_facts(self):
        for letter in self.letters:
            letter.print_facts()
