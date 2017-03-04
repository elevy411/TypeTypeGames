1. All the relevant code is in this folder

2. The unit tests can be found in unitTests branch. Slight modifications were made I beleive to some of the tests. 

3. There is no makefile for python

4. 
	i) compiling the code: 
		- make sure that pygame is installed on the machine (pip install pygame)
		- git clone https://github.com/elevy411/TypeTypeGames.git
		- All the relevant code for this is in master branch
		- make sure in the folder with the code
		- run python XXXX.py where XXXX is whatever you are trying to do (test or game)
		- to play the game, just run python game.py

	ii) To run the unit tests, just run them with python testXXXX.py 
			-note: some of them will fail because of time constraints and
			certain test conditions that are being tested for that might not have taken
			into account recent design decisions. Additionally, some file modification
			is neccesary for testGlobals because it assumes a specific wordlist in
			wordList.txt

	iii) To test this code, you can play all the games! Each game was made from a different pairing and has its own faults/pitfalls. Most of the games basic ideas were put into code, but some are definitely not in "full-game" mode yet. This should be fixed by the final code commit for next week. 

	When changing difficulty, the difficulty will print to the command line so you know what difficulty setting you are on.

	Easy = 1:00 min game time
	Medium = 0:30 game time
	Hard = 0:15 game time
	
	Difficulty changes other factors of the games too. For Falling Words for instance, it increases speed and score.
	
5.  i) Nearly everything that was promised in the original proposal has been implemented in some form or the other. By the nature of being creative and splitting into groups, each group had free creative reign over their game. Thus, the original proposal may not match the games perfectly. Most are very similar though. 

The only thing that was not finished in time for this milestone was the credits and highscore tracking.

6.  	Hadi and Gera paired
	Leeho and Rohin Paired
	Michelle and Elliot paired
	Wesley and Cole paired

	This second iteration was when we split into groups and did our own games. 
		Elliot and Michelle - Falling Words: Michelle and Elliot polished up the overall structure of the game and made falling words game. The game is almost 100% implemented and some of the features that might be added by final release includes sounds and high scores.

		Cole and Wesley - Type Type Revolutoin: Cole and Wesley were responsible for type type revolution. They implemented the entirety on their own, and implemented their own design choices. 
		
		Hadi and Gera - Type Type Wars: Hadi and Gera did Type Wars. The game is not yet perfect, but has all the aspects neccesary to finish up.
		Leeho and Rohin - Type Vs Monsters: Leeho and Rohin finished type type monsters and made the game. It too is very close to completion, just needs a little polishing.
		
7. Changes: Mainly small class changes were made (like splitting classes up/ name changes etc.). Additionally the games are slightly different than originally proposed. 

8. Nothing else really for the TA to know
