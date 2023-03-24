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
    tiles = [] #list that's ten letters
    count = 0 #going to stop at 10
    letters_dict = LETTER_POOL.copy()
    while count != 10:
        letter = random.choice(list(letters_dict.keys()))
        if letters_dict[letter] > 0:
            letters_dict[letter] -= 1
            tiles.append(letter)
            count += 1
        else:
            continue
    return tiles
        

def uses_available_letters(word, letter_bank):
    letter_bank_dict = {}
    word_dict = {}
    word = word.upper()

    for letter in letter_bank:
        if letter not in letter_bank_dict:
            letter_bank_dict[letter] = 1
        else:
            letter_bank_dict[letter] += 1

    for character in word:
        if character not in letter_bank:
            return False
        else:
            if character not in word_dict:
                word_dict[character] = 1
            else:
                word_dict[character] += 1

    for characters in word_dict:
        if word_dict[characters] > letter_bank_dict[characters]:
            return False
    return True
        
def score_word(word):
    point_values = {
        "A" : 1,
        "B" : 3,
        "C" : 3,
        "D" : 2,
        "E" : 1,
        "F" : 4,
        "G" : 2,
        "H" : 4,
        "I" : 1,
        "J" : 8,
        "K" : 5,
        "L" : 1,
        "M" : 3,
        "N" : 1,
        "O" : 1,
        "P" : 3,
        "Q" : 10,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "U" : 1,
        "V" : 4,
        "W" : 4,
        "X" : 8,
        "Y" : 4,
        "Z": 10,
    }
    total_points = 0
    word = word.upper()
    
    if len(word) >= 7:
        total_points += 8

    for letter in word:
        letter_point_amount = point_values[letter] 
        total_points += letter_point_amount
    return total_points
    

def get_highest_word_score(word_list):
    words_points = {}
    for word in word_list:
        points = score_word(word)
        if points not in words_points.keys():
            words_points[points] = [word]
        else:
            words_points[points].append(word)
    
    highest_key = max(words_points.keys())
    highest_words_list = words_points[highest_key] 

    current_winner = highest_words_list[0]
    for index in range(1, len(highest_words_list)):
        if len(current_winner) == 10:
            return (current_winner, highest_key)
        elif len(highest_words_list[index]) == 10:
            return (highest_words_list[index], highest_key)
        elif len(current_winner) > len(highest_words_list[index]):
            current_winner = highest_words_list[index]
    return (current_winner, highest_key)

        
    
        

    




draw_letters()
