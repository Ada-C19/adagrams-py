import random

def draw_letters():
    # Letters to choose from
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

    ten_letters = [] # List for 10 random letters

    while len(ten_letters) < 10:
        letter_to_add = random.choice(list(LETTER_POOL))
        if LETTER_POOL.get(letter_to_add) > 0:
            ten_letters.append(letter_to_add)
            LETTER_POOL[letter_to_add] -= 1

    return ten_letters

def uses_available_letters(word, letter_bank):
    for letter in word:
        if not letter in letter_bank:
            return False
    
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass