import sys
from time import sleep
import pygame as P
from letter import Letter
from word import Word
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu
import random

P.init()

velocity = 1;
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
band_pos = 360 # this will be toward the bottom of the screen
band_left = (0,360)
band_right = (640,360)
#margin of error around band line that will still count as valid
band_range = 10
FRAMERATE = 60

def reset_velocity(): # using difficulty stored in Globals, we're setting the velocity
    #velocity is defined as number of pixels to shift per refresh
    if G.DIFFICULTY_LEVEL == 1:
        velocity = 2
    elif G.DIFFICULTY_LEVEL == 2:
        velocity = 3
    elif G.DIFFICULTY_LEVEL == 3:
        velocity = 4
    return None

'''
    update_position: updates position of input letter to redraw
    letter: letter whose position to update
'''
def update_position(letter): 
    letter.set_position(letter.pos_x, letter.pos_y + velocity)
    return None # do we need to return the updated object?
    
def spawn_letter():
    ret = Letter(alphabet[random.randrange(0,26,1)])
    # gives us x number between 30 and 610, in lanes 30 pixels wide
    ret.set_position(random.randrange(30, 610, 30), 0) 
    return ret
  
def typing():
    loop = True
    
    screen = P.display.set_mode((G.D_WIDTH, G.D_HEIGHT),0,32)
    gm = GameMenu(screen,[],G.BLACK)
    
    topCenter = G.TOP_CENTER
    topLeft = (topCenter[0]-200,topCenter[1]-50)
    topRight = (topCenter[0]+200,topCenter[1]-50)
    BG_COLOR = G.BLACK
    LETTER_COLOR = G.WHITE
    score = G.SCORE
    
# determine whether a given letter is within the desired band
    def within_range(input_letter):
        if ( input_letter.pos_y > band_pos + band_range and input_letter.pos_y < band_pos - band_range):
            return True
        else:
            return False
    
    def draw_list(surfs): # is this at the correct level of indentation?
        for (label,(x,y)) in surfs:
            G.draw(gm,label,(x,y))
    
    thingsToDraw = []
    
    centerX = G.SCREEN_CENTER[0]
    centerY = G.TOP_CENTER[1]
    difficulty_setting = G.DIFFICULTY_LEVEL
    reset_velocity()
    
    P.time.set_timer(P.USEREVENT, 1000) # timer set for each second
    
    #rounds are 60 seconds no matter what
    timeCount = 60
    timeText = "1:00"
    
    gm.screen.fill(BG_COLOR)
    thingsToDraw.append((Word.create_word('Score: {}'.format(score)).get_label(),topLeft)) # display the current score in the top left
    thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))
    
    initial_letter = spawn_letter()
    current_letters = [initial_letter]
    print initial_letter.position
    thingsToDraw.append((initial_letter.get_label(),initial_letter.position))
    
    draw_list(thingsToDraw)
    P.display.flip()
    

    thingsToDraw=[]
    counter = 0
    spawn_letter_interval = 60 # letters will spawn at a constant speed
    

    clock = P.time.Clock()
    
    while loop:

        clock.tick(FRAMERATE)
        gm.screen.fill(BG_COLOR)

        thingsToDraw.append((Word.create_word('Score: {}'.format(score)).get_label(),topLeft)) # display the current score in the top left
        thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))
       
        counter += 1 # this counter will be used to determine when to spawn a new letter
        if (counter % spawn_letter_interval == 0): # when the interval between letter spawning has passed
            new_letter = spawn_letter()
            current_letters.append(new_letter)
        #see if update time
        if (counter % FRAMERATE == 0):
            timeCount -= 1
            print timeCount
            if timeCount >= 10:
                timeText = "0:{}".format(timeCount)
            elif timeCount >= 0:
                timeText = "0:0{}".format(timeCount)
            else: 
                thingsToDraw = []
                thingsToDraw.append((Word.create_word('Game Over!').get_label(),topCenter))
                thingsToDraw.append((Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100)))
                thingsToDraw.append((Word.create_word('Your Score was {}'.format(score)).get_label(),(centerX,centerY+100)))
                draw_list(thingsToDraw)
                P.display.update()
                loop = False
                #would like to figure out why sleep
                sleep(2.0)
                break
                    
        for e in P.event.get(): 
            gm.screen.fill(BG_COLOR)
            if e.type == P.QUIT:
                loop = False
                break
   #         if e.type == P.USEREVENT: # code taken (and modified) from basic typing game

            if e.type == P.KEYDOWN: # if the user has pressed a key
                #user wants to leave this place
                if e.key== P.K_ESCAPE:
                    loop = False
                    break
                #if ASCII, basically
                elif e.key in range(0,255):
                    keyName = P.key.name(e.key)
                    #if we decide to throw in capital letters use this
                    #if P.key.get_mods() in (1,2) or P.key.get_mods() in (4097,4098): #checks for left shift and right shift
                        #keyName = keyName.upper()
                    is_in_band = False
                    for character in current_letters:
                        if character.letter == keyName:
                            
                            if within_range(character):
                                current_letters.remove(character)
                                score += 10
                                is_in_band = true
                                break
                    if not is_in_band: # deduct 5 points if there is no matching letter within the band
                        if score - 5 >= 0:
                            score -= 5
                        else:
                            score = 0
                #special non-ESC character entered, deduct points for mistyping
                else: 
                    if score - 5 >= 0:
                        score -= 5
                    else:
                        score = 0
        #only consider letters that did not fall below band
        updated_list = [x for x in current_letters if
            (x.pos_y < band_pos - band_range)]
        current_letters = updated_list

        #add all letters with updated positons to thingsToDraw
        for i in range(len(current_letters)):        
            #print current_letters[i].position
            update_position(current_letters[i])
            current_letters[i].set_label()
            thingsToDraw.append((current_letters[i].get_label(), 
                    current_letters[i].position))

        draw_list(thingsToDraw)
        P.display.update()
        #print thingsToDraw
        thingsToDraw = []
