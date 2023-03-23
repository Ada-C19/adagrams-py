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




