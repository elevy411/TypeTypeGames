
import sys
import pygame
from word import Word
from letter import Letter
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu

pygame.init()
 
def typing():
    loop = True
    screen = pygame.display.set_mode((640,480),0,32)
    gm = GameMenu(screen,[],G.BLACK)
    pygame.display.flip()
    screenWord = Word([])
    words = G.make_word_list()
    wordList = map(lambda listword: Word.create_word(listword),words)
    pygame.key.set_repeat(500,50) #so people can hold a key down
    gm.screen.fill(G.BLACK)
    screenCenter = (gm.get_width()/2,gm.get_height()/2)
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
                        screenWord.clear()
                        label = screenWord.get_label()
                        draw(gm,label,screenCenter)
                        pygame.display.flip()
                    if e.key == pygame.K_BACKSPACE:
                        screenWord.remove_letter()
                        label = screenWord.get_label()
                        draw(gm,label,screenCenter)
                        pygame.display.flip()
                    else:
                        pass
                elif e.key in range(0,255):
                    screenWord.add_letter( Letter(pygame.key.name(e.key).upper()) )
                    label = screenWord.get_label()
                    draw(gm,label,screenCenter)
                    pygame.display.flip()

def draw(gm,label,center,bg_color=G.BLACK):
    gm.screen.fill(bg_color)
    label_rect = label.get_rect(center=center)
    gm.screen.blit(label,label_rect)

if __name__ == "__main__":
 
    # Creating the screen
    screen = pygame.display.set_mode((640, 480), 0, 32)
 
    menu_items = ('Start', 'Quit')
    funcs = {'Start': typing,
             'Quit': sys.exit}
 
    pygame.display.set_caption('Game Menu')
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()