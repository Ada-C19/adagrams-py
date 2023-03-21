import random

def generate_letter_pool():
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
    letter_pool_list = []
    for letter, quantity in LETTER_POOL.items():
        letter_pool_list.extend([letter] * quantity)
    
    return letter_pool_list 

print(generate_letter_pool())


def casefold_letters(letters):
    casefolded_letters = []
    for letter in letters:
        casefolded_letters.append(letter.casefold())
    
    return casefolded_letters


def count_available_letters(letters):
    letter_counts = {}
    for letter in letters:
        letter_counts[letter] = 0
    for letter in letters:
        letter_counts[letter] += 1
    
    return letter_counts


def find_top_word_and_score(scores):
    top_word = ''
    top_score = 0

    for word, score in scores.items():
        if score > top_score:
            top_word = word
            top_score = score
        elif score == top_score:
            if len(word) == 10 and len(top_word) != 10:
                top_word = word
                top_score = score
            elif len(top_word) == 10:
                continue
            elif len(word) < len(top_word):
                top_word = word
                top_score = score
    
    return top_word, top_score


def draw_letters():
    letter_pool_list = generate_letter_pool()
    letter_bank = []

    for tile in range(0, 10):
        random_tile = random.choice(letter_pool_list)
        letter_pool_list.remove(random_tile)
        letter_bank.append(random_tile)
    
    return letter_bank


def uses_available_letters(word, letter_bank):
    letter_bank = casefold_letters(letter_bank)
    word = casefold_letters(word)
    letter_counts = count_available_letters(letter_bank)

    for letter in word:
        if letter in letter_bank and letter_counts[letter] > 0:
            letter_counts[letter] -= 1
        else:
            return False
    
    return True


def score_word(word):
    point_values = {
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

    score = 0
    if len(word) in range(7,11):
        score += 8
    for letter in word:
        score += point_values[letter.upper()]
    
    return score
    
        
def get_highest_word_score(word_list):
    scores = {}
    potential_winning_word = ""
    second_potential_winning_word = ""
    potential_highest_score = 0
    second_potential_highest_score = 0

    for word in word_list:
        scores[word] = score_word(word)

    potential_winning_word, potential_highest_score = find_top_word_and_score(scores)
        
    scores.pop(potential_winning_word)

    second_potential_winning_word, second_potential_winning_score = find_top_word_and_score(scores)

    top_two_words = {
        potential_winning_word : potential_highest_score,
        second_potential_winning_word : second_potential_winning_score
    }

    winning_word_and_score = find_top_word_and_score(top_two_words)

    return winning_word_and_score
