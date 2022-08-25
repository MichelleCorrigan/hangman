import random

animal_words = ["Alligator", "Bear", "Cheetah", "Deer"]


def get_word():
    """
    Chooses a word from the list randomly
    """
    word = random.choice(animal_words).upper()
    return word


def play_game(word):
    """
    Function prints a '_' for each letter in the random word choosen.
    Asks the player to input a guess, that can only contain one letter
    for each guess.
    Checks if the guess is in the random word.
    Counts down the number of lives left.
    Confirms if player has won or lost.
    """
    print("Try to guess the word:")
    word_to_guess = "_" * len(word)
    guessed = False
    guessed_letters = []
    num_lives = 7
    while not guessed and num_lives > 0:
        for letter in word:
            if letter.upper() in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
    
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed {guess}")
            elif guess not in word:
                print(f"Sorry! There is no {guess}.")
                guessed_letters.append(guess)
                print(f"Letters already guessed: {guessed_letters}")
                num_lives -= 1
                print(f"Lives left: {num_lives}")
                if num_lives == 0:
                    print("Game over!")
                    break
            else:
                print("Correct!")
                guessed_letters.append(guess)
                letters_in_word = list(word_to_guess)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    letters_in_word[index] = guess
                word_to_guess = "".join(letters_in_word)
                if "_" not in word_to_guess:
                    print(f"You win! The word was {word}!")
                    guessed = True
        else:
            print("Not a valid guess. Please enter a single letter.")


def play_loop():
    """
    Function asks if player wants to play again, if not, game ends.
    """
    response = input("\nPlay again? (Y/N): ").upper()
    print()

    if response == "Y":
        print("Great!\n")
        main()
    else:
        print("Thanks for playing!")


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



def main():
    """
    Run all program functions
    """
    word = get_word()
    play_game(word)
    play_loop()
    

print("Welcome to Hangman!")
player = input("Enter your name: ").upper()
print(f"Hello {player}! Let's play!\n ")
main()
