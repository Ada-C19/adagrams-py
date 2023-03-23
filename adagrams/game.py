from random import choice


def draw_letters():

    MAX_LETTERS_IN_HAND = 10

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

    # Creating a letter pool list to emulate a pile of letters to choose from:
    for letter in LETTER_POOL:
         temp = [letter] * LETTER_POOL[letter]
         letter_pool_list.extend(temp)

    #build the player's hand (letters)
    letters = []
    while len(letters) < MAX_LETTERS_IN_HAND:
        # choose a random letter from a list of LETTER_POOL keys using random.choice
        rand_letter = choice(letter_pool_list)
        if letters.count(rand_letter) >= LETTER_POOL[rand_letter]:
            continue
        else:
            letters.append(rand_letter)

    return letters


def uses_available_letters(word, letter_bank):
    word = word.upper()  # forces the input to be case insensitive

    # to ensure each letter is in letter_bank and does not occur too frequently:
    for letter in word:
        if letter not in letter_bank or word.count(letter) > letter_bank.count(letter):
            return False
    return True


def score_word(word):
    # minimum required length of word to qualify for a long word bonus:
    BONUS_POINT_MIN_LENGTH = 7
    # bonus points to be awarded for words that meet the bonus minimum length:
    BONUS_POINTS = 8

    letter_values = {
        'AEIOULNRST': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10
    }

    score = 0
    if word:
        word = word.upper()
        if len(word) >= BONUS_POINT_MIN_LENGTH:
            score += BONUS_POINTS
        for letter in word:
            for tier in letter_values:
                if letter in tier:
                    score += letter_values[tier]
        return score
    return score


def get_highest_word_score(word_list):
    MAX_LETTER_LENGTH = 10
    word_scores = {}
    high_score = 0

    # put the words from word_list into word_scores dict with their scores
    for word in word_list:
        score = score_word(word)
        word_scores[word] = score
        if score > high_score:
            high_score = score  # keep track of the high score to find which words match it

    # compile the words with the same high score into a list
    high_score_words = [word for word in word_scores if word_scores[word] == high_score]

    if len(high_score_words) > 1:

        biggest_word = max(high_score_words, key=lambda word: len(word))
        smallest_word = min(high_score_words, key=lambda word: len(word)) # will return the first smallest word
        # in the event of multiple small words w/ same length

        if len(biggest_word) == MAX_LETTER_LENGTH:
            return biggest_word, high_score
        elif len(biggest_word) < MAX_LETTER_LENGTH:
            return smallest_word, high_score
    
    else:
        winning_word = "".join(high_score_words)
        return winning_word, high_score
