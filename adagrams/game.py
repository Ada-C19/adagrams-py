import random
import copy
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
    letter_pool_list = []
    for key, value in LETTER_POOL.items():
        letter = [key] * value
        letter_pool_list.append(letter)
    letter_pool_list = sum(letter_pool_list, [])


    letter_bank = []
    while len(letter_bank) < 10:
        letter = random.choice(letter_pool_list)
        letter_bank.append(letter)
        letter_pool_list.remove(letter)

    return(letter_bank)

word_list = []
def uses_available_letters(word, letters):
    letters_copy = copy.deepcopy(letters)
    word = word.upper()
    for letter in word:
        if letter in letters_copy:
            letters_copy.remove(letter)
        else:
            return False
    word_list.append(word)  
    return True



SCORE_CHART = {"A": 1 , "B": 3 , "C": 3 , "D": 2 ,
"E": 1 , "F": 4 , "G": 2 , "H": 4 ,
"I": 1 , "J": 8 , "K": 5 , "L": 1 ,
"M": 3 , "N": 1 , "O": 1 , "P": 3 ,
"Q": 10, "R": 1 , "S": 1 , "T": 1 ,
"U": 1 , "V": 4 , "W": 4 , "X": 8 ,
"Y": 4 , "Z": 10}


def score_word(word):
    sum = 0
    word = word.lower().upper()
    higher_point_values = [7, 8, 9, 10]
    for letter in word:
        point_value = SCORE_CHART[letter]
        sum += point_value
    if len(word) in higher_point_values:
        sum += 8
    return sum


def get_highest_word_score(word_list):
    score_dict = {} 
    highest_score_word = []
    for word in word_list:
        score_dict[word] = score_word(word)
    max_value = max(score_dict.values())
    for word, point_value in score_dict.items():
        if point_value == max_value:
            highest_score_word.append(word)
    if len(highest_score_word) > 1:
        for word in highest_score_word:
            for i in range(len(highest_score_word)):
                if len(highest_score_word[i]) == 10:
                    return (highest_score_word[i], score_word(highest_score_word[i]))
            for i in range(len(highest_score_word)):    
                bestest_word = min(highest_score_word, key=len)
                if len(highest_score_word[i]) == len(bestest_word):
                    bestest_word = highest_score_word[i]
                    return (bestest_word, score_word(bestest_word))
    else:
        return (highest_score_word[0], score_word(highest_score_word[0]))