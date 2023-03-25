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
    letters = []
    pool = LETTER_POOL.copy()
    while len(letters) < 10:
        hand = random.choice(list(pool))
        if pool[hand] <= 0:
            continue
        pool[hand] -= 1
        letters.append(hand)
    return letters

def uses_available_letters(word, letter_bank):
    bank = letter_bank.copy()
    for character in word:
        character = character.upper()
        if character in bank:
            bank.remove(character)
        else:
            return False
    return True          

def score_word(word):
    score = 0
    for character in word:
        character = character.upper() 
        score += SCORE_CHART[character] 
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    candidates = [(w, score_word(w)) for w in word_list]
    highest_score = max(candidates, key = lambda c: c[1])
    ties = [c for c in candidates if c[1] == highest_score[1]]
    if len(ties) == 1:
        return ties[0]
    for c in candidates:
        if len(c[0]) == 10:
            return c
    return min(ties, key=lambda t: len(t[0]))