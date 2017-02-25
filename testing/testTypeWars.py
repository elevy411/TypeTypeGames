import sys
import pygame as P
from word import Word
from letter import Letter
import Globals as G

#+all import statements necessary 


"""Series of tests for checking our implementation TypeTypeWars and Speed game
   
   player{
	 index          #indicates current position of player in prompt
	 counter        #time spent typing, tracked by pygames
	 health         #initialized as 100, for combat
	 
	 modifyHealth() #only negate health
	 modifyIndex()  #increase current index based on words typed 
   }"""

#tests health modification
def test_health_mod(player): 
	#get health of player
	health = player.health
	player.modifyHealth(-1)
	assert health - 1 == player.health

	player.modifyHealth(-4)
	assert health - 5 == player.health

	#once player loses more than 100 health, 0
	player.modifyHealth(-96)
	assert 0 == player.health

	#can't gain health, modifyHealth() only takes - ints
	player.modifyHealth(20)
	assert 0 == player.health

#tests WPM calculation
def test_WPM_calc(player):
	typed = player.index
	time_elapsed = player.counter
	time_elapsed = time_elapsed / 60
	WPM = player.calculateWPM

	assert WPM == typed / time_elapsed 

#tests if typical combat sequence works
def test_combat(player1, player2):
	index1 = player1.index
	index2 = player2.index
	diff1 = index1 - index2
	diff2 = index2 - index1
	health1 = player1.health
	health2 = player2.health

	#someone loses health
	player1.modifyHealth(diff1)
	player2.modifyHealth(diff2)

	if diff1 < 0:
		assert health1 - diff1 = player1.health
	if diff2 < 0:
		assert health2 - diff2 == player2.health

#tests if index modification works
def test_index(player):
	typed = player.index

	player.modifyIndex(10)
	assert typed + 10 = player.index

	player.modifyIndex(100)
	assert typed + 110 = player.index









