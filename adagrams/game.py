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
    letters = []
    letter_pool_counter = LETTER_POOL.copy()
    while len(letters) < 10:
        # choose random letter from LETTER_POOL
        random_letter = random.choice(list(LETTER_POOL.keys()))
        
        # verify letter_pool_counter[random_letter] is not 0,
        # decrement dict and append list
        if letter_pool_counter[random_letter]:
            letter_pool_counter[random_letter] -= 1
            letters += random_letter
        # random_letter empty, start over.  
        else:
            continue

    return letters


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass