import random 

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

LETTER_SCORE = {
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
    available_letters = []
    ten_random_letters = []

    # I am iterating through each letter and number in the dictionary so that I can
    # get a list (available_letters) showing all available letters. 
    for letter, number in LETTER_POOL.items():
        available_letters.extend([letter]*number)


    while len(ten_random_letters) < 10:
        one_random_letter = random.choice(available_letters)
        ten_random_letters.append(one_random_letter)
        available_letters.remove(one_random_letter)
    
    return ten_random_letters

# using list comprehention for the function above +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def draw_letters():
#     available_letters = [letter for letter, number in LETTER_POOL.items() for i in range(number)]
#     ten_random_letters = [random.choice(available_letters) for i in range(10)]
#     return ten_random_letters
# ------------------------------------------------------------- 

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    word = word.upper()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

    
def score_word(word):
    word_score = 0

    for letter in word:
        word_score += LETTER_SCORE[letter.upper()]

    if len(word) >= 7:
            word_score += 8 
    return word_score

def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = ""
    for word in word_list:
        current_score = score_word(word) 
        if current_score > highest_score:
            highest_score = current_score
            winning_word = word
        
        # Conditonals for tie breaker rules
        elif current_score == highest_score and len(winning_word) != 10:
            if len(word) == 10 or len(word) < len(winning_word):
                winning_word = word
                highest_score = current_score

    return (winning_word, highest_score)