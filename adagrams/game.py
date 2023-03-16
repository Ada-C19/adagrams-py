import random as r

def make_letter_list():
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

    letter_list = []
    for letter, count in LETTER_POOL.items():
        for _ in range(count):
            letter_list.append(letter)

    return letter_list


def draw_letters():
    letter_list = make_letter_list()

    hand = []

    for _ in range(10):
        letter_index = r.randint(0, len(letter_list) - 1)
        hand.append(letter_list[letter_index])
        letter_list.pop(letter_index)

    return hand


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass