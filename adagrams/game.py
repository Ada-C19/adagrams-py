
# Import string and random module
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
    'Z': 1}

LETTER_SCORE = {
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
    'Z': 10}


def draw_letters():
    letter_pool_list = []
    output_letter_list = []
    for key, value in LETTER_POOL.items():
        for i in range(value):
            letter_pool_list.append(key)
    
    for i in range(10):
        output_letter = random.choice(letter_pool_list)
        letter_pool_list.remove(output_letter)
        output_letter_list.append(output_letter)

    return output_letter_list



def uses_available_letters(word, letter_bank):
    copy_of_letter_bank =[]
    for each in letter_bank:
        copy_of_letter_bank.append(each)

    for char in word:
        upper_char = char.upper()
        if upper_char not in copy_of_letter_bank:
            return False
        if upper_char in copy_of_letter_bank:
            copy_of_letter_bank.remove(upper_char)
    
    return True
            


def score_word(word):
    sum_of_word = 0

    for char in word:
        upper_char = char.upper()
        value = LETTER_SCORE[upper_char]
        sum_of_word += value
    
    if len(word) >= 7 and len(word) <= 10:
        sum_of_word += 8

    return sum_of_word

def get_highest_word_score(word_list):
    highest_score = 0
    highest_word = []

    for each in word_list:
        score = score_word(each)
        if score > highest_score:
            highest_score = score
            highest_word = [each]
        elif score == highest_score:
            highest_word.append(each)

    if len(highest_word) == 1:
        return (highest_word[0], highest_score)

    least_len = 10000000
    least_len_word =[]
    for each in highest_word:
        len_of_word = len(each)
        if len_of_word == 10:
            return (each, highest_score)
        if len_of_word < least_len:
            least_len = len_of_word
            least_len_word =[each]
        elif len_of_word == least_len:
            least_len_word.append(each) 
        
    return (least_len_word[0], highest_score)
