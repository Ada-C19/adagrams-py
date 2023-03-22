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


def draw_letters():   
    # Store the quantity of each letter in the pool and the count of each letter in these 2 lists
    counts = []
    letters = []

    # Get the letters and how many of each letter there are in the pool
    for letter, count in LETTER_POOL.items():
        letters.append(letter)
        counts.append(count)
        
    # Draw a hand of 10 letters from the letter pool
    hand = random.sample(letters, counts=counts, k=10)

    return hand
    

# Helper functions
def count_letter_frequency(sequence):
    letter_frequency = {}
    for letter in sequence:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    
    return letter_frequency


def convert_case(sequence):
    converted_sequence = ""
    for letter in sequence:
        converted_sequence += letter.upper()
    
    return converted_sequence


def uses_available_letters(word, letter_bank):
    # Convert case on the word string and the letter bank list
    word = convert_case(word)
    letter_bank = convert_case(letter_bank)
    
    # Iterate through the letters in the word to check if they're in the letter bank
    for letter in word:
        if letter not in letter_bank:
            return False
    
    # Check how many times a letter occurs in the word and the letter bank
    frequency_word = count_letter_frequency(word)
    frequency_bank = count_letter_frequency(letter_bank)
    
    # Compare the word frequency in the word and the letter bank
    for letter in word:
        if not (frequency_word[letter] <= frequency_bank[letter]):
            return False  
    
    return True


def score_word(word):
    points_total = 0
    word = convert_case(word)

    score_chart = {
        "A": 1,
        "E": 1, 
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10,
    }
    
    # If the string is empty
    if not word:
        return 0
    
    # Add up the points by looking up each letter in word in the score_chart dict
    for letter in word:
        points_total += score_chart[letter]

    if len(word) > 6:
        points_total += 8

    return points_total


def get_highest_word_score(word_list):
    word_dict = {}

    for word in word_list:
        # Check if word isn't in the dict already, add its length and score to dict 
        if word not in word_dict:
            word_dict[word] = [len(word), score_word(word)]

    # Get a list of all the scores 
    scores = [len_score[1] for len_score in word_dict.values()]

    # Find the highest score 
    highest_score = max(scores)

    # Find the lengths of with the the highest score 
    lengths_with_highest_scores = []

    for len_score in word_dict.values():
        if len_score[1] == highest_score:
            lengths_with_highest_scores.append(len_score[0])

    # Find the shortest word length with the highest score
    shortest_highest = min(lengths_with_highest_scores)

    for word, value in word_dict.items():
        length = value[0]
        score = value[1]

        if score == highest_score and length == 10:
            return word, score
        
    for word, value in word_dict.items():
        length = value[0]
        score = value[1]
        
        if score == highest_score and length == shortest_highest:
            return word, score

