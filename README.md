Welcome to Type Type Games!

Installation:
- git clone https://github.com/elevy411/TypeTypeGames.git
- All the files should be set up as you need them, all you should have to run is make from the main folder.
- All the makefile is doing, is pip installing the various packages necessary. If the make file does not work, simply do the following:
    - (sudo?) pip install psutil
    - (sudo?) pip install pygame
    - (sudo?) pip install wheel

- After that, everything needed to play or test the game should be installed!


Functionality Description:

Type Type games is a collection of a variety of typing games designed to be fun time killers. Each game has slightly different goals but the same basic premise: typing!

To play the game: Run the command "./run" from the terminal in the main folder that you downloaded (from git).

You will now be at a main menu where you can pick from a variety of games.

Use the Up and Down arrow keys and enter key on the keyboard or the mouse to select options.

-Settings: The settings menu has a difficulty option that will let you pick your difficulty. When you pick a difficulty, it will tell you in the terminal what difficulty you are at. The default is easy (1). The hardest is hard mode (5). 

Pressing Escape will take you back to the main menu from any game!

Basic Typing: This game is simply a game to test your basic typing skills! You will type as many words in the time alloted as possible, getting points for correct letters, and losing points for incorrect letters or backspacing. You can press "enter" to clear the word to avoid backspacing. Each correct word gives you an additional set of points. Easy, Medium, and Hard difficulties change how long is on the timer for typing. 

Falling Words: This game tests your ability to keep track of a variety of words as they fall from the top of the screen. Type them before they hit the bottom to get points! If too many hit the bottom, you lose! The more you type, the faster and harder the game gets. Press "enter" to clear the word you are currently typing. Difficulty changes the speed and point values of the words!

Type Wars: This game is designed to be played against someone else. Similar to the basic typing game, the goal of this game is to type as fast as possible while also making the fewest number of mistakes! If you make too many, you lose health and lose. The game continues until one player loses all their life. The person who types more words reduces that number from the other players health every round. 

Type Type Revolution: Similar to games like guitar hero, the goal of this game is to press the correct key when the letter crosses the thick white line at the bottom of the screen! Try to accumulate the highest score possible!

Type Vs Monster: This game plays similar to falling words, but the words come from the outside to the center of the screen. You want to type the words before they hit the center. The difference in this game though, is that letters will be taken from the front of all words on screen! So you can kill multiple words simultaneously with enough skill. Play till time runs out or you get hit by a word!



Some Bugs that may occur:
- Occsaionally, the game will have an IO error depending on conditions such as loss/win and then continuation. Simply restart the game and keep playing! 
- Inputs on your keyboard that might mess up the game are keyboard inputs that would mess up most any application (the F keys etc.). Every other key should behave normally or not do anything bad to the game. 





