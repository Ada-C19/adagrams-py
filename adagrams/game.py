import random
import string

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
    ten_letters = []    
    while len(ten_letters) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        if LETTER_POOL[random_letter] > 0:
            LETTER_POOL[random_letter] -= 1
            ten_letters.append(random_letter)

    return ten_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]

    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    

    return True

def score_word(word):
    #bring in table with scores as a dictionary
    score_chart = {
        "A":1,
        "E":1,
        "I":1,
        "O":1,
        "U":1,
        "L":1,
        "N":1,
        "R":1,
        "S":1,
        "T":1,
        "D":2,
        "G":2,
        "B":3,
        "C":3,
        "M":3,
        "P":3,
        "F":4,
        "H":4,
        "V":4,
        "W":4,
        "Y":4,
        "K":5,
        "J":8,
        "X":8,
        "Q":10,
        "Z":10
    }
    total_points = 0
    if len(word) >= 7:
        total_points += 8

    for letter in word:
        letter = letter.upper()
        print(letter)
        if letter in score_chart:
            print("score_chart:",score_chart[letter])
        #add that value (Score) to total_points
            total_points += score_chart[letter]
            # print(f'total_points:{total_points}')
    print(f'total_points:{total_points}')
    return total_points

def get_highest_word_score(word_list):
    pass

