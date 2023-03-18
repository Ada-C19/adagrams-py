import random

def draw_letters():
    LETTER_POOL = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 2,
        "Z": 1
    }

    hand_letters = []
    letters = list(LETTER_POOL.keys())
    
    while len(hand_letters) < 10:
        letter = random.choice(letters)
        if LETTER_POOL[letter] > 0:
            LETTER_POOL[letter] -= 1
            hand_letters.append(letter)
    return hand_letters

def uses_available_letters(word, letter_bank):
    copy_letter_bank = letter_bank[:]

    for letter in word.upper():
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            return False
        
    return True

def score_word(word):
    SCORE_CHART = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    score = 0
    score_chart_letters = list(SCORE_CHART.values())
    word_letters = list(word.upper())
    index_to_points = []

    for i in range(len(score_chart_letters)):
        for letter in score_chart_letters[i]:
            for j in range(len(word_letters)):
                if word_letters[j] == letter:
                    index_to_points.append(i)

    for each in index_to_points:
        if each == 0:
            score += 1
        elif each == 1:
            score += 2
        elif each == 2:
            score += 3
        elif each == 3:
            score += 4
        elif each == 4:
            score += 5
        elif each == 5:
            score += 8
        else:
            score += 10

    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    words_and_scores = {}
    highest_score = 0
    ties = 0

    for word in word_list:
        words_and_scores[word] = score_word(word)
    
    for score in words_and_scores.values():
        if score > highest_score:
            highest_score = score
        elif score == highest_score:
            ties += 1

    if ties == 0:
        for word, score in words_and_scores.items():
            if score == highest_score:
                return (word, score)
    else:
        tied_words = []
        for word, score in words_and_scores.items():
            if score == highest_score:
                tied_words.append(word)

        for word in tied_words:
            if len(word) == 10:
                return (word, words_and_scores[word])

        shortest_length = 10
        shortest_word = ""
        for i in range(len(tied_words)):
            if len(tied_words[i]) < shortest_length:
                shortest_length = len(tied_words[i])
                shortest_word = tied_words[i]
        return (shortest_word, words_and_scores[shortest_word])