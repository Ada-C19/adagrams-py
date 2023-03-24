import random

def draw_letters():
    letters_drawn = []
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

    i = 0
    while i < 10:
        random_letter = random.choice(list(LETTER_POOL.keys()))
        letter_count = letters_drawn.count(random_letter)
        if letter_count < LETTER_POOL[random_letter]:
            letters_drawn.append(random_letter)
            i += 1
        
    return letters_drawn


def uses_available_letters(word, letter_bank):
    word = word.upper()

    for letter in word:
        if letter not in letter_bank:
            return False
        elif not word.count(letter) <= letter_bank.count(letter):
            return False
    return True

def score_word(word):
    word = word.upper()
    score = 0
    letter_scores = {
        'A': 1,
        'E': 1,
        'I': 1,
        'O': 1,
        'U': 1,
        'L': 1,
        'N': 1,
        'R': 1,
        'S': 1,
        'R': 1,
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
        'Z': 10,
    }
    
    if len(word) >= 7:
        score += 8
    
    if word == '':
        return False
    else:
        for letter in word:
            score += letter_scores[letter]
    
    return score


def get_highest_word_score(word_list):
    list_of_scores = []
    length_of_words = []

    for word in word_list:
        get_scores = score_word(word)
        list_of_scores.append(get_scores)
        word_length = len(word)
        length_of_words.append(word_length)
    
    highest_score = max(list_of_scores)
    index_of_highscore = list_of_scores.index(highest_score)
    right_word = word_list[index_of_highscore]
    count_of_highscore = list_of_scores.count(highest_score)
    
    if count_of_highscore == 1:
        winner = (right_word, highest_score)
        return winner
    else:
        for number in length_of_words:
            if number == 10:
                index_of_ten_letter_word = length_of_words.index(number)
                return (word_list[index_of_ten_letter_word], highest_score)
        smallest_number = min(length_of_words)
        for word in word_list:
            if len(word) == 10:
                return (word, highest_score)
            elif len(word) == smallest_number:
                return (word, highest_score)
            




