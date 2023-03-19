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
    

def cap_converter(original_word):
    return original_word.upper()

# def uses_available_letters(word, letter_bank):
#     letter_set = set(letter_bank)
#     cap_word_set = set(list(cap_converter(word)))
#     if cap_word_set <= letter_set:
#         return True
#     else:
#         return False
def uses_available_letters(word, letter_bank):
    letter_dict = Counter(letter_bank)
    cap_word_dict = Counter(list(word.upper()))
    for char, char_count in cap_word_dict.items():
        if cap_word_dict[char] <= letter_dict[char]:
            print(letter_dict[char])
            # print("Yup")
        else:
            return False
    return True
    

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass