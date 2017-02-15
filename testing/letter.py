import sys
import pygame
import Globals as G

pygame.init()

class Letter(pygame.font.Font):
    def __init__(self,letter,font_color=G.WHITE,font=G.MONOSPACE_FONT,font_size=30,(pos_x,pos_y)=(0,0),xspeed=0,yspeed=5):
 
        pygame.font.Font.__init__(self, font, font_size)
        self.letter = letter
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.label = self.render(self.letter,1,self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.xspeed = xspeed
        self.yspeed = yspeed

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def update_position(self):
        self.set_position((float)(self.pos_x+self.xspeed),  
             (float)(self.pos_y+self.yspeed))
             
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
        
    def print_facts(self):
        print "Value -- {}\n".format(self.letter)
        print "Width -- {}\n".format(self.width)
        print "Height -- {}\n".format(self.height)
        print "Pos -- ({},{})\n".format(self.pos_x,self.pos_y)
