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

    letter_pool_copy_dict = LETTER_POOL.copy()
    full_letter_bank_list = []
    my_letter_bank_list = []

    for letter in letter_pool_copy_dict:
        while full_letter_bank_list.count(letter) < letter_pool_copy_dict[letter]:
            full_letter_bank_list.append(letter)

    while len(my_letter_bank_list) < 10:
        random_letter = random.choice(full_letter_bank_list)
        my_letter_bank_list.append(random_letter)
        full_letter_bank_list.remove(random_letter)

    return my_letter_bank_list



def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        if letter not in letter_bank:
            return False
        if word.count(letter) > letter_bank.count(letter):
            return False
    return True
            
    
    

def score_word(word):
    SCORE_CHART = {
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1,
    'L': 1,
    'N': 1,
    'R': 1,
    'S': 1,
    'T': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10
    }


    word = word.upper()
    score = 0
    if len(word) >= 7:
        score += 8
    for letter in word:
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]
        elif letter not in SCORE_CHART:
            return 0
        
    return score



def get_highest_word_score(word_list):
    score_with_word_dict = {}
    word_list_with_scores = []
    word_length_list = []

    
    for word in word_list:
        score = score_word(word)
        score_with_word_dict[word]= score

    highest_score = max(score_with_word_dict.values())
    for word, score in score_with_word_dict.items():
        if highest_score == score:
            winning_word= (word, score)
            word_list_with_scores.append(winning_word)


    for str, value in word_list_with_scores:
        word_length_list.append(len(str))
        if len(str) == 10:
            winning_word = (str, value)
            return winning_word
        else: 
            continue
        

    least_letter_word= min(word_length_list)
    for str, value in word_list_with_scores:
        word_length_list.append(len(str))
        if len(str) == least_letter_word:
            winning_word = (str, value)
            return winning_word


