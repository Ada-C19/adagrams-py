import random

import copy

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
    hand_of_letters = []                             # 1
    
    # syntax: new_list = copy.deepcopy(old_list)
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    
    while len(hand_of_letters) < 10:                            # 3, # 4- 5, # P2 - 5
        letter_dict_keys = list(LETTER_POOL.keys())
        weight_values_list = list(LETTER_POOL.values())
        random_letter = random.choices(letter_dict_keys, weights = weight_values_list, k=1)[0]
                
        if letter_pool_copy[random_letter] > 0:
            hand_of_letters.append(random_letter)
            
            letter_pool_copy[random_letter] -= 1
            
    return hand_of_letters

# draw_letter``s()


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
