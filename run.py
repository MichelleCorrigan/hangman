import random

animal_words = ["Alligator", "Bear", "Cheetah", "Deer"]

def get_word():
    word = random.choice(animal_words)
    print(word)

get_word()