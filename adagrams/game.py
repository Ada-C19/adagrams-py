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

SCORE_CHART = {
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

def draw_letters():
    """
    Returns the player's "hand", an array of ten strings, each containing only one letter.
    Letters are randomly drawn from LETTER_POOL without replacement. 
    Calling this function does not mutate LETTER_POOL.
    """
    letters = list(LETTER_POOL.keys())
    weights = list(LETTER_POOL.values())

    hand = []
    # Draw 10 letters without replacement
    for _ in range(10):
        # Select a random letter with consideration for the odds of drawing it
        letter = random.choices(letters, weights=weights, k=1)[0]
        idx = letters.index(letter)
        # Letter with weight 0 should have no chance of being drawn
        assert weights[idx] > 0
        hand.append(letter)
        weights[idx] -= 1

    return hand


def uses_available_letters(word, letter_bank):
    """
    Returns a boolean.
    Checks if an input word is valid based on available letters in hand (i.e., letter_bank).
    Does not mutate the hand.
    Allows for lowercase letters.
    """

    copy_bank = [a.upper() for a in letter_bank]
    word = word.upper()

    for char in word:
        if char not in copy_bank:
            return False
        copy_bank.remove(char)

    return True


def score_word(word):
    """
    Returns an integer representing the number of points.
    A word with length greater than 6 gets an additional 8 points.
    """
    word = word.upper()

    score = sum([SCORE_CHART[char] for char in word])
    
    # Give bonus for words longer than 6 letters
    if len(word) > 6:
        score += 8

    return score

def get_highest_word_score(word_list):
    """
    Returns a tuple of the winning word and its score.
    In case of a tie, prioritize the word with 10 letters, 
    then the word with the fewest letters, then the first element in the list
    """
    
    word_scores = []
    max_score = 0
    
    for idx, word in enumerate(word_list):
        score = score_word(word)
        if score > max_score:
            max_score = score
        word_scores.append((word, score, idx))

    # Sort word_scores in descending order of scores
    word_scores.sort(reverse=True, key=lambda x: x[1])
  
    # Create list of words and their indices with tied scores
    ties = [(word, idx) for word, score, idx in word_scores if score == max_score]

    # Handle the case of a clear winner
    if len(ties) == 1:
        winner = ties[0][0]
        return winner, max_score

    # Sort list of ties in ascending order of word length
    ties.sort(key=lambda x:len(x[0]))

    # Prioritize words with length 10 as winners
    if len(ties[-1][0]) == 10:
        # Mutate ties to only contain words with length 10
        ties = [(word, idx) for word, idx in ties if len(word) == 10]
        # Select the word with lowest index if there's more than one option for winner
        if len(ties) != 1:
            ties.sort(key=lambda x:x[1])
        winner = ties[0][0]
    
    # Secondary win condition: words with fewest letters
    else:
        min_length = len(ties[0][0])
        # Mutate ties to only contain words with fewest letters
        ties = [(word, idx) for word, idx in ties if len(word) == min_length]
        # Select the word with lowest index if there's more than one option for winner
        if len(ties) != 1:
            ties.sort(key=lambda x:x[1])
        winner = ties[0][0]

    return winner, max_score

        
    


        




        

    
