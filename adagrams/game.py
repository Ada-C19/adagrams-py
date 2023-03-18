import random

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

    hand = []
    i = 0
    while i < 10:
        draw_random_letters = random.choice(list(LETTER_POOL.keys()))
        letter_count = hand.count(draw_random_letters)
        if letter_count < LETTER_POOL[draw_random_letters]:
            hand.append(draw_random_letters)
            i += 1
    return hand
   


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if letter not in letter_bank:
            return False
        elif word.count(letter) > letter_bank.count(letter):
            return False
    return True


def score_word(word):
    
    one_point = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    two_point = ["D", "G"]
    three_point = ["B", "C", "M", "P"]
    four_point = ["F", "H", "V", "W", "Y"]
    five_point = ["K"]
    eight_point = ["J", "X"]
    ten_point = ["Q", "Z"]

    total_score = 0
    for letter in word.upper():
        if letter in one_point:
            total_score += 1
        elif letter in two_point:
            total_score += 2
        elif letter in three_point:
            total_score += 3
        elif letter in four_point:
            total_score += 4
        elif letter in five_point:
            total_score += 5
        elif letter in eight_point:
            total_score += 8
        elif letter in ten_point:
            total_score += 10

    if len(word) >= 7:
        total_score += 8
    return total_score       

def get_highest_word_score(word_list):
    pass