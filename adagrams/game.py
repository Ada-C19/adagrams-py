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
    word_scores = [(word, score_word(word)) for word in word_list]
    highest_word = word_scores[0]

    for word, score in word_scores[1:]:
        if score > highest_word[1] or (
            score == highest_word[1] and
            (len(word) == 10 and len(highest_word[0]) != 10) or
            (len(highest_word[0]) != 10 and len(word) < len(highest_word[0]))
        ):
            highest_word = (word, score)
        elif score == highest_word[1] and len(word) == len(highest_word[0]):
            highest_word = (word_list.index(word) < word_list.index(highest_word[0])) and (word, score) or highest_word

    return highest_word


def play_game():
    all_words = []

    for i in range(4):
        hand = draw_letters()
        print(f"Hand {i + 1}: {hand}")

        word = input("Enter a word using the available letters: ")

        if uses_available_letters(word, hand):
            score = score_word(word)
            print(f"The word '{word}' is valid and has a score of {score}.")
            all_words.append(word)
        else:
            print(f"The word '{word}' is not valid.")
    
    result = get_highest_word_score(all_words)
    if result:
        highest_word, highest_score = result
        print(f"The highest scoring word is '{highest_word}' with a score of {highest_score}.")
if __name__ == "__main__":
    play_game()






