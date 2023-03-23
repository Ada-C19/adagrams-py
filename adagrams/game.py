import random

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
    available_letters =[]
    for letter, number in LETTER_POOL.items():
        letter_quantity = letter * number
        available_letters.append(letter_quantity)


    letter_string = ''.join(available_letters)
    list_letter_pool = list(letter_string)
    
    hand = []

    while len(hand) != 10:
        random_letter = random.choice(list_letter_pool)
        hand.append(random_letter)
        for letter in list_letter_pool:
            if letter in hand:
                list_letter_pool.remove(letter)
    return hand

    

def uses_available_letters(word, hand):
    word = word.upper()   
    for letter in word:
      if letter in hand and word.count(letter) < hand.count(letter):
        continue
      elif letter not in hand or word.count(letter) > hand.count(letter):
        return False
    return True
    

def score_word(word):

    score = 0
    bonus_point_list =[7,8,9,10]
    points_value = {'A': 1, 
                'E' : 1, 
                'I': 1, 
                'O': 1, 
                'U': 1,
                'L': 1, 
                'N': 1, 
                'R': 1, 
                'S': 1,
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
                'J':8,
                'X':8,
                'Q':10,
                'Z':10   
}
    for letter in word.upper():
      score += points_value[letter]
      if len(word) == 0:
        score = 0
    if len(word) in bonus_point_list:
        score = score + 8
    return(score) 
    

def get_highest_word_score(word_list):
    
    word_value_dictionary = {}
    score_list = []
    for word in word_list:
        score = score_word(word)
        # points_list.append(score)
        word_value_dictionary[word] = score
    
    highest_score = max(word_value_dictionary.values())
    for k,v in word_value_dictionary.items():
        if v == highest_score:
            score_list.append(k)
            score_list.append(highest_score)
    return tuple(score_list) 

