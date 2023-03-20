import random

def draw_letters():
    letters = {
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
    hand = []
    for i in range(10):
        choose_letter = list(letters.keys())
        letter_choice = random.choice(choose_letter)
        while letters[letter_choice] == 0:
            letter_choice = random.choice(choose_letter)
        hand.append(letter_choice)
        letters[letter_choice] -= 1
    return hand
            


def uses_available_letters(word, letter_bank):
    letters_used = [letter for letter in letter_bank]
    word = word.upper()
    for letter in word:
        if letter in letters_used:
            letters_used.remove(letter)
    if len(word) == len(letter_bank) - len(letters_used):
        return True
    else:
        return False


def score_word(word):
    letter_points = {
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
    
    word = word.upper()
    score = int()
    for letter in word:
        if letter in letter_points:
            score += letter_points[letter]
    if len(word) >=7 and len(word) <=10:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    pass