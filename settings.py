import pygame
import time
import random
 
pygame.init()


DIFFICULTY_LEVEL = 1

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Settings')
clock = pygame.time.Clock()

def set_1():
    DIFFICULTY_LEVEL = 1
    return DIFFICULTY_LEVEL

def set_2():
    DIFFICULTY_LEVEL = 2
    return DIFFICULTY_LEVEL

def set_3():
    DIFFICULTY_LEVEL = 3 
    return DIFFICULTY_LEVEL

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg,xcoor,ycoor,width,height,color,color2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if xcoor+width > mouse[0] > xcoor and ycoor+height > mouse[1] > ycoor:
        if click[0] == 1 and action != None:
            action()
        elif click[0] == 1 and action == None:
            quit()
            

    else:
        pygame.draw.rect(gameDisplay, color,(xcoor,ycoor,width,height))

    smallText = pygame.font.SysFont(None, display_width/20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((xcoor+(width/2)), (ycoor+(height/2)))
    gameDisplay.blit(textSurf, textRect)

def settings():
	
    settings_menu = True
    while settings_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 

        gameDisplay.fill(white)
        largeText = pygame.font.Font(None, display_width/12)
        TextSurf, TextRect = text_objects("Level of Difficulty", largeText)	
        TextRect.center = ((display_width*0.50),(display_height*0.25))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        button("3", display_width*0.65, display_height*0.40, display_width/20, display_height/20, white, white, set_3())
        button("2", display_width*0.45, display_height*0.40, display_width/20, display_height/20, white, white, set_2())
        button("1", display_width*0.25, display_height*0.40, display_width/20, display_height/20, white, white, set_1())

        button("Quit", display_width*0.75, display_height*0.75, display_width/15, display_height/20, white, white)
        button("Back to Main Menu", display_width*0.25, display_height*0.75, display_width/15, display_height/20, white, white)
	   
        print DIFFICULTY_LEVEL
        pygame.display.update()
        clock.tick(20)
            

settings()
pygame.quit()
quit()