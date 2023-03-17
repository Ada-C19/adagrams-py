import random

def draw_letters():
    pool = {
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
    frequency_list = []
    for letter, frequency in pool.items():
        frequency_list += letter * frequency
    random_letter_list = []
    while len(random_letter_list) < 10:
        random_letter = random.choice(frequency_list)
        random_letter_list.append(random_letter)

    return random_letter_list

def frequency_maker(list):
    pass

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_frequency = {}
    for letter in word:
        if letter in letter_frequency.keys():
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1

        if letter not in letter_bank:
            return False
    
    for character in letter_bank:
        if character in letter_frequency.keys():
            if letter_frequency[character] != letter_bank.count(character):
                return False
    return True
        


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass