import random

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def get_new_letter_pool():
    '''
        Helper function to create pool of letters that will be used to create user's hand.
        This dictionary holds letters in respect to amount availability per letter. 
    '''
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
    return letter_pool

def draw_letters():
    letter_pool = get_new_letter_pool()
    hand = []

    # 10 letters needed in user hand, keep looping until 10 letters obtained
    while len(hand) < 10:
        # returns a list of randomly selected letters and 
        # selection is made with probability of each letter available in letter pool
        generate_letter = random.choices(list(letter_pool.keys()), weights = letter_pool.values(), k=1)[0] 
        hand.append(generate_letter)

        # checks that letters do not exceed available amount per letter
        if letter_pool[generate_letter] > 0:
            letter_pool[generate_letter] -= 1
        else:
            letter_pool.pop(generate_letter)

    return hand

def uses_available_letters(word, letter_bank):
    # change word to all uppercase to account for no case sensitivity
    uppercase_word = word.upper()

    for character in uppercase_word:
        count_character = uppercase_word.count(character)
        if character not in letter_bank or count_character > letter_bank.count(character):
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass