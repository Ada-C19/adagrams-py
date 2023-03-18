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
    letter = random.choice(list(LETTER_POOL))

    while hand.count(letter) < LETTER_POOL[letter] and len(hand) < 10:
            hand.append(letter)
            letter = random.choice(list(LETTER_POOL))

    return hand

def uses_available_letters(word, letter_bank):
    
    letter_freq_in_word = {}
    letter_freq_in_bank = {}

    word = word.upper()

    for i in range(len(word)):
        if word[i] not in letter_freq_in_word:
            letter_freq_in_word[word[i]] = 0
        letter_freq_in_word[word[i]] += 1

        occurrence = letter_bank.count(word[i])
        if word[i] not in letter_freq_in_bank:
            letter_freq_in_bank[word[i]] = occurrence

    for letter in word:
        if letter_freq_in_word[letter] > letter_freq_in_bank[letter]:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass