import random
import string

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
    hand = []
    # Randomly choose 10 letters and add to the list
    while len(hand) < 10:
        random_letter = random.choice(string.ascii_uppercase)

        # Count the number of random_letter currently in hand
        count = 0
        for letter in hand:
            if letter == random_letter:
                count += 1
        
        # Add random_letter to hand if conditions met
        if count < LETTER_POOL[random_letter]:
            hand.append(random_letter)
        
    return hand

def uses_available_letters(word, letter_bank):
    word = word.upper() # Avoid errors due to case sensitivity
    temp_letter_bank = letter_bank.copy() # Copy of letter_bank to avoid changing the original list

    # Check availability of each letter in word
    for i in range(len(word)):
        user_letter = word[i]
        available = False

        for letter in temp_letter_bank:
            if user_letter == letter:
                available = True
                temp_letter_bank.remove(letter) # Remove the letter from temp_letter_bank if it's already used in word
        
        # Return False if a letter in word not in temp_letter_bank
        if available == False:
            return False

    return True

LETTER_POINT = {
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

def score_word(word):
    word = word.upper()

    # Calculate total points
    if word:
        n = len(word)
        
        # Additional 8 points if word has 7 or more letters 
        if n > 6:
            points = 8
        else:
            points = 0

        # Loop through each letter and calculate total points
        for i in range(n):
            points += LETTER_POINT[word[i]]
    else:
        points = 0
    
    return points

def get_highest_word_score(word_list):
    word_score_list = [] # List of tuples of words and scores
    score_list = [] # List of scores only

    # Calculate each word's score and add to word_score_list of tuples and score_list
    for word in word_list:
        score = score_word(word)
        score_list.append(score) 
        word_score_list.append((word,score)) 
    
    # Find the maximum score
    max_score = max(score_list)

    # Find tuples of words with the highest score and add it to the highest score word list
    highest_score_word = []

    for word_score in word_score_list:
        if word_score[1] == max_score:
            highest_score_word.append(word_score)
    
    # Find THE highest score word from the list of highest score words

    # if there is only one tuple in the list, return the tuple, otherwise
    if len(highest_score_word) == 1:
        return highest_score_word[0]
    
    # If there are more than 1, apply the rules to choose the highest score word
    # Return the first word that has 10 letters, if any
    for word_score in highest_score_word:
        if len(word_score[0]) == 10:
            return word_score
        
    # Filter out the list to contain only word(s) with the least letters
    while len(highest_score_word) > 1:

        for i in range(len(highest_score_word) - 1):
            word_score = highest_score_word[i]
            next_word_score = highest_score_word[i+1]
            
            if len(word_score[0]) > len(next_word_score[0]):
                highest_score_word.remove(word_score)
    
    # Return the first tuple in the list
    return highest_score_word[0]