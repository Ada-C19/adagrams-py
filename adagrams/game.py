import random


def draw_letters():
    
    letters   = {
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

    pieces = []
    count = 99
    for i in range(10):
        rand_piece = random.randrange(1, count)
        key = weighted(letters, rand_piece)
        pieces.append(key)
        
        if letters[key] == 0:
            letters.pop(key)
        else:
            letters[key] -= 1
        count -= 1
    return pieces

def weighted(dict,random_piece):
    for char, weight in dict.items():
            random_piece = random_piece - weight
            if random_piece <= 0:
                #pieces.append(char)
                return char

"""
def draw_letters():
    
    letters = [
        'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
        'B', 'B',
        'C', 'C',
        'D', 'D', 'D', 'D',
        'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
        'F', 'F',
        'G', 'G', 'G',
        'H', 'H',
        'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
        'J',
        'K',
        'L', 'L', 'L', 'L',
        'M', 'M',
        'N', 'N', 'N', 'N', 'N', 'N',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
        'P', 'P',
        'Q',
        'R', 'R', 'R', 'R', 'R', 'R', 
        'S', 'S', 'S', 'S',
        'T', 'T', 'T', 'T', 'T', 'T', 
        'U', 'U', 'U', 'U', 
        'V', 'V', 
        'W', 'W', 
        'X', 
        'Y', 'Y',
        'Z'
            ]

    pieces = []


    random.shuffle(letters)
    for i in range (10):
        rand_piece = random.randrange(len(letters))
        
        pieces.append(letters[rand_piece])
        letters.pop(rand_piece)
    return pieces

""" 
"""
def draw_letters():
    rand_letters =[]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']
    weight = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 
            4, 6, 4, 2, 2, 1, 2, 1]

    for i in range(10):
        rand_piece = random.choices(letters, weights = weight, k = 1)

        # with replacement 
        index = letters.index(rand_piece[0])
        weight[index] -= 1
        if weight[index] == 0:
            weight.pop(index)
            letters.pop(index)

        rand_letters.append(rand_piece[0])

    return rand_letters
"""
def uses_available_letters(word, letter_bank):
    # check if they can use the word they inputted
    new_letter_bank = []
    for l in letter_bank:
        new_letter_bank.append(l.upper())
    for letter in word:
        if letter.upper() in new_letter_bank:
            new_letter_bank.remove(letter.upper())
        else:
            return False
    return True

def score_word(word):
    values = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T') :1,
            ('D', 'G'):	2,
            ('B', 'C', 'M', 'P'): 3,
            ('F', 'H', 'V', 'W', 'Y') : 4,
            ('K'): 5,
            ('J', 'X'):	8,  
            ('Q', 'Z'):	10}
    
    sum = 0
    if len(word) >= 7:
        sum += 8
    for letter in word:
        for val in values.keys():
            if letter.upper() in val:
              sum += values.get(val)
              continue
    return sum


def get_highest_word_score(word_list):
    max_val = 0
    temp_score = 0

    for word in word_list:
        temp_score = score_word(word)
        if max_val < temp_score:
            max_val = temp_score
            max_word = word
        elif max_val == temp_score:
            if len(word) == 10 and len(max_word) != 10:
                max_word = word       
            elif len(word) < len(max_word) and len(max_word) != 10:
                max_word = word
            
    tup = (max_word, max_val)
    return tup
