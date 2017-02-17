import pygame
import time
import random
 
pygame.init()

#Global difficulty value. Will change if the user would like to
DIFFICULTY_LEVEL = 1

#Global width/height values. Can be changed to whatever.
display_width = 1000
display_height = 750

#Colors black and white
black = (0,0,0)
white = (255,255,255)

#Game display and clock.
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Settings')
clock = pygame.time.Clock()

#IMPLEMENTED THIS WAY BECAUSE OF THE BUTTON FUNCTION...

#Set difficulty to 1 function
def set_1():
    global DIFFICULTY_LEVEL
    DIFFICULTY_LEVEL = 1
    return DIFFICULTY_LEVEL

#Set difficulty to 2 function
def set_2():
    global DIFFICULTY_LEVEL
    DIFFICULTY_LEVEL = 2
    return DIFFICULTY_LEVEL

#Set difficulty to 3 function
def set_3():
    global DIFFICULTY_LEVEL
    DIFFICULTY_LEVEL = 3 
    return DIFFICULTY_LEVEL

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Button function implemented with help from https://pythonprogramming.net/pygame-button-function-events/
#Button function that allows you to create a button on page of specified width/height
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

#General settings function for settings page
def settings():
    settings_menu = True
    #Settings Menu Initialize
    while settings_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 

        #Background will be white
        gameDisplay.fill(white)

        #Define text size 
        largeText = pygame.font.Font(None, display_width/12)
        
        #Level of difficulty
        TextSurf, TextRect = text_objects("Level of Difficulty", largeText)	

        #Center text
        TextRect.center = ((display_width*0.50),(display_height*0.25))

        gameDisplay.blit(TextSurf, TextRect)

        #Pygame function to get the x,y coordinates on screen. Will use for button functionality
        mouse = pygame.mouse.get_pos()

        #Difficulty level options
        button("3", display_width*0.65, display_height*0.40, display_width/20, display_height/20, white, white, set_3)
        button("2", display_width*0.45, display_height*0.40, display_width/20, display_height/20, white, white, set_2)
        button("1", display_width*0.25, display_height*0.40, display_width/20, display_height/20, white, white, set_1)

        #Quit option
        button("Quit", display_width*0.75, display_height*0.75, display_width/15, display_height/20, white, white)

        #Main menu option
        button("Back to Main Menu", display_width*0.25, display_height*0.75, display_width/15, display_height/20, white, white)
	   
        print DIFFICULTY_LEVEL
        pygame.display.update()
        clock.tick(20)
            
settings()
pygame.quit()
quit()