import string
import random
LETTERS_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LETTERS_MAX_ALLOWED = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
def draw_letters():
    hand = []
    random_letter = ""
    letters_alphabet = LETTERS_ALPHABET
    cant_letter = 0
        
    while len(hand) < 10:
        random_letter = random.choice(list(letters_alphabet))
        for i in range(len(letters_alphabet)):
            if letters_alphabet[i] == random_letter and cant_letter < LETTERS_MAX_ALLOWED[i]:
                hand.append(random_letter)
                cant_letter += 1

    return hand

    for i in range(10):
        random_letter = random_letter()
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass