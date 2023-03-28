import random
import copy
MAX_LETTERS = 10

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

    letter_pool_copy = copy.deepcopy(LETTER_POOL)

    drawn_letters = []

    while len(drawn_letters) < MAX_LETTERS:

        random_letter = random.choice(list(letter_pool_copy.keys()))


        if letter_pool_copy[random_letter] > 0:
            print(letter_pool_copy[random_letter])
            drawn_letters.append(random_letter)
            letter_pool_copy[random_letter] -= 1
        

    return drawn_letters


def uses_available_letters(word, letter_bank):

    # Has two parameters:
    #     word, the first parameter, describes some input word, and is a string
    #     letter_bank, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings, with each string representing a letter
    # Returns either True or False
    # Returns True if every letter in the input word is available (in the right quantities) in the letter_bank
    # Returns False if not; if there is a letter in input that is not present in the letter_bank or has too much of compared to the letter_bank
    
    uppercase_word = word.upper()
    check_letter = {}
    duplicate_letters_word = {}
    duplicate_letters_bank = {}
    
    # my_dict = {i:MyList.count(i) for i in MyList}
    for letter in letter_bank:
        duplicate_letters_bank[letter] = letter_bank.count(letter)

    for letter in uppercase_word:
        
        if letter in letter_bank:
            # creates letter and turns to true if in word
            check_letter[letter] = True
        elif letter not in letter_bank:
            # creates letter and turns to false if not in word
            check_letter[letter] = False
    
    for i in check_letter:
        if check_letter[letter] == True:
            duplicate_letters_word[letter] = uppercase_word.count(letter)
            if duplicate_letters_word[letter] > duplicate_letters_bank[letter]:
                return False
            continue
        if check_letter[letter] == False:
            return False

        
    return True


def score_word(word):
    
#     Now you need a function returns the score of a given word as defined by the Adagrams game.

# Implement the function score_word in game.py. This method should have the following properties:

#     Has one parameter: word, which is a string of characters
#     Returns an integer representing the number of points
#     Each letter within word has a point value. The number of points of each letter is summed up to represent the total score of word
#     Each letter's point value is described in the table below
#     If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    
    score = 0
    uppercase_word = word.upper()

    for letter in uppercase_word:
        score += SCORE_CHART[letter]
    
    if len(word) >= 7:
        score += 8
    
    return score


def get_highest_word_score(word_list):

# After several hands have been drawn, words have been submitted, checked, scored, and played, you need a way to find the highest scoring word. This function looks at the list of word_list and calculates which of these words has the highest score, applies any tie-breaking logic, and returns the winning word in a special data structure.

# Implement a function called get_highest_word_score in game.py. This method should have the following properties:

#     Has one parameter: word_list, which is a list of strings
#     Returns a tuple that represents the data of a winning word and it's score. The tuple must contain the following elements:
#         index 0 ([0]): a string of a word
#         index 1 ([1]): the score of that word
#     In the case of tie in scores, use these tie-breaking rules:
#         prefer the word with the fewest letters...
#         ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
#         If the there are multiple words that are the same score and the same length, pick the first one in the supplied list

    best_score = ('', 0)
    
    for word in word_list:
        calculated_score = score_word(word)
        
        if (best_score[1] < calculated_score or
            (best_score[1] == calculated_score and len(best_score[0]) > len(word))
        ):
            best_score = word, calculated_score

        if len(word) == 10:
            best_score = word, calculated_score
            break

    return best_score


