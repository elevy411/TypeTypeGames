import sys
import pygame as P
from word import Word
from letter import Letter
import Globals as G
import TypeWars as T

#+all import statements necessary 


"""Series of tests for checking our implementation TypeTypeWars and Speed game
   
   player{
	 index          #indicates current position of player in prompt
	 counter        #time spent typing, tracked by pygames
	 health         #initialized as 100, for combat
	 
	 modifyHealth() #only negate health
	 modifyIndex()  #increase current index based on words typed 
   	 calculateWPM() #calculated WPM for player
   }"""

player1 = T.Player()
player2 = T.Player()
#tests health modification
def test_health_mod(): 
	#get health of player
	health = player1.health
	player1.modifyHealth(-1)
	assert health - 1 == player1.health

	player1.modifyHealth(-4)
	assert health - 5 == player1.health

	#once player loses more than 100 health, 0
	player1.modifyHealth(-96)
	assert 0 == player1.health

	#can't gain health, modifyHealth() only takes - ints
	player1.modifyHealth(20)
	assert 0 == player1.health

	print "modifyHealth test passed"


#tests WPM calculation
def test_WPM_calc():
	player1.modifyIndex(20)
	typed = player1.index
	player1.updateCounter(30)
	time_elapsed = player1.counter
	time_elapsed = float(time_elapsed) / 60
	WPM = player1.calculateWPM()

	assert WPM == typed / time_elapsed 
	print "calculateWPM test passed"


#tests if typical combat sequence works
def test_combat():
	player1.resetHealth()
	player2.resetHealth()
	player1.modifyIndex(20)
	index1 = player1.index
	player2.modifyIndex(30)
	index2 = player2.index
	diff1 = index1 - index2
	diff2 = index2 - index1
	health1 = player1.health
	health2 = player2.health

	#someone loses health
	player1.modifyHealth(diff1)
	player2.modifyHealth(diff2)

	if diff1 < 0:
		assert health1 + diff1 == player1.health
		print "combat test passed"
	if diff2 < 0:
		assert health2 + diff2 == player2.health
		print "combat test passed"

#tests if index modification works
def test_index():
	typed = player1.index

	player1.modifyIndex(10)
	assert typed + 10 == player1.index

	player1.modifyIndex(100)
	assert typed + 110 == player1.index
	print "modifyIndex test passed"


test_health_mod()
test_WPM_calc()
test_combat()
test_index()