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

player_one = []
pool_conversion = list(LETTER_POOL)

def draw_letters():

    re_ordered_list = random.sample(pool_conversion, len(pool_conversion))
    game_letters = re_ordered_list[:10]
    return game_letters



def uses_available_letters(word, letters):

    matches = []
    word = word.upper()
    for letter in word:
        if letter in letters:
            if matches.count(letter) < letters.count(letter):
                matches.append(letter)
            elif matches.count(letter) == letters.count(letter):
                continue
    
    if len(matches) == len(word):
        return True
    else:
        return False



points_dict = {
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
def score_word(word):

    score = 0
    for letter in word.upper():
        score += points_dict[letter]
    if len(word) >= 7 <= 10:
        score += 8
        

    return score


def get_highest_word_score(words):

    best_word = []
    word_scores = []
    high_value_words = []  

    for word in words:
        word_scores.append(score_word(word))
        max_score = max(word_scores)
    for i in range(len(word_scores)):
        if word_scores[i] == max_score:
            high_value_words.append(words[i])
            high_value_words.sort(key = len, reverse = True)
    for word in high_value_words:
        shortest_word = high_value_words[-1]
        if len(word) == 10:
            best_word.append(word)
            break
        else:
            best_word.append(shortest_word)
            break

    best_word.append(max_score)

    return best_word
