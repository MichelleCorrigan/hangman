import random

animal_words = ["Alligator", "Bear", "Cheetah", "Deer"]

def get_word():
    word = random.choice(animal_words)
    return word


def play_game(get_word):
    player = input("Enter your name: ").upper()
    print(f"Hello {player}! Let's play Hangman!\n ")
    guessed = False
    guessed_letters = []
    num_lives = 7
    word_to_guess = "_" * len(get_word())
    print(word_to_guess)
    guess = input("Please guess a letter: ").upper()
        if guess not in word_to_guess:
        print(f"Sorry! There is no {guess}.")
        num_lives -= 1
        print(f"Lives left: {num_lives}")
        print(input("Please guess again: ").upper())
        
    else:
        print(f"Correct! {guess} is in {word_to_guess}")
        


play_game(get_word)
    


# def letters_guessed():
#     num_lives = 7
#     if wrong_guesses < 7:
#         print("Try another guess")
#     else wrong_guesses >= 7:
#         print("No lives left. Game over!")


# def main():
#     """
#     Run all program functions
#     """
#     get_word()
#     play_game(word)



# print("Welcome to Hangman!")
