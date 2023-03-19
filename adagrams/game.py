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

LETTER_COST = (
        (('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T '), 1),
        (('D', 'G'), 2),
        (('B', 'C', 'M', 'P'), 3),
        (('F', 'H', 'V', 'W', 'Y'), 4),
        (('K'), 5),
        (('J', 'X'), 8),
        (('Q', 'Z'), 10)
        )

def draw_letters():
    letters = ''
    for letter, count in LETTER_POOL.items():
        letters += ''.join(letter*count)
    
    letter_bank = random.choices(letters, k=10)
    
    return letter_bank

def uses_available_letters(word, letter_bank):
    letter_bank_dict = {}
    for letter in letter_bank:
        letter_bank_dict[letter] = letter_bank_dict.get(letter, 0) + 1
        
    if len(word) > len(letter_bank) or not word.isalpha():
        return False
    
    for letter in word.upper().strip():
        if not letter_bank_dict.get(letter, 0):
            return False
        letter_bank_dict[letter] -= 1

    return True

def get_letter_cost(letter):
    for letters, points in LETTER_COST:
        if letter in letters:
            return points
            
def score_word(word):
    score = 0
    for letter in word.upper().strip():
        score += get_letter_cost(letter)
            
    return score

def get_highest_word_score(word_list):
    winner = [None, 0]
    
    for i in range(len(word_list)):
        if word_list[i][1] > winner[0][1]:
            winner = [word_list[i][0], word_list[i][1]]
        elif word_list[i][1] == winner[0][1]:
            winner.append([word_list[1][0], word_list[i][1]])