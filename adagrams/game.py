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

def is_letter_selected_too_much():
    letters = draw_letters()

    letter_freq = {}
    for letter in letters:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
    print("letters: ", letters)
    print("letter freq: ", letter_freq)

    for letter in letters:
        print("letter freq: ", letter, letter_freq[letter])
        print("letter pool: ", letter, LETTER_POOL[letter])
        return letter, letter_freq[letter] <= LETTER_POOL[letter], letter_freq[letter]


def draw_letters():   
    # Store the quantity of each letter in the pool in the weights list
    weights = []
    letters = []
    # Get the letters and how many of each letter there are in the pool
    for letter, weight in LETTER_POOL.items():
        letters.append(letter)
        weights.append(weight)

    hand = random.choices(letters, weights, k=10)
    print(hand)
    print(is_letter_selected_too_much())
        
    return hand
    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

print(draw_letters())