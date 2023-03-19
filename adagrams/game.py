import random
from collections import Counter
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
    hand = random.sample(list(LETTER_POOL.keys()), 10)
    return hand

# def uses_available_letters(word, letter_bank):
#     # Convert word to uppercase
#     word = word.upper()
#     # Create a counter of the letter_bank
#     bank_counts = Counter(letter_bank)
#     # Iterate over each letter in the word
#     for letter in word:
#         # If the letter is not in the bank_counts, or if the count is 0, return False
#         if letter not in letter_bank or bank_counts[letter] == 0:
#             return False
#         # Otherwise, decrement the count of the letter in bank_counts
#         bank_counts[letter] -= 1
#     # If we make it through the loop without returning False, return True
#     return True
def uses_available_letters(word, letter_bank):
    word = word.upper()
    word_counts = Counter(word)
    for letter, count in word_counts.items():
        if count > letter_bank.count(letter):
            return False
    return True

def score_word(word):
    # word = word.upper()
    # score = 0
    # for letter in word:
    #     if letter in "AEIOULNRST":
    #         score += 1
    #     elif letter in "DG":
    #         score += 2
    #     elif letter in "BCMP":
    #         score += 3
    #     elif letter in "FHVWY":
    #         score += 4
    #     elif letter == "K":
    #         score += 5
    #     elif letter in "JX":
    #         score += 8
    #     elif letter in "QZ":
    #         score += 10
    # if len(word) >= 7:
    #     score += 8
    # return score
    scores = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
        'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
        'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10}
    score = sum(scores.get(letter, 0) for letter in word.upper())
    if len(word) >= 7:
        score += 8
    return score



# def get_highest_word_score(word_list):
#     word_dict = {}
#     for word in word_list:
#         word_dict[word] = score_word(word)
#     max_val = max(word_dict.values())
#     max_word = max(word_dict, key=word_dict.get)
#     for word, score in word_dict.items():
#         if score == max_val:
#             if len(max_word) == 10:
#                 return max_word, max_val
#             elif len(word) == 10 or len(word) < len(max_word):
#                 max_word = word
#     return max_word, max_val
def get_highest_word_score(word_list):
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
