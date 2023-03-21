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

def draw_letters():
    # create letter bag
    letters_bag = []
    for letter, quantity in LETTER_POOL.items():
        # letter_to_add = letter
        for i in range(quantity):
            letters_bag.append(letter)
    
    player_letters = []
    while len(player_letters) < 10:
        random_letter = random.choice(letters_bag)
        letters_bag.remove(random_letter)
        player_letters.append(random_letter)

    return player_letters

def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if letter not in letter_bank:
            return False
        elif word.count(letter) > letter_bank.count(letter):
            return False
    return True

def score_word(word):
    word = word.upper()
    score = 0
    for letter in word:
        if letter in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
            score += 1
        elif letter in ["D", "G"]:
            score += 2
        elif letter in ["B", "C", "M", "P"]:
            score += 3
        elif letter in ["F", "H", "V", "W", "Y"]:
            score += 4
        elif letter == "K":
            score += 5
        elif letter in ["J", "X"]:
            score += 8
        elif letter in ["Q", "Z"]:
            score += 10
        
    if len(word) >= 7:
        score += 8

    return score

def get_highest_word_score(word_list):
    best_word = ""
    high_score = score_word(best_word)
    for word in word_list:
        new_score = score_word(word)
        if new_score == high_score:
            if len(best_word) == 10:
                continue
            if len(word) == 10:
                best_word = word
            elif len(word) < len(best_word): 
                best_word = word
        elif new_score > high_score:
            high_score = new_score
            best_word = word
        
    return best_word, high_score