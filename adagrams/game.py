import string
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
    hand = [] 
    while len(hand) < 10:
        letter = random.choice(string.ascii_letters).upper()
        count = hand.count(letter)
        if LETTER_POOL[letter] > count: 
            hand.append(letter)

    return hand

def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    for letter in uppercase_word:
        count_letter_bank = letter_bank.count(letter)
        count_word = uppercase_word.count(letter)
        if count_letter_bank == 0 or count_word > count_letter_bank:
            return False
    return True 

def score_word(word):
    score = 0
    for letter in word.upper():
        if letter in "AEIOULNRST":
            score += 1
        elif letter in "DG":
            score += 2
        elif letter in "BCMP":
            score += 3
        elif letter in "FHVWY":
            score += 4
        elif letter in "K":
            score += 5
        elif letter in "JX":
            score += 8
        elif letter in "QZ":
            score += 10

    if 6 < len(word) < 11:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    highest_word_score = []

    for word in word_list:
        if len(highest_word_score) == 0:
            highest_word_score.append(word)
            highest_word_score.append(score_word(word))
        elif score_word(word) == highest_word_score[1] and len(highest_word_score[0]) != 10:
            if len(word) == 10 or len(word) < len(highest_word_score[0]):
                highest_word_score[0] = word
                highest_word_score[1] = score_word(word)
        elif score_word(word) > highest_word_score[1]:
            highest_word_score[0] = word
            highest_word_score[1] = score_word(word)
        
    return tuple(highest_word_score)