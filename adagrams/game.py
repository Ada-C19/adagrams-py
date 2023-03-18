
import random
from random import choices

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

def build_pile_of_letters(dictionary):
    pile = []
    if dictionary == []:
        return None
    for x,y in dictionary.items():
        for i in range(0,y):
            pile.append(x)
    return pile

def draw_letters():
    hand = random.sample(build_pile_of_letters(LETTER_POOL),10)
    return hand

def uses_available_letters(word, letter_bank):
    new_bank = list(letter_bank)
    remainders = list(word.upper())
    print(remainders)
    
    for i in word.upper(): 
        if i in new_bank:
            remainders.remove(i)
            new_bank.remove(i)

    if remainders == []:
        return True
    else: 
        return False


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

