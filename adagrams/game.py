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
    # Input: list of strings, diff words
    # Output: list or tuple with word and the score

    word_dict = {}
    winner = []

    for word in word_list:
        # Check if word isn't in the dict already, add its length and score to dict 
        if word not in word_dict:
            word_dict[word] = [len(word), score_word(word)]
    print(word_dict)

    # Get a list of all the scores 
    scores = []
    for value in word_dict.values():
        scores.append(value[1])
    print(scores)

    # Find the highest score 
    highest_score = max(scores)
    print(highest_score)

    # Find the lengths of with the the highest score 
    lengths_with_highest_scores = []

    for value in word_dict.values():
        if value[1] == highest_score:
            lengths_with_highest_scores.append(value[0])

    print(lengths_with_highest_scores)

    # Find the shortest word with the highest score
    shortest_highest = min(lengths_with_highest_scores)
    print(f"Shortest and highest: {shortest_highest}")

    for word, len_and_score in word_dict.items():
        length = len_and_score[0]
        score = len_and_score[1]

        if score == highest_score and length == 10:
            winner.append(word)
            winner.append(score)
        
        elif score == highest_score and length == shortest_highest:
            winner.append(word)
            winner.append(score)
    
    print(f"Winner: {winner}")
    return winner


        # elif multiple words have the same score:
            # if there is a 10-letter word:
                # the 10-letter word wins
            # elif there is a word with fewer letter:
                # shorter word wins


    # In the case of tie in scores, use these tie-breaking rules:
        # prefer the word with the fewest letters...
        # ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
        # If the there are multiple words that are the same score and the same length, pick the first one in the supplied list

get_highest_word_score(["WWW", "MMMM", "BBBBBB", "AAAAAAAAD", "JQ", "KFHK"])