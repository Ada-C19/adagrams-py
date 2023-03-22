import random

def draw_letters():

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
    
    # Create pool of letters with frequency as outlined in letter_probability dict
    pool_of_letters = []
    for letter in letter_probability:
        pool_of_letters.extend([letter] * letter_probability[letter])

    # Choose a hand of 10 letters
    hand_of_letters = []

    while len(hand_of_letters) < 10:
        random_index = random.randint(0, len(pool_of_letters) - 1)
        random_letter = pool_of_letters[random_index]

    # Ensure no letter is overrepresented compared to letter_probability dict
        if hand_of_letters.count(random_letter) < letter_probability[random_letter]:
            hand_of_letters.append(pool_of_letters[random_index])

    return hand_of_letters


def uses_available_letters(word, letter_bank):
    word = word.upper()

    # Ensure that letters in word are available in correct quantities in hand
    for letter in word:
        if letter not in letter_bank or (word.count(letter) > letter_bank.count(letter)):
            return False
    return True


def score_word(word):

    point_dictionary = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"], 
    3: ["B", "C", "M", "P"], 
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
    }

    points = 0

    # Loop through word & dict to add points
    for letter in word.upper():
        for key, value in point_dictionary.items():
            if letter in value:
                points += key

    # Add extra points for words longer than 6
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

