import random
import string

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
    hand = []
    # Randomly choose 10 letters and add to the list
    while len(hand) < 10:
        random_letter = random.choice(string.ascii_uppercase)

        # Count the number of random_letter currently in hand
        count = 0
        for letter in hand:
            if letter == random_letter:
                count += 1
        
        # Add random_letter to hand if conditions met
        if count < LETTER_POOL[random_letter]:
            hand.append(random_letter)
        
    return hand

def uses_available_letters(word, letter_bank):
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass