import game
import Globals as G
import word 
import letter
import typeTypeRevolution as ttr
import pygame

#get_position tested in Word and Letter previously

def test_update_position(test_letter):
    #update_position will be dependent on the difficulty
    #will be called each cycle before rendering
    #assuming default speed of 2 at framerate of 30
    G.set_difficulty_medium()
    for i in range(50):
    	assert test_letter.position == (G.TOP_CENTER[0],G.TOP_CENTER[1]+1*i),"update position fails at medium"
        ttr.update_position(test_letter)
    test_letter.set_position(G.TOP_CENTER[0],G.TOP_CENTER[1])
    G.set_difficulty_hard()
    for i in range(50):
    	assert test_letter.position == (G.TOP_CENTER[0],G.TOP_CENTER[1]+2*i),"update position fails at hard"
        ttr.update_position(test_letter)
    print "test_update_position passes"
    return None


def test_velocity(test_letter):
    G.set_difficulty_medium()
    ttr.reset_velocity()
    assert ttr.base_velocity == 1, "velocity not set correctly at medium"
    G.  set_difficulty_hard()
    ttr.reset_velocity()
    assert ttr.base_velocity == 2, "velocity not set correctly at hard"
    print "test_velocity passes"
    return None

def test_within_range(test_letter):
    #will have a tuple in TTR that represents the boundaries of our band
    band_pos = ttr.band_pos
    band_range = ttr.band_range
    assert not ttr.within_range(test_letter), "erroneously considers test_letter in range"
    while(test_letter.pos_y > G.D_HEIGHT):
        if (test_letter.pos_y > band_pos + band_range or test_letter.posy < band_pos - band_range):
            assert not ttr.within_range(test_letter), "erroneously considers test_letter in range"
        else:
             assert ttr.within_range(test_letter), "erroneously considers test_letter not in range"
    print "test_within_range passes"
    return None
    
    
test_letter = letter.Letter('a', G.WHITE) #Letter constuctor based on pygame Font which takes in (text,color,font,size,(posx,posy))
test_letter.set_position(G.TOP_CENTER[0],G.TOP_CENTER[1])
test_update_position(test_letter)
test_velocity(test_letter)
test_within_range(test_letter)
