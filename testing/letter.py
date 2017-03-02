import sys
import pygame
import Globals as G

pygame.init()

class Letter(pygame.font.Font):
    def __init__(self,letter,font_color=G.WHITE,font=G.MONOSPACE_FONT,font_size=30,(pos_x,pos_y)=(0,0)):
 
        pygame.font.Font.__init__(self, font, font_size) #intialize the font object from super class
        self.letter = letter #string with letter value eg: "v"
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.label = self.render(self.letter,1,self.font_color) #the image that gets put to screen with font_color
        self.width = self.label.get_rect().width #width of rectangle of label (the image)
        self.height = self.label.get_rect().height #height of rectangle of label (the image)
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x #position in space x direction
        self.pos_y = pos_y #position in space y direction
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.letter, 1, self.font_color)

    def set_letter(self,letter):
        self.letter = letter

    def get_letter(self):
        return self.letter
    
    def set_label(self,font_color=G.WHITE):
        self.label = self.render(self.letter,1,font_color)

    def get_label(self):
        return self.label

    def equals(self,otherLetter):
        if self.letter == otherLetter.get_letter():
            return True
        else:
            return False

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    
    def recolor(self):
        self.set_font_color(G.GREEN)

    def uncolor(self):
        self.set_font_color(G.WHITE)

    def print_facts(self):
        print "Value -- {}\n".format(self.letter)
        print "Width -- {}\n".format(self.width)
        print "Height -- {}\n".format(self.height)
        print "Pos -- ({},{})\n".format(self.pos_x,self.pos_y)
