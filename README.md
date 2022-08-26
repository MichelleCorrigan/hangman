# HANGMAN

Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku

<p>
<img src="vscode-remote://michellecorriga-hangman-kelgzbi7t95.ws-eu63.gitpod.io/workspace/hangman/screen-mockup.png" alt="Screens mockup">
<p>

## How to play

Hangman is an electronic version of the classic pen-and-paper game. You can discover more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))
The player is asked to enter their name, then a random word is generated with dashes representing each letter. Players try to guess the letters in the word. If they guess all the letters correctly, they win. If too many letters which do not appear in the word are guessed, the player is hanged (and loses).

## Features

### Existing Features

- Random word generation
- Play against the computer
- Accepts user input
- Maintains scores
- Displays a visual for each life lost
- Input validation and error-checking
  - You must enter a single letter
  - You cannot enter the same guess twice 

### Future Features

- Include multiple word lists such as 'Movies', 'Music', 'Cars', etc so the player can choose which subject their random word is generated from.


## Testing

I tested the project in the following ways:
- Passed the code through the PEP8 linter and confirmed there are no problems
- Tested invalid inputs; more than one letter at a time, same input twice, any input other than a letter
- Tested in my local terminal and the Code Institute Heroku terminal

### Bugs

#### Solved Bugs

- When I was testing the code and entering the correct guess it wasn't updating in the word_to_guess. I fixed this by adding `.upper`
