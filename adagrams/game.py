import random

letter_quant_dict = {
    "A" : 9,
    "B" : 2,
    "C" : 2,
    "D" : 4,
    "E" : 12,
    "F" : 2,
    "G" : 3,
    "H" : 2,
    "I" : 9,
    "J" : 1,
    "K" : 1,
    "L" : 4,
    "M" : 2,
    "N" : 6,
    "O" : 8,
    "P" : 2,
    "Q" : 1,
    "R" : 6,
    "S" : 4,
    "T" : 6,
    "U" : 4,
    "V" : 2,
    "W" : 2,
    "X" : 1,
    "Y" : 1,
    "Z" : 1
}

letter_score_dict = {
    "A" : 1,
    "B" : 3,
    "C" : 3,
    "D" : 2,
    "E" : 1,
    "F" : 4,
    "G" : 2,
    "H" : 4,
    "I" : 1,
    "J" : 8,
    "K" : 5,
    "L" : 1,
    "M" : 3,
    "N" : 1,
    "O" : 1,
    "P" : 3,
    "Q" : 10,
    "R" : 1,
    "S" : 1,
    "T" : 1,
    "U" : 1,
    "V" : 4,
    "W" : 4,
    "X" : 8,
    "Y" : 4,
    "Z" : 10
}

# # Create a pool from the dictionary
# def create_pool(letter_quant_dict):
#     pool = []
#     for letter in letter_quant_dict:
#         quant = letter_quant_dict[letter]
#         while quant > 0:
#             pool.append(letter)
#             quant -= 1
#     return pool
# pool = create_pool(letter_quant_dict)

def draw_letters(letter_quant_dict):
    pool = []
    for letter in letter_quant_dict:
        quant = letter_quant_dict[letter]
        while quant > 0:
            pool.append(letter)
            quant -= 1
    hand = []
    draw = 10
    while draw > 0:
        index = random.randint(0, len(pool))
        hand.append(pool[index])
        pool.pop(index)
        draw -= 1
    return hand

letter_bank = draw_letters(letter_quant_dict)

def uses_available_letters(word, letter_bank):
    hand = letter_bank
    for letter in word.upper():
        if not letter in hand:
            return False
        hand.remove(letter)
    return True

def score_word(word):
    word_score = 0
    for letter in word.upper():
        letter_score = letter_score_dict[letter]
        word_score += letter_score
    return word_score

def get_highest_word_score(word_list):
    word_score_dict = {}
    
    highest_score_yet = 0
    highest_word_yet = ""
    highest_len_yet = 0
    
    winning_tuple = ()
    
    for word in word_list:
        word_score_dict[word] = score_word(word)

    for word in word_score_dict:
        if word_score_dict[word] > highest_score_yet:
            highest_score_yet = word_score_dict[word]
            highest_word_yet = word
            highest_len_yet = len(word)
        elif word_score_dict[word] == highest_score_yet:
            if len(word) == 10:
                highest_score_yet = word_score_dict[word]
                highest_word_yet = word
                highest_len_yet = len(word)
                winning_tuple = (highest_word_yet, highest_score_yet)
            elif len(word) < highest_len_yet:
                highest_score_yet = word_score_dict[word]
                highest_word_yet = word
                highest_len_yet = len(word)
    winning_tuple = (highest_word_yet, highest_score_yet)
    return winning_tuple
