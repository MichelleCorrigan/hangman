import random

animal_words = ["Alligator", "Bear", "Cheetah", "Deer"]


def get_word():
    """
    Chooses a word from the list randomly
    """
    word = random.choice(animal_words).upper()
    return word


def play_game(word):
    player = input("Enter your name: ").upper()
    print(f"Hello {player}! Let's play Hangman!\n ")
    guessed = False
    guessed_letters = []
    num_lives = 7
    # word_to_guess = "_" * len(word)
    
    while not guessed and num_lives > 0:
        for letter in word:
            if letter.upper() in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
    
        guess = input("Please guess a letter: ").upper()
        if guess in word:
            print(f"Correct!")
            guessed_letters.append(guess)
        elif guess not in word:
            print(f"Sorry! There is no {guess}.")
            guessed_letters.append(guess)
            print(f"Letters already guessed: {guessed_letters}")
            num_lives -= 1
            print(f"Lives left: {num_lives}")
            if num_lives == 0:
                print("No lives left. Game over!")
                break
        else:
            print("Incorrect input")


def main():
    """
    Run all program functions
    """
    word = get_word()
    play_game(word)
    # wrong_guesses()

print("Welcome to Hangman!")
main()
