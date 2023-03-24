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

    # Randomly get letters from letter pool while decrementing the value associated with it
    while len(hand) < 10:
        letter = random.choice(list(letter_pool))
        if letter_pool[letter] > 0:
            hand.append(letter)
            letter_pool[letter] -= 1
            
    return hand

def uses_available_letters(word, letter_bank):
    # Create a copy of letter bank
    letters_copy = letter_bank.copy()

    # Loop through each letter of word and remove letter from letters copy
    for letter in word:
        if letter.upper() in letters_copy:
            letters_copy.remove(letter.upper())
        else:
            return False
    
    return True

def score_word(word):
    SCORE_CHART = {
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

    score = 0
    # Add up points for each letter of word according to score chart
    for letter in word:
        score += SCORE_CHART[letter.upper()]

    # Add 8 extra points to score if word has 7-10 letters 
    if 7 <= len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    winning_word = ""
    highest_score = 0

    for word in word_list:
        # Get score for each word in word list
        score = score_word(word)

        # Check if word has 10 letters
        if len(word) == 10:
            highest_score = score
            winning_word = word
            break

        # Check for highest score
        elif score > highest_score:
            highest_score = score
            winning_word = word
        
        # If highest score is tied, get shortest word
        elif score == highest_score and len(word) < len(winning_word):
            winning_word = word
        
    return winning_word, highest_score