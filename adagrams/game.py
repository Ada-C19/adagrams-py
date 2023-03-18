import random
import string


def draw_letters():
    LETTER_POOL = ETTER_POOL = {
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
    hand = []
    count_frequency = {}
    for letter in LETTER_POOL:
        count_frequency[letter] = 0
        
    i = 0
    while i < 10:
        letter = random.choice(string.ascii_letters).capitalize()
        if count_frequency[letter] < LETTER_POOL[letter]:
            hand.append(letter)
            count_frequency[letter] += 1
            i += 1
        else:
            continue
    return hand 
    

def uses_available_letters(word, letter_bank):
    word_dict = {}
    letter_bank_dict = {}
    for letter in word:
        letter = letter.capitalize()
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
            
    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1
        else:
            letter_bank_dict[letter] = 1
            
    for key in word_dict:
        if key in letter_bank_dict and word_dict[key] <= letter_bank_dict[key]:
            continue 
        return False
    return True 
            
def score_word(word):
    word_score = {
        ('A','E','I','O','U','L','N','R','S','T'):1,
        ('D','G'):2,
        ('B','C','M','P'):3,
        ('F','H','V','W','Y'):4,
        ('K'):5,
        ('J','X'):8,
        ('Q','Z'):10
    }
    total_score = 0
    if word == "":
        total_score = 0
    for letter in word:
        for key in word_score:
            if letter.capitalize() in list(key):
                total_score += word_score[key] 
    if len(word) >= 7:
        total_score += 8
    return total_score               

def get_highest_word_score(word_list):
    pass