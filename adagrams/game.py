import random 


# random allows us to accept 
# random letters from LETTER_POOL 
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
    
    for letter in LETTER_POOL.keys():
        players_hand.append(letter)
    
    random.shuffle(players_hand)
    
    return players_hand[:10]
        

def uses_available_letters(word, letter_bank):
    hand_frequency = {}
    
    for letter in letter_bank:
        hand_frequency[letter.upper()] = hand_frequency.get(letter.upper(), 0) + 1

    for letter in word.upper():
        if letter not in hand_frequency or hand_frequency[letter] == 0:
            return False
        else:
            hand_frequency[letter] -= 1

  
    return True

def score_word(word):
    pass
    

def get_highest_word_score(word_list):
    pass
