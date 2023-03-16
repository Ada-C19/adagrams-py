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

def draw_letters():
    ada_gram = LETTER_POOL
    letter_pool = []
    hand_as_list = []

    for k,v in ada_gram.items():
        for i in range(v):
            letter_pool.append(k)
    
    while len(hand_as_list) < 10:
        hand_as_list.append(random.choice(letter_pool))
    # print(hand_as_list)
    return hand_as_list

# draw_letters()

def uses_available_letters(word, letter_bank):
    # word is input string 
    # letter bank is list of words
    #letter_bank can have multiple of one letter, 
    # must remove letter at a time to account for multiple of same letter in bank
    for letter in word:
        if letter in letter_bank:
            letter_bank.remove(letter)
            return True
        else:
            return False
    

def score_word(word):
    # word is a string of characters
    # return integer represening the number of points
    # each letter within word has a point value. The number of points 
    # is summed up to represent the total score of word
    # ***if len of word is 7, 8, 9, or 10 then word gets additional 8 points

def get_highest_word_score(word_list):
    pass