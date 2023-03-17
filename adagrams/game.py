import string
import random

def draw_letters():
    hand = []
    random_letter = ""
    for i in range(10):
        random_letter = random.choice(string.ascii_letters).upper()
        hand.append(random_letter)
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass