import random

WORD_LENGTH_BONUS_THRESHOLD = 7
WORD_LENGTH_BONUS_POINTS = 8
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
POINT_VALUES = {
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


def generate_letter_pool():
    """Return a list of all the available letters."""
    letter_pool_list = []
    for letter, quantity in LETTER_POOL.items():
        letter_pool_list.extend([letter] * quantity)
    return letter_pool_list


def draw_letters():
    """Return a list of 10 randomly chosen letters from the letter pool."""
    letter_pool_list = generate_letter_pool()
    letter_bank = []
    for letter in range(0, 10):
        random_index = random.randint(0, len(letter_pool_list) - 1)
        letter_bank.append(letter_pool_list[random_index])
        letter_pool_list.pop(random_index)
    return letter_bank


def count_available_letters(letter_bank):
    """Return a dictionary containing the quantity of each letter in letter_bank."""
    letter_counts = {letter: 0 for letter in letter_bank}
    for letter in letter_bank:
        letter_counts[letter] += 1
    return letter_counts


def uses_available_letters(word, letter_bank):
    """Return True if a word uses only the letters from letter_bank."""
    letter_counts = count_available_letters(letter_bank)
    word = word.upper()
    for letter in word:
        if letter not in letter_bank or letter_counts[letter] <= 0:
            return False
        letter_counts[letter] -= 1
    return True


def score_word(word):
    """Return the amount of points (integer) for a word."""
    score = 0
    if len(word) >= WORD_LENGTH_BONUS_THRESHOLD:
        score += WORD_LENGTH_BONUS_POINTS
    for letter in word:
        score += POINT_VALUES[letter.upper()]
    return score


def make_scores_and_words_dictionary(word_list):
    """Score all words and return dictionary of scores and words corresponding to that score."""
    scores_and_words = {}
    for word in word_list:
        score = score_word(word)
        if score not in scores_and_words:
            scores_and_words[score] = [word]
            continue
        scores_and_words[score].append(word)
    return scores_and_words


def find_top_score_and_best_words(word_list):
    """Find the top scoring words and return them along with corresponding score."""
    scores_and_words = make_scores_and_words_dictionary(word_list)
    highest_score = max(scores_and_words.keys())
    return scores_and_words[highest_score], highest_score


def get_highest_word_score(word_list):
    """Find the best word out of the words with the top score. Return as tuple with its score."""
    words_to_compare, highest_score = find_top_score_and_best_words(word_list)

    current_winner = words_to_compare[0]
    for word in words_to_compare:                  # If there is only 1 winner, we skip the for loop to return the winner                               
        if len(word) == 10:                        # The first word to have 10 letters wins
            return word, highest_score
        elif len(word) < len(current_winner):      # If no word has ten letters, the word with the fewest letters wins
            current_winner = word
    return current_winner, highest_score
