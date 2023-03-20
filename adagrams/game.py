import random
LETTER_QUANTITY = {
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
    # creates a list of ten randomized characters
    # uses pop and add back into the data structure of letters? 
    # maybe: make a list of all the letters, only occurring the allowed number of times and use a randomizing operator on it
    # iterate over the dictionary to make list
    
    master_letter_bank = []
    for letter, frequency in LETTER_QUANTITY.items():
        for i in range(frequency):
            master_letter_bank.append(letter)


    drawn_hand = []
    while len(drawn_hand) < 10:
        new_letter = random.choice(master_letter_bank)
        drawn_hand.append(new_letter)
        master_letter_bank.remove(new_letter)
        
    return drawn_hand


def uses_available_letters(word, letter_bank):
    #ensures user's word only uses letters from drawn_hand
    #loops through each character in the word and checks if it is in drawn_hand

    #also need to return false if a character is used too many times...
    #make a dictionary for drawn_hand that has letter and frequency to compare? 
    #use a new data type like set or tuple? 
    valid_word = False
    valid_frequency = False
    letter_frequency = {}
    max_frequency = {}
    for char in letter_bank:
        if char in max_frequency:
            max_frequency[char] +=1
        else:
            max_frequency[char] = 1
    

    for char in word:
        char = char.capitalize()
        if char not in letter_bank:
            valid_word = False
            break
        elif char in letter_bank:
            valid_word = True

        if char in letter_frequency:
            letter_frequency[char] += 1
        else:
            letter_frequency[char] = 1   

        # my question/where i am stuck!! 
        if letter_frequency[char]> max_frequency[char]:
            valid_frequency = False
            valid_word = False
        else:
            valid_word = True    

    return valid_word

#  taken from test files:  
#       letter_freq = {}
#         for letter in letters:
#             if letter in letter_freq:
#                 letter_freq[letter] += 1
#                 else:
#                     letter_freq[letter] = 1
#     return valid_word

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass