import random

def generate_letter_pool():
    """Return a list of all the available letter tiles."""
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
    letter_pool_list = []
    for letter, quantity in LETTER_POOL.items():
        letter_pool_list.extend([letter] * quantity)
    return letter_pool_list


def casefold_letters(word):
    """Return a list letters from a word in all lowercase."""
    casefolded_letters = []
    for letter in word:
        casefolded_letters.append(letter.casefold())
    
    return casefolded_letters


def count_available_letters(letter_bank):
    """Return a dictionary containing the quantity of each letter in letter_bank."""
    letter_counts = {}
    # for letter in letter_bank:
    #     letter_counts[letter] = 0
    # for letter in letter_bank:
    #     letter_counts[letter] += 1

    for letter in letter_bank:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    
    return letter_counts


def sort_scores(word_list):
    """Return a tuple sorted by the scores."""
    scores = {}
    for word in word_list:
        scores[word] = score_word(word)
    sorted_scores = sorted(scores.items())

    return sorted_scores


def draw_letters():
    """Return a list of 10 randomly chosen letters."""
    letter_pool_list = generate_letter_pool()
    letter_bank = []

    for tile in range(0, 10):
        random_tile = random.choice(letter_pool_list)
        letter_pool_list.remove(random_tile)
        letter_bank.append(random_tile)
    
    return letter_bank


def uses_available_letters(word, letter_bank):
    """Return true if a word uses only the letters from letter_bank."""
    letter_bank = casefold_letters(letter_bank)
    word = casefold_letters(word)
    letter_counts = count_available_letters(letter_bank)

    for letter in word:
        if letter in letter_bank and letter_counts[letter] > 0:
            letter_counts[letter] -= 1
        else:
            return False
    
    return True


def score_word(word):
    """Return the amount of points (integer) for a word."""
    point_values = {
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

    score = 0
    if len(word) in range(7,11):
        score += 8
    for letter in word:
        score += point_values[letter.upper()]
    
    return score
    
    
def get_highest_word_score(word_list):
    """Return a tuple containing the winning word and corresponding score."""
    winner = ("", 0)
    sorted_scores = sort_scores(word_list)
    
    for score in range(len(sorted_scores)):
        comparator_word = sorted_scores[score][0]
        comparator_points = sorted_scores[score][1]
        if comparator_points > winner[1]:
            winner = sorted_scores[score]
        elif comparator_points == winner[1]:
            if len(winner[0]) == 10:
                continue
            elif len(comparator_word) == 10:
                winner = sorted_scores[score]
            elif len(winner[0]) < len(comparator_word):
                continue
            elif len(comparator_word) < len(winner[0]):
                winner = sorted_scores[score]

    return winner