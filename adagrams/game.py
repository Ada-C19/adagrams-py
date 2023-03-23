# def draw_letters():
# def uses_available_letters(word, letter_bank):
# def score_word(word):
# def get_highest_word_score(word_list):

import random

# Function to draw random letters
def draw_letters():
    # Define the letter pool
    LETTER_POOL = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }
    
    # Create a list of letters based on their frequency in the letter pool
    letter_list = []
    for letter, count in LETTER_POOL.items():
        letter_list.extend([letter] * count)

    # Draw 10 random letters from the letter list
    hand = random.sample(letter_list, 10)
    
    # Return the hand
    return hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_copy = letter_bank.copy()

    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False

    return True

def score_word(word):
    word = word.upper()
    letter_scores = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    score = 0
    for letter in word:
        score += letter_scores[letter]

    if 7 <= len(word) <= 10:
        score += 8

    return score