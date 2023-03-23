import random


def draw_letters():                                                                       
    letter_pool_dict = {
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
    pool_list = []
    player_hand = []

    for letter, count in letter_pool_dict.items():
        pool_list += [letter] * count

    while len(player_hand) < 10:  
        letter = random.choice(pool_list) 
        player_hand += letter
        pool_list.remove(letter)
    return player_hand    


def uses_available_letters(word, letter_bank):
    copy = letter_bank[:]
    word = word.upper()
    player_word = []
    for letter in word:
        if letter in copy:
            copy.remove(letter)
            player_word.append(letter)
        else:
            return False
    return True
                    

def score_word(word):
    letter_values = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}   
    
    word = word.upper()
    score = 0
    for letter in word:
        points = letter_values[letter]
        score += points

    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    word_score_dict = {}
    
    for word in word_list:
        score = score_word(word)
        if score in word_score_dict:
            word_score_dict[score].append(word)
        else:
            word_score_dict[score] = [word]
    
    winning_score = max(word_score_dict.keys())
    winning_words = word_score_dict[winning_score]
    best_word = winning_words[0]

# what should i assume  the default winner is? IT. DOESNT. MATTER. START FROM THE BEGINNING.
    for challenger in winning_words:
        if len(challenger) > len(best_word) and len(challenger) ==10:
            best_word = challenger 
        if len(challenger) < len(best_word) and len(best_word) != 10:
            best_word = challenger
    return (best_word, winning_score)
