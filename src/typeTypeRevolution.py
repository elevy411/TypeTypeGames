import sys
from time import sleep
import pygame as P
from letter import Letter
from word import Word
import Globals as G
from menuItem import MenuItem
from gameMenu import GameMenu
import random


velocity = 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
band_pos = 360 # this will be toward the bottom of the screen
band_left = (0,360)
band_right = (640,360)
#margin of error around band line that will still count as valid
band_range = 30
FRAMERATE = 60

BG_PATH = "static/TTR_Files/BKG1.jpg"


class Background(P.sprite.Sprite):
    def __init__(self, filepath, coord):
        P.sprite.Sprite.__init__(self)
        self.image = P.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = coord


def reset_velocity(): # using difficulty stored in Globals, we're setting the velocity
    #velocity is defined as number of pixels to shift per refresh
    global velocity
    if G.DIFFICULTY_LEVEL == 1:
        velocity = 1
    elif G.DIFFICULTY_LEVEL == 3:
        velocity = 2
    elif G.DIFFICULTY_LEVEL == 5:
        velocity = 3

'''
    update_position: updates position of input letter to redraw
    letter: letter whose position to update
'''
def update_position(letter):
    letter.set_position(letter.pos_x, letter.pos_y + velocity)

def spawn_letter():
    ret = Letter(alphabet[random.randrange(0,26,1)])
    # gives us x number between 30 and 610, in lanes 30 pixels wide
    ret.set_position(random.randrange(30, 610, 30), 0)
    return ret

def within_range(input_letter):
    if ( input_letter.pos_y >= band_pos - band_range and
        input_letter.pos_y <= band_pos + band_range):
        return True
    else:
        return False


def typing():
    line_color = G.WHITE
    P.mixer.music.load('static/sounds/The_Clubbing_of_Isaac.mp3')
    P.mixer.music.play(0)
    loop = True

    screen = P.display.set_mode((G.D_WIDTH, G.D_HEIGHT),0,32)
    gm = GameMenu(screen,[],G.BLACK)

    bkg = Background(BG_PATH, [0,0])

    topCenter = G.TOP_CENTER
    topLeft = (topCenter[0]-200,topCenter[1]-50)
    topRight = (topCenter[0]+200,topCenter[1]-50)
    BG_COLOR = G.BLACK
    LETTER_COLOR = G.WHITE
    score = G.SCORE

# determine whether a given letter is within the desired band

    def draw_list(surfs): # is this at the correct level of indentation?
        for (label,(x,y)) in surfs:
            G.draw(gm,label,(x,y))

    thingsToDraw = []

    centerX = G.SCREEN_CENTER[0]
    centerY = G.TOP_CENTER[1]
    difficulty_setting = G.DIFFICULTY_LEVEL


    P.time.set_timer(P.USEREVENT, 1000) # timer set for each second

    #rounds are 60 seconds no matter what
    timeCount = 60
    timeText = "1:00"

    gm.screen.fill(BG_COLOR)
    screen.blit(bkg.image, bkg.rect)
    thingsToDraw.append((Word.create_word('Score: {}'.format(score)).get_label(),topLeft)) # display the current score in the top left
    thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))

    initial_letter = spawn_letter()
    current_letters = [initial_letter]
    thingsToDraw.append((initial_letter.get_label(),initial_letter.position))

    draw_list(thingsToDraw)
    P.draw.line(screen,line_color,(0,band_pos),(G.D_WIDTH,band_pos),4)
    P.display.flip()

    reset_velocity()

    thingsToDraw=[]
    counter = 0
    line_counter = 0
    spawn_letter_interval = 15 + 60/G.DIFFICULTY_LEVEL # letters will spawn at a constant speed
    clock = P.time.Clock()

    while loop:
        clock.tick(FRAMERATE)
        gm.screen.fill(BG_COLOR)
        screen.blit(bkg.image,bkg.rect)
        thingsToDraw.append((Word.create_word('Score: {}'.format(score)).get_label(),topLeft)) # display the current score in the top left
        thingsToDraw.append((Word.create_word(timeText).get_label(),topRight))

        counter += 1 # this counter will be used to determine when to spawn a new letter
        line_counter += 1 # this counter will be used to determine when to revert the line color to white
        if (counter % spawn_letter_interval == 0): # when the interval between letter spawning has passed
            new_letter = spawn_letter()
            current_letters.append(new_letter)

        if (line_counter % (FRAMERATE / 4) == 0):
            line_color = G.WHITE
        #see if update time
        if (counter % FRAMERATE == 0):
            timeCount -= 1
            if timeCount >= 10:
                timeText = "0:{}".format(timeCount)
            elif timeCount >= 0:
                timeText = "0:0{}".format(timeCount)
            else:
                thingsToDraw = []
                thingsToDraw.append((Word.create_word('Game Over!').get_label(),topCenter))
                # thingsToDraw.append((Word.create_word('Press Any Key To Continue').get_label(),(centerX,centerY-100)))
                thingsToDraw.append((Word.create_word('Your Score was {}'.format(score)).get_label(),(centerX,centerY+100)))
                draw_list(thingsToDraw)
                P.display.update()
                P.mixer.music.stop()
                loop = False
                #would like to figure out why sleep
                sleep(5.0)
                break

        for e in P.event.get():
            if e.type == P.QUIT:
                P.mixer.music.stop()
                loop = False
                break
   #         if e.type == P.USEREVENT: # code taken (and modified) from basic typing game

            if e.type == P.KEYDOWN: # if the user has pressed a key
                #user wants to leave this place
                if e.key== P.K_ESCAPE:
                    P.mixer.music.stop()
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
                                line_color = (0,255,0) # green
                                line_counter = 0;
                                current_letters.remove(character)
                                score += 10
                                is_in_band = True
                                break
                    if not is_in_band: # deduct 5 points if there is no matching letter within the band
                        line_color = (255,0,0) # red
                        line_counter = 0;
                        if score - 1 >= 0:
                            score -= 1
                        else:
                            score = 0
                #special non-ESC character entered, deduct points for mistyping
                else:
                    if score - 1 >= 0:
                        score -= 1
                    else:
                        score = 0


        #deduct points for letters than have fallen below range
        for x in current_letters:
            if (x.pos_y > band_pos + band_range):
                if score >= 5:
                    score -= 5
                else:
                    score = 0
        #only consider letters that did not fall below band
        updated_list = [x for x in current_letters if
            (x.pos_y <= band_pos + band_range)]
        current_letters = updated_list



        #add all letters with updated positons to thingsToDraw
        for i in range(len(current_letters)):
            update_position(current_letters[i])
            current_letters[i].set_label()
            thingsToDraw.append((current_letters[i].get_label(),
                    current_letters[i].position))

        draw_list(thingsToDraw)
        P.draw.line(screen,line_color,(0,band_pos),(G.D_WIDTH,band_pos),4)
        P.display.update()
        thingsToDraw = []
