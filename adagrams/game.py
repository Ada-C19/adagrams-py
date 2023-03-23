"""doc string"""

import random

LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}

def draw_letters():
    """Build a hand of 10 letters for the user"""
    letter_pool_copy = LETTER_POOL.copy()
    letters = []


    while len(letters) < 10:
        letter_key = random.choice(list(letter_pool_copy.keys()))

        if letter_pool_copy[letter_key] != 0:
            letter_pool_copy[letter_key] -= 1
            letters.append(letter_key)

    return letters


def uses_available_letters(word, letter_bank):
    """ doc string """
    pass

def score_word(word):
    """ doc string """
    pass

def get_highest_word_score(word_list):
    """ doc string """
    pass