
import random
import string

def draw_letters():
    letter_pool = {
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
    hand = []
    random_letter = ""
    while len(hand) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        if letter_pool[random_letter] > 0:
            letter_pool[random_letter] = letter_pool[random_letter] - 1
            hand.append(random_letter)
        
    return hand
draw_letters()


def uses_available_letters(word, letter_bank):
    bank = []
    word = word.upper()
    for letter in letter_bank:
        bank.append(letter)
    for letter in word:
        if letter in bank:
            bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    chart = {'A': 1, 
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
    score = 0
    for letter in word.upper():
        score += chart.get(letter)
    if len(word) >= 7:
        score += 8
    return score
print(score_word("elephant"))


def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = ""
    for temp_word in word_list:
        temp_score = score_word(temp_word)
        if temp_score > highest_score:
            highest_score = temp_score
            winning_word = temp_word
            # use len() to get length of tiebreaker words
        elif temp_score == highest_score:
            if len(winning_word) == 10:
                continue
            if len(temp_word) < len(winning_word) and len(winning_word) != 10:
                highest_score = temp_score
                winning_word = temp_word
            elif len(temp_word) == 10:
                highest_score = temp_score
                winning_word = temp_word
    return winning_word, highest_score 
