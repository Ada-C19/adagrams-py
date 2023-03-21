import random

from collections import Counter

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
  #empty list of all letters
    list_of_letters = []
       
    for letter, frequency in LETTER_POOL.items():
        total_times_letter_appears = 0
        while total_times_letter_appears < frequency:
            list_of_letters.append(letter)
            total_times_letter_appears += 1
    
    letters = []
# Randomly choose a letter from the list aboveclear

    while len(letters) < 10:
        random_letter = random.choice(list_of_letters)
        # if random_letter in list_of_letters:
        list_of_letters.remove(random_letter)
        letters.append(random_letter)
        # else:
        #     continue

    #return letters which is a list of 10 letters
    return letters 

def uses_available_letters(word, letter_bank):
    
    letter_bank_copy = list(letter_bank)

    for letter in word.upper():
        if  letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

    
def score_word(word):
    # score_chart:
    one_pt_letters = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    two_pt_letters = ['D', 'G']
    three_pt_letters = ['B', 'C', 'M', 'P']
    four_pt_letters = ['F', 'H', 'V', 'W', 'Y']
    five_pt_letters = ['K']
    eight_pt_letters = ['J', 'X']
    ten_pt_letters = ['Q','Z']
    
    score = 0
    
    if len(word) >= 7:
        score += 8
    
    for letter in word.upper():
        if letter in one_pt_letters:
            score += 1
        elif letter in two_pt_letters:
            score += 2
        elif letter in three_pt_letters:
            score += 3
        elif letter in four_pt_letters:
            score += 4
        elif letter in five_pt_letters:
            score += 5
        elif letter in eight_pt_letters:
            score += 8
        elif letter in ten_pt_letters:
            score += 10
        elif letter == "": 
            return 0


    return score

def get_highest_word_score(word_list):
      
  scores_dict = {}

  for word in word_list:
    scores_dict[word] = score_word(word)

  high_score = 0
  shortest_word = ""
  for word, score in scores_dict.items():
    if score > high_score:
        high_score = score
        shortest_word = word
    elif score == high_score:
        if len(shortest_word) == 10:
            shortest_word = shortest_word
        elif len(word) == 10:
            shortest_word = word
        elif len(word) < len(shortest_word):
            shortest_word = word

        

    #1st highest up word with 10 charac.
    #2nd current word with 10 characters
    #3rd shortest word
    
  
  winning_score = (shortest_word, high_score)

  
  return winning_score