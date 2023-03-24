import random

def draw_letters():
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

    letter_bank = []
    for i in range(10):
        letter = random.choice(list(LETTER_POOL.keys()))
        letter_bank.append(letter)
        LETTER_POOL[letter] -= 1
        
        if LETTER_POOL[letter] == 0:
            LETTER_POOL.pop(letter)


    print(letter_bank)
    return letter_bank


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
        
    return True

def score_word(word):
    LETTER_POINT_VALUE = {
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
    for letter in word.upper():
        point_value = LETTER_POINT_VALUE[letter]
        score += point_value
    if len(word) >= 7:
        score += 8  
    
    return score
    

def get_highest_word_score(word_list):
    # PART 1: 
    word_dict= {}
    for word in word_list:
        points = score_word(word)
        word_dict[word] = points
    
    max_key = max(word_dict, key=word_dict.get)
    max_value = word_dict[max_key]

    # part 2

    tie_words = []
    for word, value in word_dict.items():
        if value == max_value:
            tie_words.append(word)
    print(tie_words, max_value)

    if len(tie_words) == 1:
        return max_key, max_value
    
    word_lengths = {}
    for word in tie_words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length].append(word)
        else:
            word_lengths[length] = [word]

    # check a word has 10 characters

    if 10 in word_lengths:
        max_key_ten = word_lengths[10][0]
        return max_key_ten, max_value
    
    # check shortest 

    minimum_key = min(word_lengths)
    print(minimum_key)
    first_word = word_lengths[minimum_key][0]
    print(first_word, max_value)
    return first_word, max_value
    

