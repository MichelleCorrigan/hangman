# HANGMAN

Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku

<p>
<img src="/workspace/hangman/screen-mockup.png" alt="Screens mockup">
<p>

## How to play

Hangman is an electronic version of the classic pen-and-paper game. You can discover more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

The player is asked to enter their name, then a random word is generated with dashes representing each letter. Players try to guess the letters in the word. If they guess all the letters correctly, they win. If too many letters which do not appear in the word are guessed, the player is hanged (and loses).

## Features

### Existing Features

- Random word generation
- Play against the computer
- Accepts user input

<p>
<img src="/workspace/hangman/feature1.png" alt="User input features">
<p>

- Maintains scores
- Displays a visual for each life lost
- Input validation and error-checking
  - You must enter a single letter
  - You cannot enter the same guess twice 

<p>
<img src="/workspace/hangman/features2.png" alt="Score feature">
<p>

### Future Features

- Include multiple word lists such as 'Movies', 'Music', 'Cars', etc so the player can choose which subject their random word is generated from.


## Testing

I tested the project in the following ways:
- Passed the code through the PEP8 linter and confirmed there are no problems
- Tested invalid inputs; more than one letter at a time, same input twice, any input other than a letter
- Tested in my local terminal and the Code Institute Heroku terminal

### Bugs

#### Solved Bugs

- When I was testing the code and entering the correct guess it wasn't updating in the `word_to_guess`. I fixed this by adding `.upper` when generating the random word in the `get_word` function
- When I ran the code in the PEP8 linter there was a `continuation line under-indented for visual indent` error on many lines. This was mainly in the `display_hangman` function and I fixed it by lining up the code underneath their opening brackets.

#### Remaining Bugs

- Each time the number of `Lives left: ` is printed, `None` is also printed underneath

### Validator Testing

- PEP8
  - No errors were returned from PEP8online.com


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku

- Steps for deployment:
  - Create a new Heroku app
  - In Settings, add a *Config Var*, using the key `PORT` and the value `8000` 
  - Set the buildbacks to `Python` and `NodeJS` in that order
  - In the Deploy section, select `Github`
  - Link the Heroku app to the repository
  - Click on **Deploy**

  ## Credits

  - Code Institute for the deployment terminal
  - Wikipedia for information on the Hangman game
  - Tutorial video by Kite [YouTube](https://youtu.be/m4nEnsavl6w) and by NeuralNine [YouTube](https://youtu.be/5x6iAKdJB6U)
  - Animal word list from Chegg.com on [Pinterest](https://www.pinterest.ie/)