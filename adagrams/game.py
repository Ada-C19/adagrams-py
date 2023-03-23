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
    players_hand = []
    letter_bag = []

    for letter, quantity in LETTER_POOL.items():
        for i in range(quantity):
            letter_bag.append(letter)


    while len(players_hand) < 10:
        letter_for_hand = random.choice(letter_bag)
        players_hand.append(letter_for_hand)
        letter_bag.remove(letter_for_hand)
    
    print(players_hand)
    return players_hand
    

def uses_available_letters(word, letter_bank): 
    word = word.upper()
    result = 1
    letter_bank_2 = letter_bank.copy()

    for x in word:
        if (all (x in letter_bank for x in word)):
            if x in letter_bank_2:
                letter_bank_2.remove(x)
            else:
                result = 0
        else: 
            result = 0
    return result
    
        

def score_word(word):
    score_chart = { 
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
    points = 0
    if len(word) == 0:
        return 0
    else:
        for i in range(len(word)):
            word = word.upper()
            if len(word) > 6:
                points = 8
            else: 
                points = 0 
            for letter in word:
                letter_value = score_chart[letter]
                points += letter_value
            return points



def get_highest_word_score(word_list):
    word_scores = []

    for word in word_list:
        score = score_word(word)
        word_scores.append(score)

    highest_score = max(word_scores)
    
    for word in word_list:
        if len(word) == 10 and score_word(word) == highest_score:
            winning_word = word
            break
        else:
            sorted_word_list = sorted(word_list, key=len)
            for word in sorted_word_list:
                if score_word(word) == highest_score:
                    winning_word = word
                    break
    return winning_word, highest_score



