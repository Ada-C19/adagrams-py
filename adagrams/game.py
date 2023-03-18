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
    # array for taking in the strings after calculation, letters array, probability array
    drawn_letters = []
    letters = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    probability = []
    counter = 0
    # calculating probability - makes a numpy array
    for key in LETTER_POOL:
        p = LETTER_POOL[key]
        probability.append(p)
    # this below 2 lines is honestly from stockoverflow - it turns the probability array into an np array and makes the sum closer to 1 without altering the rates (didn't come up with it but I understood it when I saw it)
    probs = np.array(probability)
    probs_scaled = probs / probs.sum()
    # adding letters to the drawn_letters(the array to be returned) as strings. numpy nests results...
    while counter < 10:
        random_letter = str(np.random.choice(letters, 1, p=probs_scaled)[0])
        # if the letter already exists, skip iteration
        if str(random_letter) in drawn_letters:
            continue
        else:
            drawn_letters.append(random_letter)
            counter += 1
    print(drawn_letters)

    # result = []
    # str_arr = drawn_letters
    # for char in str_arr:
    #     result.append(str(char))
    return drawn_letters


# draw_letters()


    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass