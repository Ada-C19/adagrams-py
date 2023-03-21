import random

def draw_letters():
    letter_pool = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1}
    hand = []
    for i in range(10):
        letters = list(letter_pool.keys())
        letter = random.choice(letters)
        while letter_pool[letter] == 0:
            letter = random.choice(letters)
        hand.append(letter)
        letter_pool[letter] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    
    letter_bank_copy = letter_bank[]
    
    
    word_lower = word.lower()
    letter_bank_lower = [letter.lower() for letter in letter_bank_copy]
    
    for letter in word_lower:
        if letter in letter_bank_lower:
            letter_bank_lower.remove(letter)
        else:
            return False
    return True






def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass