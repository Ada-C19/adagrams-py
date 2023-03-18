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
    

# Helper functions
def count_letter_frequency(sequence):
    letter_frequency = {}
    for letter in sequence:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    
    return letter_frequency


def convert_case(sequence):
    converted_sequence = ""
    for letter in sequence:
        converted_sequence += letter.casefold()
    
    return converted_sequence


def uses_available_letters(word, letter_bank):
    # Convert case on the word string and the letter bank list
    word = convert_case(word)
    letter_bank = convert_case(letter_bank)
    # Iterate through the letters in the word to check if they're in the letter bank
    for letter in word:
        if letter not in letter_bank:
            return False
    # Check how many times a letter occurs in the word and letter bank
    frequency_word = count_letter_frequency(word)
    frequency_bank = count_letter_frequency(letter_bank)
    # Compare the word frequency in the word and letter bank
    for letter in word:
        if not (frequency_word[letter] <= frequency_bank[letter]):
            return False  
    
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

hand = draw_letters()
# print(hand)
print(uses_available_letters("Dog", ["d", 'O', "g", "A", "t"]))
# print(convert_case("Dog", ["d", 'O', "g", "A", "t"]))