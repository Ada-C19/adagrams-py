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
    drawn_letters = []
    letter_pool = dict(LETTER_POOL)

    while len(drawn_letters) < 10:

        weighted_letters = []
        for letter, count in letter_pool.items():
            weighted_letters += [letter] * count
        
        selected_letter = random.choice(weighted_letters)

        letter_pool[selected_letter] -= 1

        if letter_pool[selected_letter]== 0:
            del letter_pool[selected_letter]
        
        drawn_letters.append(selected_letter)

    return drawn_letters

def uses_available_letters(word, letter_bank):
   
    bank_copy = letter_bank[:]
    word_upper = word.upper()

    for letter in word_upper:
        if letter not in bank_copy or bank_copy.count(letter)== 0:
            return False
        else:
            bank_copy.remove(letter)
    return True

def score_word(word):
    points = 0
    word = word.upper()
    for letter in word:
        if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            points += 1
        elif letter in ['D', 'G']:
            points += 2
        elif letter in ['B', 'C', 'M', 'P']:
            points += 3
        elif letter in ['F', 'H', 'V','W', 'Y']:
            points += 4
        elif letter in ['K']:
            points +=5
        elif letter in ['J', 'X']:
            points += 8
        elif letter in ['Q', 'Z']:
            points += 10
    if len(word) in [7,8,9,10]:
        points += 8
    return points

def get_highest_word_score(word_list):
    highest_score = 0
    highest_scoring_words = []
    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score
            highest_scoring_words = [word]
        elif word_score == highest_score:
            highest_scoring_words.append(word)

    if len(highest_scoring_words) == 1:
        return (highest_scoring_words[0], highest_score)
    
    ten_letter_words = [word for word in highest_scoring_words if len(word) == 10]
    if len(ten_letter_words) == 1:
        return (ten_letter_words[0], highest_score)
    elif len(ten_letter_words) > 1:
        ten_letter_words.sort(key =len)
        return (ten_letter_words[0], highest_score)
    highest_scoring_words.sort(key=len)
    return (highest_scoring_words[0], highest_score)
    # best_word = None 
    # best_score = 0

    # for word in word_list:
    #     word_score = score_word(word)

    #     if word_score  > best_score:
    #         best_word = word
    #         best_score = word_score

    #     elif word_score == best_score:
    #         if len(word) == 10:
    #             if len(best_word) < 10:
    #                 best_word = word

    #         elif len(word) < len(best_word):
    #             best_word = word

    # return (best_word, best_score)
                