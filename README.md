# NOUGHTS AND CROSSES

Noughts and Crosses is a simple game where the play tries to connect 3 in a row. Either vertically, horizontally or even diagonally.
Game was designed on gitpod using Python and deployed to Heroku

![AmIResponsive](test-images/am-i-responsive.png)

## Launch the game [here:](https://noughts-and-crosses-pp3-29fe661c7fef.herokuapp.com/)

## Table of contents
 -  [User](#user)
    - [First time user](#first-time-user)

## User
  ### First time user
  - Play a simple game of noughts and crosses against the pc.
  - Step by step instructions on how to use it.
  - Rules to the game.
  - See your move on the board that will be printed as well as the pc move
  - Option to play again or quit.

## Features
 ### Name input
 Start of the game a message will appear with an input space to insert your player name.

 ![welcome-message](test-images/welcome-message-name.png)

 ### Print board and rules
 After inputting your name it will be printed along with a brief summary of how to play the game and the board will be printed waiting for you first move.

 ![rules-intro](test-images/rules-and-intro.png)

 ### Valid and Invalid inputs
 Invalid input numbers above 3.

 ![invalid-input](test-images/input-above-3.png)

 Invalid input spot already taken.

 ![invalid-input-1](test-images/input-spot-taken.png)

 Invalid input no space between the 2 given numbers.

 ![invalid-input-2](test-images/invalid-no-space.png)

 Valid input

 ![valid-input](test-images/correct-input-valid.png)

 ### Play again option
 Print win, loss or draw message and give the option to play again.

 ![game-over](test-images/play-again.png)

## Technologies used
- Python
- Github
- Gitpod
- Heroku
- Python Linter
- Black Playground

## Libraries used
- [Random](https://docs.python.org/3/library/random.html)
- [Colorama](https://pypi.org›project›colorama)

## Testing
Ran code through CI Python Linter, errors given were codes were to long, corrected them.

![python-linter](test-images/python-linter.png)