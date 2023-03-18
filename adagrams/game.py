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
    # score_chart = {
    #     ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    #     ("D", "G"): 2,
    #     ("B", "C", "M", "P"): 3,
    #     ("F", "H", "V", "W", "Y"): 4,
    #     ("K"): 5,
    #     ("J", "X"): 8,
    #     ("Q", "Z"): 10,
    # }
    # # Get the value of "A"
    
    word = convert_case(word)

    for letter in word:
        if not word:
            return 0
        
        if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U" or letter == "L" or letter == "N" or letter == "R" or letter == "S" or letter == "T":
            points_total += 1

        if letter == "D" or letter == "G":
            points_total += 2

        if letter == "B" or letter == "C" or letter == "M" or letter == "P":
            points_total += 3

        if letter == "F" or letter == "H" or letter == "V" or letter == "W" or letter == "Y":
            points_total += 4

        if letter == "K":
            points_total += 5

        if letter == "J" or letter == "X":
            points_total += 8

        if letter == "Q" or letter == "Z":
            points_total += 10

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
