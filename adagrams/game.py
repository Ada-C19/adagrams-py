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

    # build a list of letters from the letter pool
    letter_list = []
    for letter, freq in LETTER_POOL.items():
        letter_list.extend([letter] * freq)

    # drawing letters
    return random.sample(letter_list, 10)

# a helper function to be used in the function uses_available_letters()
def create_dict(some_list):

    new_dict = {}

    for item in some_list:
        if item.lower() not in new_dict:
            new_dict[item.lower()] = 1
        else:
            new_dict[item.lower()] += 1

    return new_dict


def uses_available_letters(word, letter_bank):

    # turning the letter pool and the passed in word to lists, with values as the occurence of letters
    letter_pool_dict = create_dict(letter_bank)
    word_dict = create_dict(word)

    # check if the word used lettes in the letter bank,
    # if yes compare the occurence of those letters in the word with the occurence in the letter bank
    for letter in word:
        if letter.lower() not in letter_pool_dict or letter_pool_dict[letter.lower()] < word_dict[letter.lower()]:
            return False

    return True


def score_word(word):

    value_dict = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
                ('D', 'G'): 2,
                ('B', 'C', 'M', 'P'): 3,
                ('F', 'H', 'V', 'W', 'Y'): 4,
                ('K'): 5,
                ('J', 'X'): 8,
                ('Q', 'Z'): 10
                }

    # access the value of the letters and add up to find the total score of the word
    word_value = 0

    for letter in word:
        letter_value = next(
            value for tp, value in value_dict.items() if letter.upper() in tp)
        word_value += letter_value

    if len(word) in range(7, 11):
        word_value += 8

    return word_value


def get_highest_word_score(word_list):

    score_dict = {word: score_word(word) for word in word_list}

    highest_score = 0
    highest_score_words = []

    best_word = tuple()

    # collect all the possible highest score words
    for word, score in score_dict.items():
        if score > highest_score:
            highest_score = score
            highest_score_words = [word]
        elif score == highest_score:
            highest_score_words.append(word)

    # check the ten-letter length condition, else choose the shortest and first one in the highest score list
    ten_letter_word = [word for word in highest_score_words if len(word) == 10]

    if ten_letter_word:
        best_word = (ten_letter_word[0], score_word(ten_letter_word[0]))
    else:
        shortest_word = min((word for word in highest_score_words), key=len)
        best_word = (shortest_word, score_word(shortest_word))

    return best_word
