import random
import copy

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

    drawn_letters = []
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    counter = 0
    
    while counter < 10: 
        letter, count = random.choice(list(letter_pool_copy.items()))
        print(letter, count)
        if count == 0:
            continue
        else:
            #decrement count by indexing the dictionary
            letter_pool_copy[letter] -= 1
            #add to drawn letters by calling it
            drawn_letters.append(str(letter))
            counter += 1
    
    return drawn_letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass