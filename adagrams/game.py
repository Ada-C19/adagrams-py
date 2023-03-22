import random
import string

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
    ten_letters = []    
    while len(ten_letters) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        if LETTER_POOL[random_letter] > 0:
            LETTER_POOL[random_letter] -= 1
            ten_letters.append(random_letter)

    return ten_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]

    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

