import random
import copy

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
    frequency_list = []
    hand = []
# adds letter to frequency_list based on the desired frequency
    for letter, frequency in letter_pool.items():
        frequency_list += letter * frequency

    while len(hand) < 10:
        random_letter = random.choice(frequency_list)
        #random.choice doing something..then loop
        frequency_list.remove(random_letter)
        hand.append(random_letter)

    return hand

def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)

    for letter in word.upper():
        if letter not in letter_bank_copy:
            return False
        elif letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
    return True

def score_word(word):
    scoring_system = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
        }
    
    word_score = 0

    for letter in word:
        for score, letters in scoring_system.items():
            if letter.upper() in letters:
                word_score += score

    #bonus if word is between 7 to 10 characters
    if 7 <= len(word) <=10:
        word_score += 8
    
    return word_score

def get_highest_word_score(word_list):
    words_with_scores = []

    for word in word_list:
        word_score = score_word(word)
        words_with_scores.append({word:word_score})

    highest_score_with_word = ("", 0)

    for pair in words_with_scores:
        for word, word_score in pair.items():
            if word_score >= highest_score_with_word[1] and len(word) == 10:
                return (word, word_score)
            elif word_score == highest_score_with_word[1] and len(word) < len(highest_score_with_word[0]):
                highest_score_with_word = (word, word_score)
            elif word_score > highest_score_with_word[1]:
                highest_score_with_word = (word, word_score)

    return highest_score_with_word

