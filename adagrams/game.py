import random

def draw_letters():
    letter_pool = {
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
        letters = list(letter_pool.keys())
        letter = random.choice(letters)
        while letter_pool[letter] == 0:
            letter = random.choice(letters)
        hand.append(letter)
        letter_pool[letter] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    letter_bank_lower = [letter.lower() for letter in letter_bank]
    word_lower = word.lower()
    
    for letter in word_lower:
        if letter in letter_bank_lower:
            letter_bank_lower.remove(letter)
        else:
            return False
    return True

def score_word(word):
    score_chart ={
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    score = 0
    word = word.upper()
    
    for letter in word:
        score += score_chart[letter]
    
    if len(word) in [7, 8, 9, 10]:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = ""
    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score
            winning_word = word
        elif word_score == highest_score:
            if len(word) == 10 and len(winning_word) != 10:
                winning_word = word
            elif len(word) < len(winning_word) and len(winning_word) != 10:
                winning_word = word
    return (winning_word, highest_score)
