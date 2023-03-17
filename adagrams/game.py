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
    # Store the quantity of each letter in the pool and the count of each letter in these 2 lists
    counts = []
    letters = []
    # Get the letters and how many of each letter there are in the pool
    for letter, count in LETTER_POOL.items():
        letters.append(letter)
        counts.append(count)

    hand = random.sample(letters, counts=counts, k=10)

    return hand
    
# Helper function
def count_letter_frequency(sequence):
    letter_frequency = {}

    for letter in sequence:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    
    return letter_frequency


def uses_available_letters(word, letter_bank):
    
    letters = ["A", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
    word = "AAA"
    # Iterate through the letters in the word to check if they're in the letter bank
    for letter in word:
        if letter not in letter_bank:
            return False
    return True

    # Check how many times a letter occurs in the user input word and compare that against the letter_bank
    #if count_letter_frequency(word) 


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

