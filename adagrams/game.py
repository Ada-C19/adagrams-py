import random

POOL = {
    "A":9,
    "B":2,
    "C":2,
    "D":4,
    "E":12,
    "F":2,
    "G":3,
    "H":2,
    "I":9,
    "J":1,
    "K":1,
    "L":4,
    "M":2,
    "N":6,
    "O":8,
    "P":2,
    "Q":1,
    "R":6,
    "S":4,
    "T":6,
    "U":4,
    "V":2,
    "W":2,
    "X":1,
    "Y":2,
    "Z":1
}

def draw_letters():
    pool_list = []
    chosen_letters = []

    for key in POOL:
        counter = POOL[key]
        while counter > 0:
            pool_list.append(key)
            counter -= 1

    while len(chosen_letters) < 10:
        letter = random.choice(pool_list)
        index = pool_list.index(letter)
        pool_list.pop(index)
        chosen_letters.append(letter)
    
    return chosen_letters

def uses_available_letters(word, letter_bank):
    letters = []
    word_cap = word.upper()

    for i in range(0,len(word_cap)):
        letters.append(word_cap[i])

    count_if_false = 0

    for letter in letters:
        if letter not in letter_bank:
            count_if_false += 1
        elif letters.count(letter) > letter_bank.count(letter):
            count_if_false += 1
        else:
            continue

    if count_if_false == 0:
        return True
    else:
        return False

def score_word(word):
    score = 0
    word = word.upper()
    one_point_letters = ["A","E","I","O","U","L","N","R","S","T"]
    two_point_letters = ["D","G"]
    three_point_letters = ["B","C","M","P"]
    four_point_letters = ["F","H","V","W","Y"]
    five_point_letters = ["K"]
    eight_point_letters = ["J","X"]
    ten_point_letters = ["Q","Z"]

    for letter in word:
        if letter in one_point_letters:
            score +=1
        elif letter in two_point_letters:
            score+=2
        elif letter in three_point_letters:
            score+=3
        elif letter in four_point_letters:
            score+=4
        elif letter in five_point_letters:
            score+=5
        elif letter in eight_point_letters:
            score+=8
        else:
            score += 10
    
    if len(word) >= 7:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    pass