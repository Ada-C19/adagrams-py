
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

VALUE_SCORES = {
'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
'D': 2, 'G': 2,
'B': 3, 'C': 3, 'M': 3, 'P': 3,
'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
'K': 5,
'J': 8, 'X': 8,
'Q':10, 'Z':10
}


#WAVE 1
def draw_letters():
    drawn_letters = []
    available_letters = []

    for letter, num in LETTER_POOL.items():
        for i in range(num):
            available_letters.append(letter)
            
    while len(drawn_letters) < 10:
        randomly_draw_letter = random.choice(available_letters)
        available_letters.remove(randomly_draw_letter)
        drawn_letters.append(randomly_draw_letter)
        
    return drawn_letters

#WAVE 2
def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
        
    return True

#WAVE 3
def score_word(word):
    score = sum(VALUE_SCORES.get(letter.upper(), 0) for letter in word)
    if len(word) in [7, 8, 9, 10]:
        score += 8
    return score

def get_highest_word_score(word_list):
    pass