import random

def draw_letters():
    
    letters   = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 
    'Y': 2, 'Z': 1 }

    pieces = []
    # number of pieces in letter pool
    count = 98

    for i in range(10):
        rand_piece = random.randrange(1, count+1)
        key = weighted(letters, rand_piece)
        pieces.append(key)
        
        letters[key] -=1
        if letters[key] == 0:
            letters.pop(key)
        count -= 1
    return pieces

def weighted(dict,random_piece):
    for char, weight in dict.items():
            random_piece -= weight
            if random_piece <= 0:
                return char
            
def uses_available_letters(word, letter_bank):
    # check if they can use the word they inputed
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
    values = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T') : 1,
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
