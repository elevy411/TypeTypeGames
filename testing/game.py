
import sys
import pygame
from word import Word
from letter import Letter
from TypeTest import TypeTest
import Globals as G


pygame.init()
 
class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=G.WHITE, (pos_x, pos_y)=(0, 0)):
 
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
 
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

    def set_text(self,text):
        self.text = text

    def get_text(self):
        return self.text
    
    def set_label(self):
        self.label = self.render(self.text,1,self.font_color)

    def get_label(self):
        return self.label
 
class GameMenu():
    def __init__(self, screen, items, funcs, bg_color=G.BLUE, font=None, font_size=30,
                 font_color=G.WHITE):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.funcs = funcs
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)
 
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)
 
            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
 
        self.mouse_is_visible = True
        self.cur_item = None

    # Functions like these aren't really necesarry in python I think.
    def get_width(self):
        return self.scr_width

    def get_height(self):
        return self.scr_height
 
    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)
 
    def set_keyboard_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(G.WHITE)
 
        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0
 
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(G.RED)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()
 
    def set_mouse_selection(self, item, mpos):
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            item.set_font_color(G.RED)
            item.set_italic(True)
        else:
            item.set_font_color(G.WHITE)
            item.set_italic(False)
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            mpos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            self.funcs[item.text]()
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for item in self.items:
                if self.mouse_is_visible:
                    self.set_mouse_selection(item, mpos)
                self.screen.blit(item.label, item.position)

            pygame.display.flip()
    
    @staticmethod
    def typing():
        loop = True
        screen = pygame.display.set_mode((640,480),0,32)
        gm = GameMenu(screen,[],G.BLACK)
        pygame.display.flip()
        screenWord = Word([])
        pygame.key.set_repeat(500,50) #so people can hold a key down
        while loop:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    loop = False
                if e.type == pygame.KEYDOWN:
                    if e.key in G.SPECIAL_KEYS:    
                        if e.key == pygame.K_ESCAPE:
                            loop = False
                            break
                        if e.key == pygame.K_RETURN:
                            gm.screen.fill(G.BLACK)
                            screenWord.clear()
                            label = screenWord.get_label()
                            label_rect = label.get_rect(center=(gm.get_width()/2,gm.get_height()/2))
                            gm.screen.blit(label,label_rect)
                            pygame.display.flip()
                        if e.key == pygame.K_BACKSPACE:
                            gm.screen.fill(G.BLACK)
                            screenWord.remove_letter()
                            label = screenWord.get_label()
                            label_rect = label.get_rect(center=(gm.get_width()/2,gm.get_height()/2))
                            gm.screen.blit(label,label_rect)
                            pygame.display.flip()
                        else:
                            pass
                    elif e.key in range(0,255):
                        gm.screen.fill(G.BLACK)
                        screenWord.add_letter( Letter(pygame.key.name(e.key).upper()) )
                        label = screenWord.get_label()
                        label_rect = label.get_rect(center=(gm.get_width()/2,gm.get_height()/2))
                        gm.screen.blit(label,label_rect)
                        pygame.display.flip()

    @staticmethod
    def type_test():
        type_test_game = TypeTest(gm.screen)
        type_test_game.run()



if __name__ == "__main__":
 
    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)
 
    menu_items = ('Start', 'TypeTest', 'Quit')
    funcs = {'Start': GameMenu.typing,
             'TypeTest' : GameMenu.type_test,
             'Quit': sys.exit}
 
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()