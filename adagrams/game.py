"""adagrams: it's really scrabble"""

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
    """Take word input and compare to letter bank."""
    letter_bank_copy = letter_bank.copy()
    letter_bank_case = [element.upper() for element in letter_bank_copy]

    for letter in word.upper():
        letter.upper()
        if letter in letter_bank_case:
            letter_bank_case.remove(letter)
        else:
            return False

    return True

def score_word(word):
    """Assign a point value to the input word"""
    letter_value = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
    }

    current_score = 0
    for letter in word:
        letter = letter.upper()
        for key, val in letter_value.items():
            if letter in val:
                current_score += key
    if 6 < len(word) < 10:
        current_score += 8

    return current_score

word_list = ['graze', 'ferment', 'add', 'sex', 'tenletters', 'branxzorfl']
def get_highest_word_score(word_list):
    """Return the highest scoring word as a tuple: ('string', word_score)"""
    # initiate empty dictionary
    word_score_dict = {}

    # for each word in the list, produce a score and assign
    # word/score to dictionary
    for word in word_list:
        score = score_word(word)
        print(f'word: {word}, score: {score}')
        word_score_dict.update({word: score})
    print(word_score_dict)

print(get_highest_word_score(word_list))
