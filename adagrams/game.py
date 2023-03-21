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
LETTER_POINT_SYSTEM = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
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


        if letter_frequency[char]> max_frequency[char]:
            valid_frequency = False
            valid_word = False
        else:
            valid_word = True    

    return valid_word


def score_word(word):
    #takes in the valid word and returns an intger representing points
    #points calculated by adding up each letter's point values
    #step one: irtate through each character and += each point value
    #step two: check if word length is 7-10 characters and add 8 extra points if so
    point_total = 0
    for char in word:
        char = char.capitalize()
        point_total += LETTER_POINT_SYSTEM[char]
    if len(word) >= 7:
        point_total += 8    
    return point_total    



def get_highest_word_score(word_list):
    #takes in word_list, a list of strings
    #calculate score of each word in list
    #in the event of a tie: prefer word with fewest letters OR 10 letters
    #if same score and length, pick the first one to occur
    #return tuple with (string word, score)

    # LIST METHOD
    points_list = []
    for word in word_list:
        points_list.append(score_word(word))
    for i in len(points_list):
        top_score = max(points_list)
        

       

    # DICTIONARY METHOD
    # word_score_log = {}
    # for word in word_list:
    #     word_score_log[word] = score_word(word)
    # top_score = max(word_score_log.values()) 
    # print(top_score) 
    # top_score_word = 

    # best_word = (word_score_log.values().index(top_score), top_score)  



