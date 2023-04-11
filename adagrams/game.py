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


def draw_letters():
    hand = []

    while len(hand) < 10:
        letter = random.choice(list(LETTER_POOL))
        if hand.count(letter) < LETTER_POOL[letter]:
            hand.append(letter)

    return hand

def uses_available_letters(word, letter_bank):
    letter_freq_in_word = {}
    letter_freq_in_bank = {}

    # word = word.upper()

    for i in range(len(word)):
        if word[i] not in letter_freq_in_word:
            letter_freq_in_word[word[i]] = 0
        letter_freq_in_word[word[i]] += 1

        occurrence = letter_bank.count(word[i])
        if word[i] not in letter_freq_in_bank:
            letter_freq_in_bank[word[i]] = occurrence

    for letter in word:
        if letter_freq_in_word[letter] > letter_freq_in_bank[letter]:
            return False
        
    return True

def score_word(word):
    score_board = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    score = 0
    extra_points = 8
    extra_points_min_length = 7
    extra_points_max_length = 10

    points_list = list(score_board)
    letters_list = list(score_board.values())

    for letter in word.upper():
        index = 0
        for i in range(len(letters_list)):
            if letter in letters_list[i]:
                index = i
                score += points_list[index]

    if len(word) >= extra_points_min_length and len(word) <= extra_points_max_length:
        score += 8

    return score


def get_highest_word_score(word_list):
    dict_scores = {}
    list_ties = []
    highest_score = 0
    
    # Get total score for each word in word_list
    for word in word_list:
        score = score_word(word)
        dict_scores[word] = score

        if dict_scores[word] > highest_score:
            list_ties = [word]
            highest_score = dict_scores[word]
        elif dict_scores[word] == highest_score:
            list_ties.append(word)
    
    # Find top word amongst the words with the same high score
    top_word = list_ties[0]

    for tie_word in list_ties:
        if len(tie_word) == 10:
            top_word = tie_word
            break
        elif len(tie_word) < len(top_word):
            top_word = tie_word

    return top_word, highest_score