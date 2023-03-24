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
    hand = []
    for k, v in LETTER_POOL.items():
        for item in range(0,v):
            letter_tiles.append(k)
    
    
    # Draw Ten
    for i in range(MAX_LETTERS):
        random_index = (random.randrange(len(letter_tiles)))
        hand.append(letter_tiles[random_index])
        letter_tiles.pop(random_index)
        
    return hand

draw_letters()

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
    return True


def score_word(word):
    score = 0
    score_dict = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, 
                "L": 1, "N": 1, "R": 1, "S": 1, "T": 1, 
                "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, 
                "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, 
                "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10
                }
    
    for letter in word.upper():    
        score += score_dict[letter]
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    highest_word_score = 0 
    best_word = ""
    for word in word_list:
        score_total = score_word(word)

        if score_total > highest_word_score:
            highest_word_score = score_total
            best_word = word
        elif score_total == highest_word_score:
            if len(best_word) == 10:
                continue
            elif len(word) == 10:
                highest_word_score = score_total
                best_word = word
            elif len(word) < len(best_word):
                best_word = word
            
    return best_word, highest_word_score
