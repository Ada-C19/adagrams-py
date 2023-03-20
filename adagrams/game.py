import random

def draw_letters():
    pool_of_letters = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "X"]

    letter_probability = {
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

    hand_of_letters = []
    count = 0

    while count < 10:
        random_index = random.randint(0, len(pool_of_letters) - 1)
        random_letter = pool_of_letters[random_index]

        if hand_of_letters.count(random_letter) >= letter_probability[random_letter]:
            continue
        else:
            hand_of_letters.append(pool_of_letters[random_index])
            count += 1

    return hand_of_letters


def uses_available_letters(word, letter_bank):
    word = word.upper()

    for letter in word:
        if letter in letter_bank and (word.count(letter) <= letter_bank.count(letter)):
            continue
        else:
            return False
    return True

def score_word(word):

    one_point = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    two_points = ["D", "G"] 
    three_points = ["B", "C", "M", "P"] 
    four_points = ["F", "H", "V", "W", "Y"]
    five_points = ["K"]
    eight_points = ["J", "X"]
    ten_points = ["Q", "Z"]
    
    word = word.upper()
    points = 0

    for letter in word:
        if letter in one_point:
            points += 1
        elif letter in two_points:
            points += 2
        elif letter in three_points:
            points += 3
        elif letter in four_points:
            points += 4
        elif letter in five_points:
            points += 5
        elif letter in eight_points:
            points += 8
        elif letter in ten_points:
            points += 10
    
    if len(word) > 6:
        points += 8

    return points


def get_highest_word_score(word_list):

    original_word_list_order = word_list.copy()
    word_list.sort(key=len)

    words_and_scores = {word: score_word(word) for word in word_list}
  
    top_score = max(words_and_scores.values())
    top_scoring_words = [key for key, value in words_and_scores.items() if value == top_score]

    if len(top_scoring_words) == 1:
        # only one top score
        return top_scoring_words[0], top_score
    
    else:
        # more than one word with top score

        # one or more words have 10 letters, return first instance
        if len(word_list[-1]) == 10:
            for word in original_word_list_order:
                if len(word) == 10:
                    return word, words_and_scores[word]
        
        else:
        # multiple words with same score and same length, return first instance
            return word_list[0], words_and_scores[word_list[0]]

