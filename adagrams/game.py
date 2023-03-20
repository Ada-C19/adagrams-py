# import numpy
import numpy as np
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
    # initializing variables: array for taking in the strings after calculation(drawn_letters), letters array, probability array, counter
    drawn_letters = []
    letters = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    probability = []
    counter = 0
    # calculating probability
    for key in LETTER_POOL:
        p = LETTER_POOL[key]
        probability.append(p)
    # the below 2 lines are honestly from stockoverflow - it turns the probability array into an np array and makes the sum closer to 1 without altering the rates (didn't come up with it but I sort of understand it...ish)
    probs = np.array(probability)
    probs_scaled = probs / probs.sum()
    # adding letters to the drawn_letters(the array to be returned) as strings. didn't know that numpy nests all results (first time using numpy, not a fan of their doucmentation style)
    while counter < 10:
        random_letter = str(np.random.choice(letters, 1, p=probs_scaled)[0])
        # if the letter already exists, skip iteration for no dupes. else continue on until there are 10 letters
        if str(random_letter) in drawn_letters:
            continue
        else:
            drawn_letters.append(random_letter)
            counter += 1
    return drawn_letters



def uses_available_letters(word, letter_bank):
    # an array for determining whether letters of word exists in letter_bank
    true_false = []
    # copy of letter_bank since direct modification is discouraged according to test_wave_02
    letter_bank_copy = letter_bank[:]
    # since letter_bank uses capital letters
    word = word.upper()
    # check if letter in word are in letter_bank_copy
    for char in word:
        if char in letter_bank_copy:
        # if it does exist, append 'true' and remove letter from letter_bank_copy to avoid using that letter multiple times
            true_false.append('true')
            letter_bank_copy.remove(char)
        else:
        # if it doesn't exist, append 'false'
            true_false.append('false')
    # if any instance of 'false' is in the true_false list, return False
    if 'false' in true_false:
        return False
    # or else, if all that exists in the true_false array is 'true', return True
    return True        



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