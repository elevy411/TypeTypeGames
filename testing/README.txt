1. All the relevant code is in this folder

2. The unit tests have been merged into this branch as well (from unitTests) with VERY slight additions in globalTest. 

3. There is no makefile for python

4. 
	i) compiling the code: 
		- make sure that pygame is installed on the machine (pip install pygame)
		- git clone https://github.com/elevy411/TypeTypeGames.git
		- All the relevant code for this is in basicTyping branch
		- make sure in the folder with the code
		- run python XXXX.py where XXXX is whatever you are trying to do (test or game)
		- to play the game, just run python game.py

	ii) To run the unit tests, just run them with python testXXXX.py 
			-note: some of them will fail because of time constraints and
			certain test conditions that are being tested for that might not have taken
			into account recent design decisions. Additionally, some file modification
			is neccesary for testGlobals because it assumes a specific wordlist in
			wordList.txt

	iii) To test this code, you should play the game! I encourage you to try out all the various
	things available at the moment. Operate the screen with either mouse or keyboard controls. (up and down). You can currently change the settings (change difficulty = how much time the game runs) or you can play the game. the ESC key will quit the game when you start it and return you back to the main menu. Otherwise its pretty self explanatory. 

	When changing difficulty, the difficulty will print to the command line so you know what difficulty setting you are on.

	Easy = 1:00 min game time
	Medium = 0:30 game time
	Hard = 0:15 game time


	Expected output: When you type letters that are correct, they should show up green, wrong letters will show up red. The enter key will clear the current word. Typing past a word will switch to the next word. Most keys should be disabled. 

	Correct letters = 10 points each
	Correct word = 30 points
	Wrong letter = -10 points
	Backspace = -10 points

	You can mess around with the wordList but I would be careful making it too small at the moment because not all of the winning/losing conditions have been set equally (due to time constraints)

5.  i) Nearly everything that was promised in the Milestone 2 write up has been coded. The only that hasnt been implemented is a true difficulty and the ability to choose the other games (trivial to make the screens change but nothing is there yet). 

	The basic classes that will be used through all the games are implemented 
	- Word
	- Letter
	- GameMenu
	- menuItem
	- game
	- Globals

6.  Hadi and Gera paired
	Leeho and Rohin Paired
	Michelle and Elliot paired
	Wesley and Cole paired

	This first iteration was mainly a chance for all of us to become familiar with the code in various ways for the future iteration and for our individual games. As for who did what specific part:
		Elliot and Michelle: Elliot managed the overall structure of all of the code, making sure that parts implemented by the other group memebers. He did a very large portion of the initial coding to get the group up to speed, but various small aspects were modified by the other group members. Michelle did a lot of work in making sure the basic typing logic was correct and that the images on the screen matched what we wanted. Additionaly she figured out the spacing issues. 

		Cole and Wesley: Main work was done in starting the implementation of speed (not in this iteration). Also helped in debugging the menu logic. (A good portion of UI update will occur as soon as this deadline passes as Wesley made some nice changes). They also made large contributions in the testing part of the iteration.

		Hadi and Gera: Since Hadi and Gera had less python experience, they were responsible for most of the testing in the early part of the iteration.  