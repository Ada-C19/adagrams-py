import random
from collections import Counter
def draw_letters():
    letter_pool = {
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

    hand = random.sample(list(letter_pool.keys()), 10)
    return hand

def uses_available_letters(word, letter_bank):
    # Convert word to uppercase
    word = word.upper()
    # Create a counter of the letter_bank
    bank_counts = Counter(letter_bank)
    # Iterate over each letter in the word
    for letter in word:
        # If the letter is not in the bank_counts, or if the count is 0, return False
        if letter not in letter_bank or bank_counts[letter] == 0:
            return False
        # Otherwise, decrement the count of the letter in bank_counts
        bank_counts[letter] -= 1
    # If we make it through the loop without returning False, return True
    return True

def score_word(word):
    word = word.upper()
    score = 0
    for letter in word:
        if letter in "AEIOULNRST":
            score += 1
        elif letter in "DG":
            score += 2
        elif letter in "BCMP":
            score += 3
        elif letter in "FHVWY":
            score += 4
        elif letter == "K":
            score += 5
        elif letter in "JX":
            score += 8
        elif letter in "QZ":
            score += 10
    if len(word) >= 7:
        score += 8
    return score



def get_highest_word_score(word_list):
    pass