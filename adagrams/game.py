import random

LETTER_TILES = {
    'A': {'frequency': 9, 'value': 1},
    'B': {'frequency': 2, 'value': 3},
    'C': {'frequency': 2, 'value': 3}, 
    'D': {'frequency': 4, 'value': 2}, 
    'E': {'frequency': 12, 'value': 1}, 
    'F': {'frequency': 2, 'value': 4}, 
    'G': {'frequency': 3, 'value': 2}, 
    'H': {'frequency': 2, 'value': 4}, 
    'I': {'frequency': 9, 'value': 1}, 
    'J': {'frequency': 1, 'value': 8}, 
    'K': {'frequency': 1, 'value': 5}, 
    'L': {'frequency': 4, 'value': 1}, 
    'M': {'frequency': 2, 'value': 3}, 
    'N': {'frequency': 6, 'value': 1}, 
    'O': {'frequency': 8, 'value': 1}, 
    'P': {'frequency': 2, 'value': 3}, 
    'Q': {'frequency': 1, 'value': 10}, 
    'R': {'frequency': 6, 'value': 1}, 
    'S': {'frequency': 4, 'value': 1}, 
    'T': {'frequency': 6, 'value': 1}, 
    'U': {'frequency': 4, 'value': 1}, 
    'V': {'frequency': 2, 'value': 4}, 
    'W': {'frequency': 2, 'value': 4}, 
    'X': {'frequency': 1, 'value': 8}, 
    'Y': {'frequency': 2, 'value': 4}, 
    'Z': {'frequency': 1, 'value': 10}
}

TOTAL_TILES_PER_HAND = 10

def draw_letters():
    letter_bank = []

    for letter in LETTER_TILES:
        for i in range(LETTER_TILES[letter]['frequency']):
            letter_bank.append(letter)

    player_hand = []

    while len(player_hand) < TOTAL_TILES_PER_HAND:
        current_letter = random.choice(letter_bank)
        letter_occurences = 0
        
        if current_letter in player_hand:
            for current_letter in player_hand:
                letter_occurences += 1
        
        if letter_occurences >= LETTER_TILES[current_letter]['frequency']:
                continue

        player_hand.append(current_letter)

    return player_hand

def uses_available_letters(word, letter_bank):
    letter_bank_copy = []
    word = word.upper()
    for letter in letter_bank:
        letter_bank_copy.append(letter)

    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    score = 0
    word = word.upper()
    for letter in word:
        score += LETTER_TILES[letter]['value']
    if 7 <= len(word) <= TOTAL_TILES_PER_HAND:
        score += 8
    return score


def get_highest_word_score(word_list):
    all_scores = {}
    best_word = None
    best_score = 0

    for word in word_list:
        word_score = score_word(word)
        all_scores[word] = word_score

    for word, score in all_scores.items():
        if len(word) == TOTAL_TILES_PER_HAND:
            best_word = word
            best_score = score
            break
        if score > best_score:
            best_word = word
            best_score = score
        if score == best_score:
            if len(word) < len(best_word):
                best_word = word

    return best_word, best_score