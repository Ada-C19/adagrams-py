import random

LETTER_SELECTION = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
    'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
    'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1,
} 
    
def draw_letters():
    letter_pool = dict(LETTER_SELECTION)
    # list to store drawn letters
    hand = []
    # use while loop to draw 10
    while len(hand) < 10:
        letter = random.choices(list(letter_pool.keys()), list(letter_pool.values()))[0]
        hand.append(letter)
        letter_pool[letter] -= 1
        if letter_pool[letter] == 0:
            del letter_pool[letter]
    
    # return drawn letter list
    return hand

def uses_available_letters(word, letter_bank):
    word = word.lower()
    letter_bank = [letter.lower() for letter in letter_bank]
    # Check if every letter in input word is available in letter_bank
    for letter in word:
        if letter not in letter_bank:
            return False
        else:
            letter_bank.remove(letter)
    return True


def score_word(word):
    points = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    score = sum(points.get(letter.upper(), 0) for letter in word)
    if len(word) in (7, 8, 9, 10):
        score += 8
    return score


from collections import defaultdict

def get_highest_word_score(words):
    # create empty dict using defaultdict
    # assign to scores (will hold the score of each word as the key)
    scores = defaultdict(list)
    # iterate through each word in input words list
    for word in words:
    # calculate score of word using score_word func. & store it in var score
        score = score_word(word)
        scores[score].append(word)
    # find  highest score from scores dict using max func. store it in var max_score
    max_score = max(scores.keys())
    max_score_words = scores[max_score]
    
    # if only one word with highest score, return w/ score as tuple
    if len(max_score_words) == 1:
        return max_score_words[0], max_score
    # check hgihest score word length for 10, return w/ score as tuple
    ten_letter_words = [w for w in max_score_words if len(w) == 10]
    if ten_letter_words:
        return ten_letter_words[0], max_score
    # Sort list of words w/ highest score by len, use sorted func, store in var shortest_words
    shortest_words = sorted(max_score_words, key=len)
    return shortest_words[0], max_score