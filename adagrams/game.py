import random
from collections import Counter
# letter_pool is a dict saving letters and their frequencies 
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
SCORES = {
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

# def draw_letters():
#     # Create an empty list to hold the drawn letters
#     hand = []
    
#     # Create a dictionary to keep track of the count of each letter drawn
#     letter_counts = {letter: 0 for letter in LETTER_POOL}
    
#     # Draw 10 letters, one at a time
#     for i in range(10):
#         # Randomly select a letter from the list of keys in the LETTER_POOL dictionary
#         letter = random.choice(list(LETTER_POOL.keys()))
        
#         # If the letter count is less than its value in LETTER_POOL, add it to the hand
#         if letter_counts[letter] < LETTER_POOL[letter]:
#             hand.append(letter)
#             letter_counts[letter] += 1
#         # Otherwise, try again
#         else:
#             i -= 1
    
#     # Return the list of drawn letters
#     return hand

def draw_letters():
    # Create an empty list to hold the drawn letters
    hand = []
    
    # Create a list of all letters in the LETTER_POOL dictionary
    all_letters = []
    for letter, freq in LETTER_POOL.items():
        all_letters.extend([letter] * freq)
    
    # Shuffle the list of letters and draw 10 at random
    random.shuffle(all_letters)
    hand = all_letters[:10]
    
    # Return the list of drawn letters
    return hand


def uses_available_letters(word, letter_bank):
    # Convert letter_bank to string
    letter_bank_str = ''.join(letter_bank)

    # Create a counter for the letters in the word, which counts the number of occurrences of each letter
    word_counts = Counter(word.upper())

    # Create a counter for the letters in the letter bank, which counts the number of occurrences of each letter
    bank_counts = Counter(letter_bank_str.upper())

    # Loop over the letters and their counts in the word counter
    for letter, count in word_counts.items():
        # Check if the count of the letter in the word is greater than the count of the letter in the letter bank
        if count > bank_counts[letter]:
            # If so, the word cannot be made from the letter bank, so return False
            return False
    
    # If all letters in the word can be made from the letter bank, return True
    return True

def score_word(word):
    """
    Returns the score for a given word. The word should be a string of letters (can be lowercase or uppercase).
    """
    
    # Calculate the score for the word
    score = 0
    for letter in word.upper():
        try:
            score += SCORES[letter]
        except KeyError:
            score += 0
    
    # Add 8 points for words of length 7 or more
    if len(word) >= 7:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    if not word_list:
        # Handle the case where word_list is empty
        raise ValueError("The word list is empty")
    
    # Calculate the score of each word in the list
    word_scores = [(word, score_word(word)) for word in word_list]

    # Find the maximum score among the list of words
    max_score = max(word_scores, key=lambda x: x[1])[1]

    # Filter the list of words to only include words with the maximum score
    max_score_words = [word for word, score in word_scores if score == max_score]

    # Check if there is a tie and apply the tie-breaking rules
    if len(max_score_words) > 1:
        # Check for a word with 10 letters and choose it over shorter words
        ten_letter_words = [word for word in max_score_words if len(word) == 10]
        if ten_letter_words:
            return ten_letter_words[0], max_score

        # If no word has 10 letters, prefer the word with the fewest letters
        shortest_word = min(max_score_words, key=len)
        return shortest_word, max_score

    # If there is only one word with the maximum score, return it
    return max_score_words[0], max_score
