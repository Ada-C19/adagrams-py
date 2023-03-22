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

    letter_pool_copy_list = LETTER_POOL
    full_letter_bank_list = []
    my_letter_bank_list = []

    for letter in letter_pool_copy_list:
        while full_letter_bank_list.count(letter) < letter_pool_copy_list[letter]:
            full_letter_bank_list.append(letter)

    while len(my_letter_bank_list) < 10:
        random_letter = random.choice(full_letter_bank_list)
        my_letter_bank_list.append(random_letter)
        full_letter_bank_list.remove(random_letter)



    return my_letter_bank_list



def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if letter not in letter_bank or word.count(letter) > letter_bank.count(letter):
            return False
    return True
            
    
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass