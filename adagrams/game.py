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
    import random
    list_of_letters = list(LETTER_POOL.keys()) 
    weight_letters = list(LETTER_POOL.values())
    ten_letters = []
    letter_freq = {}

    # could create a helperfunction if the letters are more then 10
    while len(ten_letters) < 10:
        list_letter_drawn = random.choices(list_of_letters, weights = weight_letters, k=1)
        letter_drawn = list_letter_drawn[0]
        if letter_drawn in letter_freq:
            if letter_freq[letter_drawn] < LETTER_POOL[letter_drawn]:
                letter_freq[letter_drawn] +=1
            else:
                continue
        else:
            letter_freq[letter_drawn] = 1

        ten_letters.append(letter_drawn)


    return ten_letters        


def uses_available_letters(word, letter_bank):
#  """Has two parameters:
#    - `word`, the first parameter, describes some input word, and is a string
#    - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter
#     - Returns either `True` or `False`
#     - Returns `True` if every letter in the `input` word is available (in the right quantities) in the `letter_bank`
#     - Returns `False` if not; if there is a letter in `input` that is not present in the `letter_bank` or has too much of compared to the `letter_bank`
# """ 
    letter_bank_count = {}

    for letters in letter_bank:
        if letters in letter_bank_count:
            letter_bank_count[letters] +=1
        else:
            letter_bank_count[letters] = 1

    word_capital = word.upper()
    for letter in word_capital:
        if letter in letter_bank and letter_bank_count[letter]>=1:
            letter_bank_count[letter] -=1  
        else:
            return False
    return True

def score_word(word):
# - Has one parameter: `word`, which is a string of characters
# - Returns an integer representing the number of points
# - Each letter within `word` has a point value. The number of points of each letter is summed up to represent the total score of `word`
# - Each letter's point value is described in the table below
# - If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
# |Letter                        | Value|
# |:----------------------------:|:----:|
# |A, E, I, O, U, L, N, R, S, T  |   1  |
# |D, G                          |   2  |
# |B, C, M, P                    |   3  |
# |F, H, V, W, Y                 |   4  |
# |K                             |   5  |
# |J, X                          |   8  |
# |Q, Z                          |   10 |
 
    point_system ={
    "A": 1, 
    "E": 1,
    "I": 1, 
    "O": 1, 
    "U": 1,
    "L": 1,
    "N": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "D": 2, 
    "G": 2,
    "B": 3, 
    "C": 3, 
    "M": 3, 
    "P": 3,
    "F": 4, 
    "H": 4, 
    "V": 4, 
    "W": 4, 
    "Y": 4,
    "K": 5,
    "J": 8, 
    "X": 8,
    "Q": 10,
    "Z": 10
    }
# FUNCTION BODY
    word_capital = word.upper()
    points = 0
    for letter in word_capital:
        points += point_system.get(letter)
    if len(word_capital) in [7,8,9,10]:
        points += 8
    return points


def get_highest_word_score(word_list):
# - Has one parameter: `word_list`, which is a list of strings
# - Returns a tuple that represents the data of a winning word and it's score.  The tuple must contain the following elements:
#   - index 0 ([0]): a string of a word
#   - index 1 ([1]): the score of that word
# - In the case of tie in scores, use these tie-breaking rules:
#     - prefer the word with the fewest letters...
#     - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
#     - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list

# FUNCTION BODY
    all_scores = {}
    top_word = ""
    top_score = 0
    count_ten_words = 0
    for word in word_list:
        score = score_word(word)
        if score > top_score:
            if len(word) == 10:
                count_ten_words +=1
            top_score = score
            top_word = word
        elif score == top_score:
            if len(word) ==10 and count_ten_words <= 0:
                top_word = word
                count_ten_words +=1
            elif len(word) < len(top_word) and len(top_word) != 10:
                top_word = word
                
    best_word = (top_word, top_score)
    return best_word