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

    letter_pool = LETTER_POOL.copy()
    letters = []
    for i in range(10):
        letter = random.choice(list(letter_pool.keys()))
        while letter_pool[letter] == 0:
            letter = random.choice(list(letter_pool.keys()))
        letters.append(letter)
        letter_pool[letter] -= 1

    return letters

def uses_available_letters(word, letter_bank):
    
    letter_word_upper = word.upper()
    letter_bank_copy = letter_bank.copy()

    for letter in letter_word_upper:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
    
        else: 
            return False
        
    return True 

def score_word(word):
    letter_word_upper = word.upper()
    final_score = 0 
    for letter in letter_word_upper:
        final_score += LETTER_SCORES[letter]
    
    if len(word) > 6:
        final_score += 8
    
    return final_score

def get_highest_word_score(word_list):
    
    max_score = ('xaerfgtyujh',-1)
    for word in word_list:
        score = score_word(word)
        if max_score[1] < score: 
            max_score = (word,score)
        elif max_score[1] == score and len(word) != len(max_score[0]):
            if len(word) == 10:
                max_score = (word,score)
            elif len(max_score[0]) != 10 and len(word) < len(max_score[0]):
                max_score = (word,score)
    return max_score
        
