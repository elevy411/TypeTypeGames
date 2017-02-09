import sys
import pygame
from letter import Letter
import Globals as G

pygame.init()

class Word(pygame.font.Font):
    def __init__(self,letters,text='',font=None,font_size=30,font_color=G.WHITE,(pos_x,pos_y)=(0,0)):
        
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