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

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass