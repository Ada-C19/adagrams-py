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
    letter_list = []

    # While the length of letter_list list is not 10, continue finding an available letter
    while len(letter_list) != 10:
        # convert the keys in the LETTER_POOL dictionary into a list
        # randomly choose a letter form this list
        letter = random.choice(list(LETTER_POOL.keys()))
        # check if the random letter selected is available in the LETTER_POOL dicrionary
        if LETTER_POOL[letter] > 0:
            # if the letter is available, append the selected letter to the letter_list list
            letter_list.append(letter)
            # once the letter is used, decrement the quantity available for this letter in the LETTER_POOL dictionary
            LETTER_POOL[letter] -= 1
    # return letter_list list that contains 10 randomly selected letters
    return letter_list


def uses_available_letters(word, letter_bank):
    # makes a list copy of the letter_bank list so as not to modify the original list
    letter_bank_copy = letter_bank.copy()
    # iterates through each capitalized letter in the word the user passes in
    for letter in word.upper():
        # checks if the current letter if found in the letter_bank_copy list
        if letter in letter_bank_copy:
            # if the current letter is found, remove that instance from the list
            letter_bank_copy.remove(letter)
        else:
            # on the first instance the current letter is not found in the letter_bank_copy list, return False
            return False
    # ends function and returns True if all of the letters in word are found in the letter_bank list
    return True


def score_word(word):
    # SCORE_CHART is a chart that contains the point value for each letter
    SCORE_CHART = {
        "AEIOULNRST": 1,
        "DG": 2,
        "BCMP": 3,
        "FHVWY": 4,
        "K": 5,
        "JX": 8,
        "QZ": 10
    }
    # initializes score variable that will keep track of the accumulating score for each letter found in the user's word
    score = 0
    # grabs the key and value of each dicionary key-pair in the SCORE_CHART dictionary
    for key, value in SCORE_CHART.items():
        # iterate through each letter in capitalized word
        for letter in word.upper():
            # searches for each letter in a key of letters from SCORE_CHART
            if letter in key:
                # if the current letter is found in any of the keys from SCORE_CHART, add that key's value to the score
                score += value
    # checks if the length of the word is between 7 and 10
    if 7 <= len(word) <= 10:
      # if the length of the word is between 7 and 10, an additional 8 bonus points are added to score
        score += 8
    # returns the final score
    return score


def get_highest_word_score(word_list):
    best_word = ""
    highest_score = 0

    for i in range(0, len(word_list)):
        current_word_score = score_word(word_list[i])
        if current_word_score > highest_score:
            best_word = word_list[i]
            highest_score = current_word_score

        elif current_word_score == highest_score:
            if (len(word_list[i]) == 10) and (len(best_word) == 10):
                best_word = best_word
                highest_score = highest_score
            elif (len(word_list[i]) == 10) and (len(best_word) != 10):
                best_word = word_list[i]
                highest_score = current_word_score
            elif (len(word_list[i]) != 10) and (len(best_word) == 10):
                best_word = best_word
                highest_score = highest_score
            elif len(word_list[i]) > len(best_word):
                best_word = best_word
                highest_score = highest_score
            elif len(word_list[i]) < len(best_word):
                best_word = word_list[i]
                highest_score = current_word_score
    return best_word, highest_score
