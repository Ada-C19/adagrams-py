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
    total_score = sum(score_chart.get(letter.upper(), 0) for letter in word)
    if len(word) in [7, 8, 9, 10]:
        total_score += 8
    return total_score
    

def get_highest_word_score(word_list):
    high_score = 0
    best_word = None
    scored_word_dict = {}
    
    for word in word_list:
        score = score_word(word)
        scored_word_dict[word] = score 
        if len(word) == 10:
            best_word = (word, score)
            return best_word
        
        if score > high_score:
            high_score = score 
            if len(word) == 10:
                best_word = (word, high_score)
                return best_word
            else:
                best_word = (word, high_score)
                
            
        elif score == high_score:
            if len(word) == 10:
                best_word = (word, high_score)
            elif len(word) < len(best_word[0]):
                best_word = (word, high_score)
            elif len(word) == len(best_word[0]):
                best_word = (word, high_score)
            
    
    
    return best_word       
        
