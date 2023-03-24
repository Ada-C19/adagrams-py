import random

# Function to draw 10 random letters from the letter pool

def draw_letters():
    LETTER_POOL = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
        'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
        'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

 # Create a list of letters with the frequency as specified in the pool
    letter_list = []
    for letter, count in LETTER_POOL.items():
        letter_list.extend([letter] * count)

    # Draw a random sample of 10 letters from the letter list
    hand = random.sample(letter_list, 10)
    
    return hand

# Function to check if the given word can be formed using the available letters
def uses_available_letters(word, letter_bank):
    word = word.upper()
        # Create a copy of the letter bank to avoid modifying the original

    letter_bank_copy = letter_bank.copy()

    # Iterate through each letter in the word
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False

    # If all letters are in the letter bank copy, the word is valid
    return True

def score_word(word):
    word = word.upper()
    letter_scores = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    score = 0
    for letter in word:
        score += letter_scores[letter]

    if 7 <= len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    # Calculate the score for each word in the word_list and store them as tuples
    word_scores = [(word, score_word(word)) for word in word_list]
    
    # Initialize the highest_word variable with the first word and its score
    highest_word = word_scores[0]

    # Iterate through the rest of the word_scores list (skipping the first element)
    for word, score in word_scores[1:]:
        # Check if the current word has a higher score than the highest_word
        if score > highest_word[1] or (
            # If the scores are equal, apply tie-breaking rules:
            score == highest_word[1] and (
                # If the current word has 10 letters and the highest_word doesn't, choose the current word
                (len(word) == 10 and len(highest_word[0]) != 10) or
                # If neither word has 10 letters, choose the word with fewer letters
                (len(highest_word[0]) != 10 and len(word) < len(highest_word[0]))
            )
        ):
            # Update the highest_word with the current word and its score
                    highest_word = (word, score)
        # If the scores are equal and the word lengths are also equal, use the order in the supplied list
        elif score == highest_word[1] and len(word) == len(highest_word[0]):
            # Check the index of the current word and highest_word in the original list
            # If the index of the current word is lower, update highest_word with the current word and its score
            highest_word = (word_list.index(word) < word_list.index(highest_word[0])) and (word, score) or highest_word

    # Return the highest_word tuple containing the winning word and its score
    return highest_word

def play_game():
    # Initialize an empty list to store all the words played
    all_words = []

    # Play 4 rounds of the game
    for i in range(4):
        # Draw a new hand of 10 letters
        hand = draw_letters()
        # Print the current hand
        print(f"Hand {i + 1}: {hand}")

        # Ask the user to input a word using the available letters
        word = input("Enter a word using the available letters: ")

        # Check if the input word is valid using the available letters
        if uses_available_letters(word, hand):
            # Calculate the score of the input word
            score = score_word(word)
            # Print the valid word and its score
            print(f"The word '{word}' is valid and has a score of {score}.")
            # Add the valid word to the list of all_words
            all_words.append(word)
        else:
            # Print an error message if the input word is not valid
            print(f"The word '{word}' is not valid.")

    # Calculate the highest scoring word and its score
    result = get_highest_word_score(all_words)
    if result:
        # result tuple into highest_word and highest_score variables
        highest_word, highest_score = result
        print(f"The highest scoring word is '{highest_word}' with a score of {highest_score}.")
if __name__ == "__main__":
    play_game()






