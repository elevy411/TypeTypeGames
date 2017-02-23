import game
import Globals as G
import Word 
import Letter
import typeTypeRevolution as ttr

#get_position tested in Word and Letter previously

def test_update_position(tword):
    #update_position will be dependent on the difficulty
    #will be called each cycle before rendering
    #assuming default speed of 2 at framerate of 30
    G.set_difficulty_medium()
    for i in range(200):
        ttr.update_position(tword)
        assert tword.position == (G.TOP_CENTER[0],G.TOP_CENTER[1]+2*i),"update position fails at medium"
    tword.set_position(G.TOP_CENTER[0],G.TOP_CENTER[1])
    #assuming default speed of 3 at framerate of 30
    G.set_difficulty_hard()
    for i in range(200):
        ttr.update_position(tword)
        assert tword.position == (G.TOP_CENTER[0],G.TOP_CENTER[1]+4*i),"update position fails at medium"
    print "test_update_position passes"
    return None


def test_velocity(tword):
    G.set_difficulty_medium()
    ttr.reset_velocity()
    assert ttr.velocity = 2, "velocity not set correctly at medium"
    G.set_difficulty_hard()
    ttr.reset_velocity()
    assert ttr.velocity = 3, "velocity not set correctly at hard"
    print "test_velocity passes"
    return None

def test_within_range(tword):
    #will have a tuple in TTR that represents the boundaries of our band
    band_pos = ttr.band_pos
    band_range = ttr.band_range
    assert !ttr.within_range(tword), "erroneously considers tword in range"
    while(tword.pos_y > G.D_HEIGHT){
        if (tword.pos_y > band_pos + band_range or tword.posy < band_pos - band_range):
            assert !ttr.within_range(tword), "erroneously considers tword in range"
        else:
             assert ttr.within_range(tword), "erroneously considers tword not in range"
    print "test_within_range passes"
    return None
    
    
#also will iterate over collection of letters generated in the word
test_word = Word.create_word('This is a test')
test_word.set_position(G.TOP_CENTER[0],G.TOP_CENTER[1])
test_update_position(test_word)
test_velocity()
test_within_range(test_word)
