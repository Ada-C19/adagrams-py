import random

def draw_letters(LETTER_POOL):
    letter_list = list(LETTER_POOL.key())
    random_letter = random.choice(letter_list)
    print(random_letter)

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass