import random

LETTER_POOL = {
    "A":9, "B":2, "C":2, "D":4, "E":12, "F":2, "G":3, "H":2,
    "I":9, "J":1, "K":1, "L":4, "M":2, "N":6, "O":8, "P":2,
    "Q":1, "R":6, "S":4, "T":6, "U":4, "V":2, "W":2, "X":1,
    "Y":2, "Z":1
}

LETTER_VALUES = {
   "A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4,
    "I":1, "J":8, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3,
    "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8,
    "Y":4, "Z":10 
}

def draw_letters():
    letters = [] 
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency): # loop through the frequency of each letter to make sure no over drawing
            letters.append(letter) # add into the list 
    selected_letters = []
    for i in range(10):
        letter = random.choice(letters)
        selected_letters.append(letter)
        letters.remove(letter) # use remove method to avoid over drawing letters from letters list
    return selected_letters 
        

def uses_available_letters(word, letter_bank):
    letters = list(letter_bank) # make another copy of the letter_bank to avoid modify original letter bank  
    for letter in word.upper(): # use .upper() to handle lower case letters
        if letter not in letters: # if any letter from the word is not in the letter_bank, just return False
            return False
        letters.remove(letter) # removed the letter is being used to keep track of which letters are used to form the given word
    return True


def score_word(word):
    score = 0
    for letter in word.upper(): # handle the lower case letters
        score += LETTER_VALUES[letter] # adding up the letter values 
    if len(word) >= 7: # extra 8 points if the word length is >= 7
        score += 8
    return score 


def get_highest_word_score(word_list):
    # step 1: find highest words

    highest_score = 0
    highest_word_list = [] # create a list to store only the highest socre word
    for word in word_list:
        score = score_word(word) # call score_word function and assigned to score
        if score > highest_score:
            highest_score = score
            highest_word_list = [word] # replace the position in the list with highest score word each time 
        elif score == highest_score: # if there are multiple same highest score word, just add them into the list
            highest_word_list.append(word)


    # step 2: find the winner word from highest_word_list

    min_word = highest_word_list[0] # set the first word in the list and assume it's the shortest word 
    min_len = len(min_word) 
    for word in highest_word_list:
        if len(word) == 10: # if the word length is 10, directly return it 
            return (word, highest_score)
        elif len(word) < min_len: # if the word is shorter than the first one in the list, replace the position 
            min_len = len(word)   # update the length
            min_word = word       # update the word to the shortest word      
    return (min_word, highest_score) 


