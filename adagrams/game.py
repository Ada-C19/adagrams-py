import random
from collections import Counter

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

LETTER_SCORES = {
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
    'Z': 10
}

def draw_letters():
    """""""""
    input: no parameters
    output: 10 letters, each letter repeats proper # of times
    """""""""
    letter_list = []
    for _ in range(10):
        letter = random.choice(list(LETTER_POOL.keys()))
        letter_counts = Counter(letter_list)
        if letter not in letter_list:
            letter_list.append(letter)
        else:
            if letter_counts[letter] < LETTER_POOL[letter]:
                letter_list.append(letter)
            else:
                continue
    return letter_list
    
def uses_available_letters(word, letter_bank):
    letter_dict = Counter(letter_bank)
    cap_word_dict = Counter(list(word.upper()))
    for char, char_count in cap_word_dict.items():
        if cap_word_dict[char] <= letter_dict[char]:
            print(letter_dict[char])
        else:
            return False
    return True
    

def score_word(word):
    scores = []
    total = 0
    for char in list(word.upper()):
        scores.append(LETTER_SCORES[char])
    if len(scores) >= 7 and len(scores) <= 10:
        total += 8
        for value in scores:
            total += value
    else:
        for value in scores:
            total += value
    return total

def get_highest_word_score(word_list):
    pass