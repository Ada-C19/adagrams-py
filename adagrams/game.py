from random import choice

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
    # build the pool of letters as a list with all 
    # the letters the appropriate number of times
    all_letters = []
    for key, value in LETTER_POOL.items():
        for i in range(value):
            all_letters.append(key)

    # build the hand
    hand = []
    for i in range(10):
        random_letter = choice(all_letters)
        # add the letter to the hand
        hand.append(random_letter)
        # make sure if it was the 1 z it cant be selected again
        all_letters.remove(random_letter)

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass