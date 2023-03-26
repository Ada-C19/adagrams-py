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
    LENGTH_OF_HAND = 10
    ALPHABET = list(letter_pool.keys())
    
    for i in range(LENGTH_OF_HAND):
        letter_choice = random.choice(ALPHABET)
        while letter_pool[letter_choice] == 0:
            letter_choice = random.choice(ALPHABET)
        hand.append(letter_choice)
        letter_pool[letter_choice] -= 1
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
    LETTER_POINTS = {
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
        if letter in LETTER_POINTS:
            score += LETTER_POINTS[letter]
    if len(word) >=7 and len(word) <=10:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    word_scores = {}
    for word in word_list:
        score = score_word(word)
        word_scores[word] = score

    high_score = 0
    high_scorers = []
    for score in word_scores.values():
        if score >= high_score:
            high_score = score
    for word, score in word_scores.items():
        if score == high_score:
            high_scorers.append(word)

    winner = ''
    shortest_word = []
    shortest_word_length = len(min(high_scorers, key=len))

    for word in high_scorers:
        if len(word) == 10:
            winner = word
            return winner, high_score      
        elif len(word) == shortest_word_length:
            shortest_word.append(word)

    winner = shortest_word[0]
    
    return winner, high_score