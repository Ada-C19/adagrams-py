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

SCORE_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"], 
    3: ["B", "C", "M", "P"], 
    4: ["F", "H", "V", "W", "Y"], 
    5: ["K"], 
    8: ["J", "X"], 
    10: ["Q", "Z"]
    }

def draw_letters():
    hand_of_letters = []
    
    while len(hand_of_letters) <= 9:
        letter = random.choice(list(LETTER_POOL))
        if hand_of_letters.count(letter) < LETTER_POOL[letter]:
            hand_of_letters.append(letter)
        if len(hand_of_letters) >= 10:
            break
    
    return hand_of_letters

def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()

    for letter in uppercase_word:
        count_of_letter_in_uppercase_word = uppercase_word.count(letter)
        count_of_letter_in_letter_bank = letter_bank.count(letter)
        if count_of_letter_in_uppercase_word <= count_of_letter_in_letter_bank:
            continue
        else:
            return False
        
    return True
    

def score_word(word):
    uppercase_word = word.upper()
    score = 0

    for letter in uppercase_word:
        for points, letters in SCORE_CHART.items():
            if letter in letters:
                score += points
    
    if len(uppercase_word) == 7:
        score += 8
    elif len(uppercase_word) == 8:
        score += 8
    elif len(uppercase_word) == 9:
        score += 8
    elif len(uppercase_word) == 10:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    pass






