# import numpy
import random
# letter pool copied from test_wave_01. using for probability calculations.
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



# draw_letters_function
def draw_letters():   
    # initializing variables: drawn_letters("hand"), letters array, probability array, counter
    drawn_letters = []
    letters = list(LETTER_POOL.keys())
    probability = list(LETTER_POOL.values())
    counter = 0
    # adding letters to the drawn_letters(the array to be returned) as strings. random.choices nests each element so to access just the letters I'm using [0]
    while counter < 10:
        random_letter = random.choices(letters, weights=probability,k=1)[0]
        # if the letter already exists, skip iteration for no dupes. else continue on until there are 10 letters
        if random_letter in drawn_letters:
            continue
        else:
            drawn_letters.append(random_letter)
            counter += 1
    # return the drawn letters("hand")
    return drawn_letters



def uses_available_letters(word, letter_bank):
    # initializing variable: counter for counting charcters in word that exist in letter_bank
    letter_count = 0
    # copy of letter_bank since direct modification is discouraged according to test_wave_02
    letter_bank_copy = letter_bank[:]
    # since letter_bank uses capital letters
    word = word.upper()
    # check if letter in word are in letter_bank_copy
    for char in word:
        # if character in word is in letter_bank_copy, increment counter and remove that character from letter_bank_copy
        if char in letter_bank_copy:
            letter_count += 1
            letter_bank_copy.remove(char)
    # once the loop ends and letter count is equal to the length of the word, that means all the letters in word were in letter_bank so return True
    if letter_count == len(word):
        return True     
    # otherwise return False
    return False



# Score Chart from README
score_chart = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
    ('D', 'G'): 2,
    ('B', 'C', 'M', 'P'): 3,
    ('F', 'H', 'V', 'W', 'Y'): 4, 
    ('K'): 5,
    ('J', 'X'): 8,
    ('Q', 'Z'): 10
}



def score_word(word):
    total = 0
    word = word.upper()
    # extra points for longer words
    if len(word) >= 7:
        total += 8
    # loop through each letter
    for letter in word:
    # loop through dictionary to find the letter
        for key, val in score_chart.items():
    # if the letter is in the tuple that is the dictionary key, add the value (score) to the total
            if letter in key:
                total += val
    # return total
    return total



def get_highest_word_score(word_list):
    #initializing variables: best scoring word & best score, ties list
    best_score_word = ""
    best_score = 0
    ties = []
    # iterate through words in word list
    for word in word_list:
        # score of the word (using score_word function to calculate)
        current_score = score_word(word)
        # if word length > 9, return that word ASAP
        if len(word) > 9:
            return (word, current_score)
        # else if, current word's score > the last best score, then update the best_score and best scoring word accordingly
        elif current_score > best_score:
            best_score_word = word
            best_score = current_score
        # else if 2, if current score is equal to the best score, stash current word in the ties list
        elif current_score == best_score:
            ties.append(word)
    # if there's anything in ties list,
    if len(ties):
        # loop through the list
        for word in ties:
            # if length of the tying word is shorter than current best word, set the shorter word as the new best word
            if len(word) < len(best_score_word):
                best_score_word = word
    # return the best scoring word and its score
    return [best_score_word, best_score]