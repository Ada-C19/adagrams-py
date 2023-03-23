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


    letter_pool_copy = letter_pool.copy()
    hand_of_letter = []

    while len(hand_of_letter) < 10:
        letter = random.choice(list(letter_pool_copy.keys()))
        if letter.isalpha() and letter_pool_copy[letter] > 0:
                hand_of_letter.append(letter)
                letter_pool_copy[letter] -=1
        else:
            continue
    return hand_of_letter



def uses_available_letters(word, letter_bank):

    word = word.upper()
    letter_dict = {}
    for letter in letter_bank:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    
    for letter in word:
        if letter not in letter_dict:
            return False
        elif letter_dict[letter] == 0:
            return False
        else:
            letter_dict[letter] -= 1
    
    return True 



def score_word(word):
    letter_value = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, 
        "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10
    }

    score = 0
    word = word.upper()
    for letter in word:
        score += letter_value[letter]
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    scores_calculate = {}
    for word in word_list:
        score = score_word(word)
        scores_calculate[word] = score
    
    max_score = max(scores_calculate.values())

    winners = []
    for word in scores_calculate :
        if scores_calculate[word] == max_score:
            winners.append(word)

    bigest_word = max(winners, key=len)
    smallest_word = min(winners, key=len)
    
    if len(winners) == 1: 
        return (winners[0], scores_calculate[winners[0]])
    elif len(bigest_word) == 10:
        return (bigest_word, scores_calculate[bigest_word])
    else:
        return (smallest_word, scores_calculate[smallest_word])

