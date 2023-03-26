import random


def draw_letters():

    letters = {
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
# this variable holds all the letters to draw
    letter_box = []

 # loop through the dict
    for letter, number in letters.items():
        # loop and check if the letter actually matches the frequency being added
        for i in range(number):
            letter_box.append(letter)

        # this holds the 10 letters --
    letter_list = []

# looping through letters using random.choice and appends to the letter_list
    for letters in range(10):
        letter = random.choice(letter_box)
        letter_list.append(letter)
    # remove will prevent from creating duplicates to be added 
        letter_box.remove(letter)
    return letter_list


def uses_available_letters(word, letter_bank):

    # letter_list = []
    # word_len = len(word)
    # letter_len = len(letter_list)

    # word = word.lower()

    # create an empty dictionary
    letter_frequency = {}

    # lloop through the letter_bank
    for each_letter in letter_bank:
        # get the currrent count of each letter as value increments by 1 and and defaults 0 if non-existent

        letter_frequency[each_letter.lower()] = letter_frequency.get(
            each_letter.lower(), 0) + 1
        
        #long way 

        # if each_letter in letter_frequency:
        #     letter_frequency[each_letter.lower()] += 1

        # else:
        #     letter_frequency[each_letter.lower()] = 1

    for each_letter in word:
        # if both conditions arre met, return False
        if each_letter.lower() not in letter_frequency:
            return False
        if letter_frequency[each_letter.lower()] <= 0:
            return False
# prevents from overuse -- signals that letter has been used up, minus 1
        letter_frequency[each_letter.lower()] -= 1

    return True


def score_word(word):

    total_score = 0
    # word_len = len(word)
    

    letter_set_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    letter_set_2 = ["D", "G"]
    letter_set_3 = ["B", "C", "M", "P"]
    letter_set_4 = ["F", "H", "V", "W", "Y"]
    letter_set_5 = ["K"]
    letter_set_6 = ["J", "X"]
    letter_set_7 = ["Q", "Z"]

    #    #convert since letters in sets are uuppercase
    cased_word = word.upper()


# looping through the word and check if any of the letter are in the sets and update the score
    for each_letter in cased_word:
        if each_letter in letter_set_1:
            total_score += 1
        elif each_letter in letter_set_2:
            total_score += 2
        elif each_letter in letter_set_3:
            total_score += 3
        elif each_letter in letter_set_4:
            total_score += 4
        elif each_letter in letter_set_5:
            total_score += 5
        elif each_letter in letter_set_6:
            total_score += 8
        elif each_letter in letter_set_7:
            total_score += 10

# check if 7 or more letters and increase score by 8
    if len(cased_word) >= 7:
        total_score += 8

    return total_score


def get_highest_word_score(word_list):
    # InItialize the maxi score to 0 as a startng point
    max_score = 0

    # empty list store the best word with highest score
    best_word = []
    
# boolean to chesck if there's a 10 letter word
    is_ten_letter_word = False
 
#loop
    for each_word in word_list:
        # instant winner here -- hceck first if there'a ten-letter word, exit
        if len(each_word) == 10:
            is_ten_letter_word = True
            break
    # use helper function here to extract score
    for each_word in word_list:
        current_score = score_word(each_word)
# compare scores
        if current_score > max_score:
            max_score = current_score
            best_word = each_word
# reminder -- check if current score and max_score are same
# if scores are tied, between current word and current best word has 10 --  updates the best word
        elif current_score == max_score:
            if len(each_word) == 10 and len(best_word) != 10:
                best_word = each_word
#  if best word is not a ten letter word and len is less than the current word, update best word
            elif len(each_word) < len(best_word) and len(best_word) < 10:
                best_word = each_word

    return best_word, max_score


