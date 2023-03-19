import random
from random import shuffle
from collections import Counter

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
    letter_bank = letters_pool_list[:10]
    return(letter_bank)               # user draw 10 letters



def uses_available_letters(word, letter_bank):
    word = [elem.upper() for elem in word]     # convert input word to upper case
    '''    
    if len(word) > len(letter_bank):        # too much letter than letter_bank return F
        return False
    if set(word).issubset(set(letter_bank)) == False:  # if a letter is not in letter_bank return F
        return False
    else:
    '''
    word_count = Counter(word)
    bank_count = Counter(letter_bank)
    return all(word_count[i] <= bank_count[i] for i in word_count)

        


def score_word(word):
    score_chart = {
        "A" : 1,
        "E" : 1,
        "I" : 1,
        "O" : 1,
        "U" : 1,
        "L" : 1,
        "N" : 1,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3,
        "C" : 3,
        "M" : 3,
        "P" : 3,
        "F" : 4,
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8,
        "X" : 8,
        "Q" : 10,
        "Z" : 10
    }
    sum = 0
    word = [elem.upper() for elem in word]     # convert input word to upper case

    for letter in word:
        sum = sum + score_chart[letter]
    if len(word) >= 7:
        sum += 8
    return sum

def get_highest_word_score(word_list):
    pass