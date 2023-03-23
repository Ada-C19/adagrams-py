import random


LETTER_POOL = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D',
        'D','D','D','E','E','E','E','E','E','E','E','E','E','E','E','F',
        'F','G','G','G','H','H','I','I','I','I','I','I','I','I','I','J',
        'K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O',
        'O','O','O','O','O','P','P','Q','R','R','R','R','R','R','S','S',
        'S','S','T','T','T','T','T','T','U','U','U','U','V','V','W','W',
        'X','Y','Y','Z']


def draw_letters():
    working_letter_pool = LETTER_POOL.copy()
    hand = []

    for index in range(10):
        drawn_letter = random.choice(working_letter_pool)
        if drawn_letter in working_letter_pool:
            hand.append(drawn_letter)
        working_letter_pool.remove(drawn_letter)  
    return hand


def uses_available_letters(word, letter_bank):
    working_letter_bank = letter_bank.copy()    
    word = str.upper(word)

    for letter in word:
        if letter in working_letter_bank:
            working_letter_bank.remove(letter)
        else:
            return False
    return True

def score_word(word):
    score = 0
    word = str.upper(word)

    one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    two_point = ['D','G']
    three_point = ['B', 'C', 'M', 'P']
    four_point = ['F', 'H', 'V', 'W', 'Y']
    five_point = ['K']
    eight_point = ['J', 'X']
    ten_point = ['Q', 'Z']

    word_length = len(word)
    if word_length <= 0:
        score += 0
    if word_length >= 7:
        score += 8

    for letter in word:
        if letter in ten_point:
            score += 10
        elif letter in eight_point:
            score += 8
        elif letter in five_point:
            score += 5
        elif letter in four_point:
            score += 4
        elif letter in three_point:
            score += 3
        elif letter in two_point:
            score += 2
        elif letter in one_point:
            score += 1
        else:
            score += 0
    return score

def get_highest_word_score(word_list):
    best_word = ""
    highest_score = 0

    for word in word_list:
        temp_score = score_word(word)

        if temp_score > highest_score:
            highest_score = temp_score
            best_word = word
        elif temp_score == highest_score:
            # scores are the same 
            if len(word) !=  len(best_word):
                #length of word is not the same
                if len(best_word) != 10:
                    #length of best word is not 10
                    if len(word) == 10:
                    # length of word is 10 but best word is not already 10
                        best_word = word
                    elif len(word) < len(best_word):
                    # length of word is shorter than best_word
                        best_word = word

    return tuple([best_word,highest_score])