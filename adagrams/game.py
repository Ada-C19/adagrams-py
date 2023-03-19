import random
from random import shuffle

def draw_letters():
    letters_pool = {
        "A" : 9,
        "B" : 2,
        "C" : 2,
        "D" : 4,
        "E" : 12,
        "F" : 2,
        "G" : 3,
        "H" : 2,
        "I" : 9,
        "J" : 1,
        "K" : 1,
        "L" : 4,
        "M" : 2,
        "N" : 6,
        "O" : 8,
        "P" : 2,
        "Q" : 1,
        "R" : 6,
        "S" : 4,
        "T" : 6,
        "U" : 4,
        "V" : 2,
        "W" : 2,
        "X" : 1,
        "Y" : 2,
        "Z" : 1
    }
# append letters into list
    letters_pool_list = []
    i = 0
    for key, value in letters_pool.items():
        while i < value:
            letters_pool_list.append(key)
            i += 1
        i = 0                                   # reset counter
        continue
    letters_pool_list = random.sample(letters_pool_list, len(letters_pool_list))            #shuffle the pool list
    return(letters_pool_list[:10])               # user draw 10 letters



def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass