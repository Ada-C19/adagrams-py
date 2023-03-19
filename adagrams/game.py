import random
def draw_letters():
    LETTER_POOL = {
        'A' : 9,	
        'B' : 2,	
        'C' : 2,	
        'D' : 4,	
        'E' : 12,	
        'F' : 2,	
        'G' : 3,	
        'H' : 2,	
        'I' : 9,	
        'J' : 1,	
        'K' : 1,	
        'L' : 4,	
        'M' : 2,
        'N' : 6,
        'O' : 8,
        'P' : 2,
        'Q' : 1,
        'R' : 6,
        'S' : 4,
        'T' : 6,
        'U' : 4,
        'V' : 2,
        'W' : 2,
        'X' : 1,
        'Y' : 2,
        'Z' : 1
    }
    hand = []
    for key in LETTER_POOL:
        #For each key, the loop runs a nested for loop that adds the letter key to the hand list the number of times specified by the value.
        for i in range(LETTER_POOL[key]):
            hand.append(key)
    #Once all the letters are added to the hand list, the list is shuffled
    random.shuffle(hand)
    #first 10 elements in the list are returned
    return hand[:10]

def uses_available_letters(word, letter_bank):
    letters = letter_bank[:]
    for letter in word:
        if letter not in letters:
            return False
        else:
            letters.remove(letter)
    return True

def score_word(word):
    score = 0
    for letter in word:
        if letter in "AEIOULNRST":
            score += 1
        elif letter in "DG":
            score += 2
        elif letter in "BCMP":
            score += 3
        elif letter in "FHVWY":
            score += 4
        elif letter == "K":
            score += 5
        elif letter in "JX":
            score += 8
        elif letter in "QZ":
            score += 10
        if len(word) >= 7 and len(word) <= 10:
            score += 8

    return score

def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = ''
    for word in word_list:
        score = score_word(word)
    if score > highest_score:
        highest_score = score
        winning_word = word
    if score == highest_score:
        if len(word) == 10:
            highest_score = score
            winning_word = word

    return ([winning_word, highest_score])