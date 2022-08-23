import random

animal_words = ["Alligator", "Bear", "Cheetah", "Deer"]

def get_word():
    word = random.choice(animal_words)
    return word


def play_game(word):
    player = input("Enter your name: ")
    print(f"Hello {player}! Let's play Hangman!\n ")
    word_to_guess = "_" * len(word)
    print(word_to_guess)
    guess = input("Please guess a letter: ")
    guessed = False
    guessed_letters = []
    num_lives = 7


# def letters_guessed():
#     num_lives = 7
#     if wrong_guesses < 7:
#         print("Try another guess")
#     else wrong_guesses >= 7:
#         print("No lives left. Game over!")


def main():
    """
    Run all program functions
    """
    get_word()
    play_game(word)



print("Welcome to Hangman!")
