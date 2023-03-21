import random
import operator

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
        (('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'), 1),
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
    
    letter_bank = random.sample(letters, 10)
    
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
    if len(word) >= 7:
        score += 8
    
    return score

def get_all_highest_words_1(word_list):
    winners = []
    score = 0
    
    for word in word_list:
        word_score = score_word(word)
        if word_score > score:
            winners = [word]
            score = word_score
        elif word_score == score:
            winners.append(word)
            
    return winners, score

def get_all_highest_words(word_list):
    '''
    Returns same results (a list of single winner or all tie scored winner words
    and also it score as a single int) as get_all_highest_words_1 helper function,
    but implemented using module operator and sorted reversed function,
    that way on best case if only 1 winner, for loop will exsit after
    comparing second element value, so it's cheaper.'''
    winners_dict = {}
    winners = []
    
    for word in word_list:
        word_score = score_word(word)
        winners_dict[word] = word_score
    
    sorted_score = list(sorted(winners_dict.items(), key=operator.itemgetter(1), reverse=True))
    score = sorted_score[0][1]
    
    for i in range(len(sorted_score)):
        if sorted_score[i][1] < sorted_score[0][1]:
            return winners, score
        winners.append(sorted_score[i][0])
    
    return winners, score

def get_highest_word_score(word_list):
    winners, score = get_all_highest_words(word_list)

    if len(winners) == 1:
        return ','.join(winners), score
    
    winner_word = ''
    for word in winners:
        if len(word) == 10:
            return word, score
        
        if not winner_word:
            winner_word = word
        else:
            if len(word) < len (winner_word):
                winner_word = word
                print(winner_word)
                
    return winner_word, score