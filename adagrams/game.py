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
    hand_of_letters = []
    
    while len(hand_of_letters) <= 9:
        letter = random.choice(list(LETTER_POOL))
        if hand_of_letters.count(letter) < LETTER_POOL[letter]:
            hand_of_letters.append(letter)
        if len(hand_of_letters) >= 10:
            break
    
    return hand_of_letters

def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()

    for letter in uppercase_word:
        for item in letter_bank:
            if letter in letter_bank:
                continue
            if letter not in letter_bank:
                return False
    
    return True
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass






