import random 
"""
Define a list of tuples, to access frequency of letter and letter at same index
"""
LETTER_POOL = [
    ("A", 9),
    ("B", 2),
    ("C", 2),
    ("D", 4),
    ("E", 12),
    ("F", 2),
    ("G", 3),
    ("H", 2),
    ("I", 9),
    ("J", 1),
    ("K", 1),
    ("L", 4),
    ("M", 2),
    ("N", 6),
    ("O", 8),
    ("P", 2),
    ("Q", 1),
    ("R", 6),
    ("S", 4),
    ("T", 6),
    ("U", 4),
    ("V", 2),
    ("W", 2),
    ("X", 1),
    ("Y", 2),
    ("Z", 1)
]

def draw_letters():
    """
    Create a list number_of_letter_available of same lenght as LETTER_POOL
    Generate random integer, to get random index to access number_of_letters_available
    If number is greater than one, add to letter_bank list and subtract one, at the given index
    Returns letter_bank
    """
    letter_bank = []
    number_of_letter_available = []
    
    for letter in LETTER_POOL:
        number_of_letter_available.append(letter[1])
    
    while len(letter_bank) < 10:    
        random_index = random.randint(0, len(LETTER_POOL) - 1)
        if number_of_letter_available[random_index] > 0:
            letter_bank.append(LETTER_POOL[random_index][0])
            number_of_letter_available[random_index] -= 1
 
    return letter_bank


def uses_available_letters(word, letter_bank):
    """
    Create a dictionary looping over letter in letter_bank 
    Create key using letter, sum quantities of given letter key
    Create dictionary for letter in word, similarly 
    Returns True or False
    """
    cap_word = word.upper()
    letter_bank_quantity = {}
    char_quantity = {}
    result = None #flag called result 

    for letter in letter_bank:
        if letter not in letter_bank_quantity:
            letter_bank_quantity[letter] = 1
        else:
            letter_bank_quantity[letter] += 1
    
    for char in cap_word:
        if char not in char_quantity:
            char_quantity[char] = 1
        else:
            char_quantity[char] += 1
    
    for letter in cap_word:
        if letter not in letter_bank or char_quantity[letter] > letter_bank_quantity[letter]:
            result = False 
        else:
            result = True

    return result  


def score_word(word):
    """
    Define a list of tuples with group of letter's point value
    Loop over letter_score list to find if each character in word is in list
    If char is found in that index, score will be same index of outer list, index 1 of inner list
    Returns sum_score, holds total points for given word 
    """
    letter_score = [
        [("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"), 1],
        [("D", "G"), 2],
        [("B", "C", "M", "P"), 3],
        [("F", "H", "V", "W", "Y"), 4],
        [("K"), 5],
        [("J", "X"), 8],
        [("Q", "Z"), 10]
    ]
    
    cap_word = word.upper()
    sum_score = 0

    for char in cap_word:
        for i in range(len(letter_score)):
            if char in letter_score[i][0]: #check if char is in list of letters in inner list index 0
                sum_score += letter_score[i][1] #sums integer in inner list index 1
    
    if len(word) >= 7:
        sum_score += 8

    return sum_score


def get_highest_word_score(word_list):
    """
    Create a list of tuples containing word from word_list and score 
    Calculate score calling score_word function for word
    Each word and corresponding score will be at same index of list 
    Returns tuple of highest scoring word and corresponding score
    """
    words_and_score = []
    
    index_of_highest_tuple = 0 #keeps track of index where the current highest scoring word is located
    highest_score = 0 

    for word in word_list:
        score = score_word(word)
        word_tuple = (word, score)
        words_and_score.append(word_tuple)
    
    for i in range(len(words_and_score)):
        score = words_and_score[i][1]
        word = words_and_score[i][0]
        if score > highest_score:
            highest_score = score
            index_of_highest_tuple = i #assigns index of word currently being checked in for loop
        elif score == highest_score:
            current_highest = words_and_score[index_of_highest_tuple][0]
            if len(word) == len(current_highest):    
                continue #index_of_highest_tuple stays the same
            elif len(current_highest) == 10:
                continue 
            elif len(word) < len(current_highest):
                index_of_highest_tuple = i #updates index_of_highest_tuple 
            elif len(word) == 10:
                index_of_highest_tuple = i
                                

    
    return words_and_score[index_of_highest_tuple]
