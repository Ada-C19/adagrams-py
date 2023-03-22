import random 


def draw_letters():
    letters = (["A"] * 9 + ["B"] * 2 + ["C"] * 2 + ["D"] * 4 + ["E"] * 12 
               + ["F"] * 2 + ["G"] * 3 + ["H"] * 2 + ["I"] * 9 + ["J"]
               + ["K"] + ["L"] * 4 + ["M"] * 2 + ["N"] * 6 + ["O"] * 8
               + ["P"] * 2 + ["Q"] + ["R"] * 6 + ["S"] * 4 + ["T"] * 6
               + ["U"] * 4 + ["V"] * 2 + ["W"] * 2 + ["X"] + ["Y"] * 2
               + ["Z"])

    hand = random.sample(letters, k=10)

    return hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for char in word:
        if word.count(char) > letter_bank.count(char):
            return False 
    return True 


def score_word(word):
    letter_points = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, 
        "L": 1, "N": 1, "R": 1, "S": 1, "T": 1, 
        "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, 
        "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, 
        "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, 
        "Z": 10 
    }

    score = 8 if 7 <= len(word) <= 10 else 0

    for char in word:
        score += letter_points[char.upper()]
    return score


def get_highest_word_score(word_list):
    max_score = 0
    matching_scores = []
    word_dict = {}
    
    for word in word_list:
        score = score_word(word) 
        word_dict[word] = score

    max_score = max(word_dict.values())

    # Look for keys with the same score as max_score 
    # Append them to the matching_scores list
    for word in word_dict:
        if word_dict[word] == max_score:
            matching_scores.append(word)

    for word in matching_scores:
        if len(matching_scores) == 1:
            winning_word = word
        elif len(word) == 10:
            winning_word = word
            break 
        else:   
            i = 0 
            while i + 1 < len(matching_scores): 
                if len(matching_scores[i]) <= len(matching_scores[i + 1]):
                    winning_word = matching_scores[i]
                else:
                    winning_word = matching_scores[i + 1]
                i += 1

    return (winning_word, max_score)


