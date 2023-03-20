import random



def draw_letters():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    relative_weights = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
    weighted_list = []
    hand = []
    for i in range(len(letters)):
        weighted_list.extend(letters[i] * relative_weights[i])
    
    while len(hand) < 10:
        random_letter = random.choice(weighted_list)
        weighted_list.remove(random_letter)
        hand.append(random_letter)

    return hand

def uses_available_letters(word, letter_bank):
    uniform_word = word.upper()
    uniform_letter_bank = [letter.upper() for letter in letter_bank]
    word_dict = {}
    letter_bank_dict = {}
    
    for letter in uniform_letter_bank:
        if letter not in letter_bank_dict:
            letter_bank_dict[letter] = 1
        elif letter in letter_bank_dict:
            letter_bank_dict[letter] += 1

    
    for letter in uniform_word:
        if letter not in word_dict:
            word_dict[letter] = 1
        elif letter in word_dict:
            word_dict[letter] += 1
        
        if letter not in letter_bank_dict or word_dict[letter] > letter_bank_dict[letter]:
            return False
        
  
    return True 


def score_word(word):
    score = 0
    uniform_case_word = word.upper()

    point_dict = {
        ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1,
        ("D", "G"): 2,
        ("B", "C", "M", "P") : 3,
        ("F", "H", "V", "W", "Y") : 4,
        ("K") : 5,
        ("J", "X") : 8,
        ("Q", "Z") : 10
    }
    

    for letter in uniform_case_word:
        for tuple in point_dict:
            if letter in tuple:
                score += point_dict[tuple]
        
    if len(word) >= 7:
            score += 8


    return score 

def get_highest_word_score(word_list):

    winning_score = 0
    tied_words = []

    for word in word_list:
        score = score_word(word)
        print(word + " " + str(score))
        if score > winning_score:
            winning_score = score
            tied_words = [word] 
        elif score == winning_score:
            tied_words.append(word)


    winning_word = tied_words[0]
    winning_word_letter_count = len(winning_word)

    for word in tied_words:
        if len(word) == 10:
            return word, winning_score
        elif len(word) < winning_word_letter_count:
            winning_word = word
            winning_word_letter_count = len(word)

    return winning_word, score_word(winning_word)
      

        

    