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

def draw_letters():
    pool = []
    for letter in letter_quant_dict:
        quant = letter_quant_dict[letter]
        while quant > 0:
            pool.append(letter)
            quant -= 1
    hand = []
    draw = 10
    while draw > 0:
        index = random.randint(0, len(pool)-1)
        hand.append(pool[index])
        pool.pop(index)
        draw -= 1
    return hand

# def uses_available_letters(word, letter_bank):
#     hand = letter_bank
#     for letter in word.upper():
#         if not letter in hand:
#             return False
#         hand.remove(letter)
#     return True

def uses_available_letters(word, letter_bank):
    #I dont understand why we woulndt want to update the letter_bank but ok

    #build letter_bank_dict
    letter_bank_dict = {}
    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1
        else:
            letter_bank_dict[letter] = 1

    #build hand_dict
    hand_dict = {}
    for letter in word.upper():
        if letter in hand_dict:
            hand_dict[letter] += 1
        else:
            hand_dict[letter] = 1
    
    #compare two dictionaries
    for letter in hand_dict:
        if letter not in letter_bank_dict:
            return False
        elif hand_dict[letter] > letter_bank_dict[letter]:
            return False
    return True


def score_word(word):
    word_score = 0
    if len(word) >= 7:
        word_score += 8
    for letter in word.upper():
        letter_score = letter_score_dict[letter]
        word_score += letter_score
    return word_score

# def get_highest_word_score(word_list):
#     word_score_dict = {} 
#     highest_score_yet = 0
#     highest_word_yet = ""
#     highest_len_yet = 0
#     for word in word_list:
#         word_score_dict[word] = score_word(word)
#     for word, score in word_score_dict.items():
#         if score > highest_score_yet:
#             highest_score_yet = score
#             highest_word_yet = word
#             highest_len_yet = len(word)
#         if score == highest_score_yet:
#             if len(word) == 10:
#                 highest_score_yet = score
#                 highest_word_yet = word
#                 highest_len_yet = len(word)
#                 winning_tuple = (highest_word_yet, highest_score_yet)
#             elif len(word) < highest_len_yet:
#                 highest_score_yet = score
#                 highest_word_yet = word
#                 highest_len_yet = len(word)
#     winning_tuple = (highest_word_yet, highest_score_yet)
#     return winning_tuple
    
def get_highest_word_score(word_list):
    highest_word_score = 0
    highest_score_words = []
    #find the highest score
    for word in word_list:
        if score_word(word) > highest_word_score:
            highest_word_score = score_word(word)
    #add word(s) with the highest score to the highest_word_score_words list
    for word in word_list:
        if score_word(word) == highest_word_score:
            highest_score_words.append(word)
    # return the word (as a tuple) with the highest score if theres only one
    if len(highest_score_words) == 1:
        return tuple([str(highest_score_words[0]), score_word(highest_score_words[0])])
    # break tie
    elif len(highest_score_words) > 1:
        # initialize the shortest length
        shortest_word_len = 9
        # find the first 10 or shortest length
        for word in highest_score_words:            
            # return the first 10 letter long word
            if len(word) == 10:
                return tuple([word, score_word(word)])    
            elif len(word) < shortest_word_len:
                shortest_word_len = len(word)
        # return the first, shortest length word
        for word in highest_score_words:
            if len(word) == shortest_word_len:
                return tuple([word, score_word(word)])