import random

def draw_letters():
    LETTER_POOL = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1
    }

    hand_letters = []
    letters = list(LETTER_POOL.keys())
    
    while len(hand_letters) < 10:
        letter = random.choice(letters)
        if LETTER_POOL[letter] > 0:
            LETTER_POOL[letter] -= 1
            hand_letters.append(letter)
    return hand_letters

def uses_available_letters(word, letter_bank):
    copy_letter_bank = letter_bank[:]

    for letter in word.upper():
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            return False
        
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass