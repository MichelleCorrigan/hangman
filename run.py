import random

animal_words = ["Alligator", "Bear", "Cheetah", "Deer"]
NUM_LIVES = 7

def get_word():
    """
    Chooses a word from the list randomly
    """
    word = random.choice(animal_words).upper()
    return word


def play_game(word, NUM_LIVES):
    """
    Function prints a '_' for each letter in the random word choosen.
    Asks the player to input a guess, that can only contain one letter
    for each guess.
    Checks if the guess is in the random word.
    Counts down the number of lives left.
    Confirms if player has won or lost.
    """
    print("Try to guess the word:\n")
    word_to_guess = "_" * len(word)
    guessed = False
    guessed_letters = []
    
    while not guessed and NUM_LIVES > 0:
        for letter in word:
            if letter.upper() in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
    
        guess = input("\nPlease guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed {guess}")
            elif guess not in word:
                print(f"\nSorry! There is no {guess}.")
                guessed_letters.append(guess)
                print(f"Letters already guessed: {guessed_letters}")
                NUM_LIVES -= 1
                print(f"Lives left: {NUM_LIVES}\n{display_hangman(NUM_LIVES)}")
                if NUM_LIVES == 0:
                    print(f"Game over! The word was {word}")
                    break
            else:
                print("Correct!\n")
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


def display_hangman(NUM_LIVES): 
    """
    Function to display stages of Hangman with each wrong answer.
    """           
    if (NUM_LIVES == 6):
        print("\n +====+"
            "\n |   |"
            "\n     |"
            "\n     |"
            "\n     |"
            "\nx=======x")
    elif (NUM_LIVES == 5):
        print("\n +====+"
            "\n |  |"
            "\n O  |"
            "\n    |"
            "\n    |"
            "\nx=======x")
    elif (NUM_LIVES == 4):
        print("\n +====+"
            "\n |  |"
            "\n O  |"
            "\n |  |"
            "\n    |"
            "\nx=======x")
    elif (NUM_LIVES == 3):
        print("\n +====+"
            "\n |  |"
            "\n O  |"
            "\n/|  |"
            "\n    |"
            "\nx=======x")
    elif (NUM_LIVES == 2):
        print("\n +====+"
            "\n |  |"
            "\n O  |"
            "\n/|\ |"
            "\n    |"
            "\nx=======x")
    elif (NUM_LIVES == 1):
        print("\n +====+"
            "\n |  |"
            "\n O  |"
            "\n/|\ |"
            "\n/   |"
            "\nx=======x")
    elif (NUM_LIVES == 0):
        print("\n +====+"
            "\n |  |"
            "\n O  |"
            "\n/|\ |"
            "\n/ \ |"
            "\nx=======x")

    


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
        print("Thanks for playing!\n")


def main():
    """
    Run all program functions
    """
    word = get_word()
    play_game(word, NUM_LIVES)
    display_hangman(NUM_LIVES)
    play_loop()
    

print("\nWELCOME TO HANGMAN!\n")
player = input("Enter your name: ").upper()
print(f"\nHello {player}! Let's play!\n ")
main()
