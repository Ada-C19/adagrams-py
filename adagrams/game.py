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
    """
    Returns the player's "hand", an array of ten strings, each containing only one letter
    Letters are randomly drawn from a pool of letters without replacement. 
    Calling this function does not mutate LETTER_POOL
    """
    copy_pool = dict(LETTER_POOL)
    letters = list(copy_pool.keys())
    weights = list(copy_pool.values())

    hand = []

    # Loop until hand is full
    while int(len(hand)) < 10:
        # Select a random letter with consideration for weight, returns a list
        draw = random.choices(letters, weights=weights, k=1)
        l = draw[0]
        idx = letters.index(l)
        # Redraw if letter is not available
        if weights[idx] == 0:
            continue
        else:
            hand.append(l)
            weights[idx] -= 1

    return hand


def uses_available_letters(word, letter_bank):
    """
    Returns a boolean.
    Checks if an input word is valid based on available letters in hand (i.e., letter_bank).
    Does not mutate the hand.
    Allows for lowercase letters.
    """
    # Ensure original hand remains unmutated
    copy_bank = list(letter_bank)
    # Ensure lower case letters are valid
    word = word.upper()
    
    # Loop through each character in word
    for char in word:
        # Remove letter from hand if present
        if char in copy_bank:
            copy_bank.remove(char)
        # Return False if letter is not present in hand
        else:
            return False
    # If the for loop finishes without returning False, 
    # every character in word was present in hand
    return True

SCORE_CHART = LETTER_POOL = {
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
def score_word(word):
    """
    Returns an integer representing the number of points.
    A word with length greater than 6 gets an additional 8 points.
    """
    # Ensure lower case words are valid
    word = word.upper()
    score = 0
    
    # Loop through characters in word
    for char in word:
        # Add character score to score
        score += SCORE_CHART[char]
    
    # Give bonus for words longer than 6 letters
    if int(len(word)) > 6:
        score += 8

    return score

def get_highest_word_score(word_list):
    """
    Returns a tuple of the winning word and its score.
    In case of a tie, prioritize the word with 10 letters, 
    then the word with the fewest letters, then the first element in the list
    """
    word_scores = []

    for word in word_list:
        score = score_word(word)
        word_scores.append((word, score))


    # Sort list of word_scores in descending order of scores
    word_scores.sort(reverse=True, key=lambda x:x[1])

    max_score = word_scores[0][1]
    # List of tied scores
    ties = [word_scores[0]]

    for w_s in word_scores[1:]:
        if w_s[1] == max_score:
            ties.append(w_s)
    
    # If no ties, return word with max_score
    if len(ties) == 1:
        return ties[0]
    
    # Sort list of ties in ascending order of word length
    ties.sort(key=lambda x: len(x[0]))

    # If one of the ties has word length 10, that is winner
    if len(ties[-1][0]) == 10:
        return ties[-1]
    

    min_length = len(ties[0][0])
    # Eliminate ties if they do not have fewest letters
    for w_s in ties:
        word = w_s[0]
        if len(word) != min_length:
            ties.remove(w_s)
    
    # If no more ties, return word with fewest letters
    if len(ties) == 1:
        return ties[0]
    
    # Initialize baseline word_list index for later comparison
    min_idx = word_list.index(ties[0][0])
    first_w_s = ties[0]

    # Loop through each word_score tuple in ties
    for w_s in ties[1:]:
        word = w_s[0]
        # Replace min_idx and first_w_s if index is smaller than previous min_idx
        if word_list.index(word) < min_idx:
            min_idx = word_list.index(word)
            first_w_s = w_s
    
    return first_w_s

    
        
    


        




        

    
