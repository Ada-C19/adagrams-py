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
    
    #iterates over LETTER_QUANTITY dict to make a list of all letters with exact occurrences
    master_letter_bank = []
    for letter, frequency in LETTER_QUANTITY.items():
        for i in range(frequency):
            master_letter_bank.append(letter)

    # uses a randomizing operator on above list and removes that letter from the list so it cannot be reselected
    drawn_hand = []
    while len(drawn_hand) < 10:
        new_letter = random.choice(master_letter_bank)
        drawn_hand.append(new_letter)
        master_letter_bank.remove(new_letter)

    #result is a list with ten selected letters for user's hand    
    return drawn_hand


def uses_available_letters(word, drawn_hand):

    #makes a dictionary called max_frequency from drawn_hand that has letter and frequency
    valid_word = False
    valid_frequency = False
    letter_frequency = {}
    max_frequency = {}
    for char in drawn_hand:
        if char in max_frequency:
            max_frequency[char] +=1
        else:
            max_frequency[char] = 1
    
    #ensures input will be converted to capital letters
    #returns false if word uses incorrect characters not given in drawn_hand
    for char in word:
        char = char.capitalize()
        if char not in drawn_hand:
            return False
        elif char in drawn_hand:
            valid_word = True
        #populates to letter_frequency to check repeat letter usage
        if char in letter_frequency:
            letter_frequency[char] += 1
        else:
            letter_frequency[char] = 1   

        #compares to max_frequency to ensure letters are not used too many times
        if letter_frequency[char]> max_frequency[char]:
            return False
        else:
            valid_word = True    

    return valid_word


def score_word(word):
    #step one: iterate through each character and add each point value to total
    #step two: check if word length is 7-10 characters and add 8 extra points if so
    point_total = 0
    for char in word:
        char = char.capitalize()
        point_total += LETTER_POINT_SYSTEM[char]
    if len(word) >= 7:
        point_total += 8    
    return point_total    



def get_highest_word_score(word_list):
    
    #creates a dictionary of each word in word_list, with its points as values
    word_score_log = {}
    for word in word_list:
        word_score_log[word] = score_word(word)   
    top_score = max(word_score_log.values()) 

    #in the event of a tie: prefer word with fewest letters OR 10 letters
    #if same score and length, pick the first occurring word
    tied_words = []
    for word, score in word_score_log.items():
        if score == top_score:
            tied_words.append(word)
        
    current_winning_word = tied_words[0]
    for word in tied_words:
        if len(tied_words) == 1:
            return (word, word_score_log[word])
        if len(word) == 10:
            return (word, word_score_log[word])
        elif len(word) < len(current_winning_word):
            current_winning_word = word
            
    return (current_winning_word, score)

