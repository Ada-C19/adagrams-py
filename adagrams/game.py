import random
import string

letter_score_dict = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2, 
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3, 
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }

letter_pool = ["A", "A", "A", "A", "A", "A", "A", "A", "A",
                "B", "B",
                "C", "C",
                "D", "D", "D", "D",
                "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
                "F", "F",
                "G", "G", "G",
                "H", "H",
                "I", "I", "I", "I", "I", "I", "I", "I", "I",
                "J",
                "K",
                "L", "L", "L", "L",
                "M", "M",
                "N", "N", "N", "N", "N", "N",
                "O", "O", "O", "O", "O", "O", "O", "O",
                "P", "P",
                "Q",
                "R", "R", "R", "R", "R", "R",
                "S", "S", "S", "S",
                "T", "T", "T", "T", "T", "T",
                "U", "U", "U", "U",
                "V", "V",
                "W", "W",
                "X",
                "Y", "Y",
                "Z"
    ]


def draw_letters():
    random.shuffle(letter_pool)

    # Take the first 10 letters from the shuffled pool
    letters = letter_pool[:10]

    return letters
    
def uses_available_letters(word, letter_bank):
    letter_dict = {}
    word_dict = {}
    
    for item in letter_bank:
        if (item in letter_dict):
            letter_dict[item] += 1
        else:
            letter_dict[item] = 1

    for elem in word.upper():
        if (elem in word_dict):
            word_dict[elem] += 1
        else:
            word_dict[elem] = 1

    
    #returns false if any submitted letters in letter_bank are incorrect

    for key, value in word_dict.items():
        if key not in letter_dict or not value <= letter_dict[key]:
            return False
    return True

def score_word(word):  
    letter_score_dict = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10,
        'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    # dict that holds the key value pairs of letters and their scores.
    #variable that scores will be added to
    score_total = 0
    # variable to keep track of the length of each word
    #for each letter in the word: 
    for char in word.upper():
        score_total += letter_score_dict[char]

    if  7 <= len(word) <= 10:
        score_total += 8  
    return score_total
    
def get_highest_word_score(word_list):
    best_word = ""
    max_score = 0
    
    for word in word_list:
        score = score_word(word)
        
        if score > max_score:
            best_word = word
            max_score = score
        elif score == max_score:
            if len(best_word) != 10 and len(word) != 10:
                if len(word) < len(best_word) or len(best_word) == 10:
                    best_word = word
            elif len(best_word) != 10 and len(word) == 10:
                best_word = word
    
    return (best_word, max_score)


