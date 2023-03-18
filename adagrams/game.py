import random

def draw_letters():
    letters_drawn = []
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

    i = 0
    while i < 10:
        random_letter = random.choice(list(LETTER_POOL.keys()))
        letter_count = letters_drawn.count(random_letter)
        if letter_count < LETTER_POOL[random_letter]:
            letters_drawn.append(random_letter)
            i += 1
        
    return letters_drawn


def uses_available_letters(word, letter_bank):
    word = word.upper()

    for letter in word:
        if letter not in letter_bank:
            return False
        elif not word.count(letter) <= letter_bank.count(letter):
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass