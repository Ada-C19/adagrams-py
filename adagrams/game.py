import random

def draw_letters():
    letters_list = []
    pool_of_letters_dict = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1

    }
    letter_freq = {}
    #letters_list.append(random.choice(list(pool_of_letters_dict.keys())))
    #return letters_list
  
    while len(letters_list) < 10:
        random_letter = (random.choice(list(pool_of_letters_dict.keys())))
        if random_letter in letter_freq:
            letter_freq[random_letter] += 1
            if letter_freq[random_letter] < pool_of_letters_dict[random_letter]:
                letters_list.append(random_letter)
        else:
            letter_freq[random_letter] = 1
            letters_list.append(random_letter)
    return letters_list

def uses_available_letters(word, letter_bank):
    upper_case_word = word.upper()
    letter_count = {}
  # key is letter, value is # of times letter is present
    for letter in letter_bank:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

        # letter_count = {'A': 2, 'X': 8}


    # in for loop, check if we have enough available letters 
    for letter in upper_case_word:
        if letter not in letter_bank or letter_count[letter] == 0:
            return False
        elif letter in letter_bank:
            letter_count[letter] -= 1
        
    return True



def score_word(word):
    upper_case_word = word.upper()
    total = 0
    score_chart = {"A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10

    }
    for letter in upper_case_word:
        total += score_chart[letter]

    if len(word) >= 7:
        total += 8
    
    return total
        #add up each letter and return totl
    #Returns an integer representing the number of points    
    #The number of points of each letter is summed up to represent the total score of word
    
    #If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    #if letter in word length is <= 7 +8

def get_highest_word_score(word_list):
    highest_score = 0
    high_scoring_word = ""
    for word in word_list:
      score = score_word(word)
      if score > highest_score:
        highest_score = score
        high_scoring_word = word
      elif highest_score == score:
        if len(high_scoring_word) == 10:
          high_scoring_word = high_scoring_word
        elif len(word) == 10:
            high_scoring_word = word      
        elif len(word) < len(high_scoring_word):
          high_scoring_word = word
    
    return (high_scoring_word, highest_score)
    #word_list is a list of strings
    #return a tuple that represents the data of a winning word and it's score RETURN DATA OF WINNING WORD AND THE POINT AS A TUPLE
    #The tuple must contain the following elements:
    # #index 0 ([0]): a string of a word
    # #index 1 ([1]): the score of that word

#     In the case of tie in scores, use these tie-breaking rules:
    #prefer the word with the fewest letters...
    #unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    #If the there are multiple words that are the same score and the same length, pick the first one in the supplied list