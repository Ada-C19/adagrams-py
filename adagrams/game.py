import random 

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
    cap_word = word.upper()
    letter_bank_quantity = {}
    char_quantity = {}
    result = False

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
            break 
        else:
            result = True

    return result  


def score_word(word):
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
            if char in letter_score[i][0]:
                sum_score += letter_score[i][1]
    
    if len(word) >= 7:
        sum_score += 8

    return sum_score


def get_highest_word_score(word_list):
    
    words_and_score = []
    index_of_highest_tuple = 0
    
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
            index_of_highest_tuple = i
        elif score == highest_score:
            current_highest = words_and_score[index_of_highest_tuple][0]
            if len(word) == len(current_highest):
                #index_of_highest_tuple stays the same
                continue
            elif len(current_highest) == 10:
                continue
            elif len(word) < len(current_highest):
                index_of_highest_tuple = i
            elif len(word) == 10:
                index_of_highest_tuple = i
                                

    
    return words_and_score[index_of_highest_tuple]
