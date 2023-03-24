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
    hand = []
    copy_letter_pool = LETTER_POOL.copy()

    while len(hand) < 10:
      random_letter = random.choices(list(copy_letter_pool), weights = copy_letter_pool.values(), k=1)
      str_random_letter = random_letter[0]
      
      if copy_letter_pool[str_random_letter] > 0:
        hand.append(str_random_letter)
        copy_letter_pool[str_random_letter] += -1
    return hand

def uses_available_letters(word, letter_bank):
    quantity_available = {}
    validate_enough_available = {}

    for letter in letter_bank:
        available_count = letter_bank.count(letter)
        quantity_available[letter] = available_count

    for character in word.upper():
        amount_needed_for_word = (word.upper()).count(character)
        if character in quantity_available and (amount_needed_for_word <= quantity_available[character]):
            validate_enough_available[character] = True
        else:
            validate_enough_available[character] = False
  
    if False in validate_enough_available.values():
        return False
    else:
        return True
    
def score_word(word):
    score = 0
    score_chart = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2, 
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5, 
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }

    for letter in word.upper():
        if letter in score_chart:
            score += score_chart[letter]
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    player_scores = {}
    top_players = []
  
    for word in word_list:
      word_score = score_word(word)
      player_scores[word] = word_score

    for key, value in player_scores.items():
      highest_score = max(player_scores.values())
      if value >= highest_score:
        top_players.append((key, value))

    winner = top_players[0]

    for word, score in top_players:
        if len(word) == len(winner[0]):
          winner = winner
        elif len(word) >= 10:
          winner = (word, score)
        elif len(word) < len(winner[0]) and len(winner[0]) != 10:
          winner = (word, score)
    return winner
    
      
