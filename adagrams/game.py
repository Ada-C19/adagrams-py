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
    """
    Returns the player's "hand", an array of ten strings, each containing only one letter
    Letters are randomly drawn from a pool of letters without replacement. 
    Calling this function does not mutate LETTER_POOL
    """
    copy_pool = dict(LETTER_POOL)
    letters = list(copy_pool.keys())
    weights = list(copy_pool.values())

    hand = []

    while int(len(hand)) < 10:
        # Selects a random letter with consideration for weight
        # draw is a list containing 1 letter
        draw = random.choices(letters, weights=weights, k=1)
        l = draw[0]
        idx = letters.index(l)
        #
        if weights[idx] == 0:
            continue
        else:
            hand.append(l)
            weights[idx] -= 1

    return hand





def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass