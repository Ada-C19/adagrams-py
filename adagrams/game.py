import random
import copy

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

LETTER_VALUE = {
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
    alphabet = list(LETTER_POOL.keys())
    drawn_letters = []

    while True:
        # Ensure return list does not have more than 10 elems
        if len(drawn_letters) == 10:
            break

        random_letter = alphabet[random.randint(0, len(alphabet)-1)]
        quantity = LETTER_POOL[random_letter]
        counter = 0
        
        # Letter should not be in return list more than its quantity in the pool
        for i in range(len(drawn_letters)):
            if drawn_letters[i] == random_letter:
                counter += 1
        if counter < quantity:
            drawn_letters.append(random_letter)

    return drawn_letters


def uses_available_letters(word, letter_bank):
    available_letters = copy.deepcopy(letter_bank)
    word = word.upper()

    for letter in word:
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True


def score_word(word):
    word = word.upper()
    score = 0

    for letter in word:
        score += LETTER_VALUE[letter]
    
    if len(word) > 6 and len(word) < 11:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    words_scores = {}
    score_counter = 0
    potential_winners = []
    winning_word = "blank"
    word_length = 11
    shortest_words = []

    # Calculate the scores of each word in the list, highest score becomes "score_counter"
    for word in word_list:
        words_scores[word] = score_word(word)
        if words_scores[word] > score_counter:
            score_counter = words_scores[word]

    # Add any words with the highest score to potential winners list
    for word in words_scores:
        if words_scores[word] == score_counter:
            potential_winners.append(word)

    # If there is only one word in potential winners list then its the best word!
    if len(potential_winners) == 1:
        winning_word = potential_winners[0]
    
    else:
        # identify lowest word length in a for loop
        for word in potential_winners:
            if len(word) < word_length:
                word_length = len(word)

        # make a list of words with lowest length in a for loop
        for word in potential_winners:
            if len(word) == word_length:
                shortest_words.append(word)

        # winner is first in this list of lowest word length
        winning_word = shortest_words[0]
        
    return (winning_word, score_counter)