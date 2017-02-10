import pygame
from word import Word
from letter import Letter

class TypeGame():
    def __init__(self, screen, bg_color):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.center = (self.scr_width / 2, self.scr_height / 2)

        self.bg_color = bg_color
        self.clock = pygame.time.Clock()

        self.mouse_is_visible = False
        self.items = []


    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def handle_key_event(self, key):
        screenWord = Word([])

        if key in range(0,255):
            self.screen.fill(self.bg_color)
            screenWord.add_letter( Letter(pygame.key.name(key) ))
            label = screenWord.get_label()
            label_rect = label.get_rect(center=self.center)
            self.screen.blit(label,label_rect)
            pygame.display.flip()

    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            mouse_pos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.handle_key_event(event.key)
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
                #if self.mouse_is_visible:
                    #self.set_mouse_selection(item, mpos)
                self.screen.blit(item.label, item.position)

            pygame.display.flip()