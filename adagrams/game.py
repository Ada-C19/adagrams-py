# initializations
print("")
print("*** INITIALIZATIONS ***")

import random

LETTERS_TUPLE = ( {'A': 9,
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
                    'Z': 1}, )

letters_dict = LETTERS_TUPLE[0]
# print(f"letters_dict is {letters_dict}")

# helper functions

def make_letter_pool_list(letter_frequencies):
    letter_pool_list = []
    for letter in letter_frequencies:
        for i in range(letter_frequencies[letter]):
            letter_pool_list.append(letter)
    return letter_pool_list

# print(f"random number: {random.randint(0, 100)}")
# wave functions

def draw_letters():
    letter_pool = make_letter_pool_list(letters_dict)
    hand = []
    while len(hand) < 10:
        letter_selection = random.randint(0, len(letter_pool) - 1)
        hand.append(letter_pool[letter_selection])
        del letter_pool[letter_selection]
    return hand

def uses_available_letters(word, letter_bank):
    hand = list(letter_bank)
    word = word.upper()
    for letter in word:
        if letter not in hand:
            return False
        elif letter in hand:
            hand.remove(letter)
    return True

def score_word(word):
    score = 0
    for letter in word:
        score += LETTERS_TUPLE[0][letter]
    
    return score

def get_highest_word_score(word_list):
    pass

hand = draw_letters()
uses_available_letters('sandwich', hand)