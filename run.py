import random

animal_words = ["Alligator", "Bear", "Cheetah", "Deer"]

def get_word():
    word = random.choice(animal_words)
    print(word)

get_word()


def letters_guessed():
    num_lives = 7
    if wrong_guesses < 7:
        print("Try another guess")
    else wrong_guesses >= 7:
        print("No lives left. Game over!")