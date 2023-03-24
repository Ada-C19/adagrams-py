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

MAX_LETTERS = 10

def draw_letters():
    letter_tiles = []
    print(f"{letter_tiles = }")
    hand = []
    print(f"{hand = }")
    # converts letter bank to a list containing all available tiles
    for k, v in LETTER_POOL.items():
        for item in range(0,v):
            letter_tiles.append(k)
    # print(f"{letter_tiles = }")
    
    # Draw Ten
    for i in range(MAX_LETTERS):
        random_index = (random.randrange(len(letter_tiles)))
        hand.append(letter_tiles[random_index])
        letter_tiles.pop(random_index)
        
    # print(f"{random_index =}")
    # print(f"appended {hand = }")
    # print(f"tiles removed {letter_tiles = }")
    # print(f"{hand = }")
    return hand

def uses_available_letters(word, letter_bank):
    # check uppercase
    # check if letter is in letter_bank (copied to not modify original)
    # remove letters used in word from letter_bank
    letter_bank_copy = []
    letter_bank_copy.extend(letter_bank)
    for letter in word.upper():
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    # print(f"{letter_bank_copy = }")
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass