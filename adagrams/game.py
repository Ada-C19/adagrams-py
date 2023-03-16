from random import choice

def draw_letters():
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
    MAX_LETTERS = 10
    letter_pool_list = []
    for letter in LETTER_POOL:
        temp = [letter] * LETTER_POOL[letter]
        letter_pool_list.extend(temp)
    
    letters = []
    for _ in range(MAX_LETTERS):
        rand_letter = choice(letter_pool_list)
        letters.append(rand_letter)
        letter_pool_list.remove(rand_letter)

    return letters


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

test = draw_letters()
print(test)