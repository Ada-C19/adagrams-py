import random
def draw_letters():
    letters = {
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

    drawn_letter = []
    all_list = letters.items()
    mynew_list = list(all_list)
    
    while len(drawn_letter) < 10:
        random_number = random.randrange(0,len(mynew_list))
        letter_tuples = mynew_list[random_number]
        key = letter_tuples[0]
        value = letter_tuples[1]
        count_key_in_list = drawn_letter.count(key)

        if count_key_in_list < value:
            drawn_letter.append(key)

    print(drawn_letter)
    return drawn_letter

def uses_available_letters(word, letter_bank):
    
    found_count = 0
    for i in letter_bank:
        for j in word.upper():
            if i == j:
                found_count +=1
                break
        
    if found_count == len(word):
        return True
    else:
        return False

def score_word(word):

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

    count_point = 0
    for key_word in word.upper():
        count_point += points_dict[key_word]

    if len(word) in range(7, 11):
        count_point += 8

    return count_point

def get_highest_word_score(word_list):

    winner_word = ""
    winner_score = 0

    winner_dict = {}

    for word in word_list:
        score = score_word(word)
        winner_dict[word] = score

    for word, score in winner_dict.items():
        if winner_score < score:
            winner_score = score
            winner_word = word
        elif winner_score == score and len(word) == 10 and len(winner_word) != 10:
            winner_score = score
            winner_word = word
        elif winner_score == score and len(word) < len(winner_word) and len(winner_word) != 10:
            winner_score = score
            winner_word = word
        
    return (winner_word, winner_score)



