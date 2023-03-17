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
    ada_gram = LETTER_POOL
    potato = []
    hand_as_list = []
    
    for k,v in ada_gram.items():
        for i in range(v):
            potato.append(k)

    while len(hand_as_list) < 10:
        random_letter = random.choice(potato)
        hand_as_list.append(random_letter)
        potato.remove(random_letter)

    return hand_as_list



def uses_available_letters(word, letter_bank):
    word_list = []
    for letter in word:
        word_list.append(letter.upper())

    letter_list = []
    for letters in letter_bank:
        letter_list.append(letters)


    for letter in word_list:
        if letter in letter_list:
            letter_list.remove(letter)
        else:
            return False
    return True

def score_word(word):
    # word is a string of characters
    # return integer represening the number of points
    # each letter within word has a point value. The number of points 
    # is summed up to represent the total score of word
    # ***if len of word is 7, 8, 9, or 10 then word gets additional 8 points
    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    score =  0

    for k,v in score_chart.items():
        for letter in word:
            if letter.upper() in v:
                score += k
    
    if len(word) in range(7,11):
        score += 8
    # print(score)
    return score

# def get_highest_word_score(word_list):
#     # word list is a list of strings
#     # must return a tuple that represents the data of winning word
#     # and its score: tuple should = ("word", score)
#     # if there is a tie, prefer word with fewest letters 
#     # unless one word has 10 letters.
#     # if there are multiple words that are same score
#     # and same length, pick the first one in supplied list