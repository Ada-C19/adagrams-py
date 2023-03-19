import random

def draw_letters():
    
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
    letters = ''
    
    for letter, count in LETTER_POOL.items():
        letters += ''.join(letter*count)
    
    letter_bank = random.choices(letters, k=10)
    
    return letter_bank

def uses_available_letters(word, letter_bank):
    
    if len(word) > len(letter_bank) or not word.isalpha():
        return False
    
    for letter in word.upper().strip():
        if letter not in letter_bank:
            return False
        else:
            letter_bank.remove(letter)

    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass