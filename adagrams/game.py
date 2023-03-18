
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
    for x,y in dictionary.items():
        for i in range(0,y):
            pile.append(x)
    return pile

def draw_letters():
    hand = random.sample(build_pile_of_letters(LETTER_POOL),10)
    print(hand)
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

"""
def build_probabilities_of_ocurrence(dictionary):
    total_letters = 0
    probability_dictionary = {}
    
    if dictionary == {}:
        return None
    else: 
        for i in dictionary.values():
            total_letters += i
    
        for i,j in dictionary.items():
            probability_dictionary[i]=j/total_letters
    
    return probability_dictionary

def draw_letters():
    probabilities = build_probabilities_of_ocurrence(LETTER_POOL)
    weights = list(probabilities.values())
    population = list(probabilities.keys())
    
    hand = choices(population,weights,k = 10)
    print(hand)

    return hand
"""
    
#build_probabilities_of_ocurrence(LETTER_POOL)
#draw_letters()
#pruebachoices()
#build_pile_of_letters(LETTER_POOL)
