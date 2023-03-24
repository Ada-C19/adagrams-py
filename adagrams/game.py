import random
# ?What is your time complexity?
def draw_letters():

    ada_gram = {
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
    
    letter_pool = []
    hand_as_list = []
    # should this be skipped and the data structure begin in list format?
    for k,v in ada_gram.items():
        for i in range(v):
            letter_pool.append(k)

    while len(hand_as_list) < 10:
        random_letter = random.choice(letter_pool)
        hand_as_list.append(random_letter)
        letter_pool.remove(random_letter)

    return hand_as_list


def uses_available_letters(word, letter_bank):
    letter_list = []

    for char in letter_bank:
        letter_list.append(char)
    
    for letter in word:
        upper_letter = letter.upper()
        if upper_letter in letter_list:
            letter_list.remove(upper_letter)
        else:
            return False
    return True

# ?What is your time complexity#
def score_word(word):

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

    return score
# ?what is the time complexity?
def get_highest_word_score(word_list):
    winning_score = 0
    winning_word = ""

    for word in word_list:
        score = score_word(word)
        if score > winning_score:
            winning_score = score
            winning_word = word
        # could you add an and statment here???
        elif score == winning_score:
            if len(word) == 10 and len(winning_word) != 10:
                winning_word = word 
            elif len(word) != 10 and len(winning_word) == 10:
                winning_word = winning_word
            elif len(word) < len(winning_word):
                winning_word = word
            elif len(word) == len(winning_word):
                winning_word = winning_word
    return winning_word, winning_score