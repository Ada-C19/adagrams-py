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
    # assign empty array to variable hand
    hand = []
    letter_freq = {}
    # create a for loop to iterate 10 times
    while len(hand) < 10:
        # get random letter from letter pool
        random_letter = random.choice(list(LETTER_POOL.keys()))
        # conditional to check that letter frequency does not exceed number in pool
        if random_letter in letter_freq:
            letter_freq[random_letter] += 1
        elif not random_letter in letter_freq:
            letter_freq[random_letter] = 1

        # append letter to hand list
        if letter_freq[random_letter] < LETTER_POOL[random_letter]:
            hand.append(random_letter)

    # return list
    return hand


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass