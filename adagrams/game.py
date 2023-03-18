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


def convert_case(word, letter_bank):
    converted_word = ""
    converted_letter_bank = []

    for letter in word:
        converted_word += letter.casefold()

    for letter in letter_bank:
        converted_letter_bank.append(letter.casefold())
    print(converted_word)
    print(converted_letter_bank)
    return converted_word, converted_letter_bank


def uses_available_letters(word, letter_bank):
    print(word)
    print(letter_bank)
    # word = word.upper()
    # Iterate through the letters in the word to check if they're in the letter bank
    for letter in word:
        if letter.upper() not in letter_bank:
            return False
    # Check how many times a letter occurs in the user input word and compare that against the letter_bank
    frequency_word = count_letter_frequency(word)
    frequency_bank = count_letter_frequency(letter_bank)
    print(frequency_word)
    print(frequency_bank)
    for letter in word:
        if not (frequency_word[letter.upper()] <= frequency_bank[letter.upper()]):
            print(f"{frequency_word[letter.upper()]} '<=' {frequency_bank[letter.upper()]}")
            return False  
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

# hand = draw_letters()
# print(hand)
print(uses_available_letters("Dog", ["d", 'O', "g", "A", "t"]))
print(convert_case("Dog", ["d", 'O', "g", "A", "t"]))