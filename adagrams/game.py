import random



def draw_letters():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    relative_weights = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1] #how many of each letter in pool of letters
    weighted_list = []
    hand = []
    for i in range(len(letters)):
        weighted_list.extend(letters[i] * relative_weights[i]) #extended list with right number of each letter
    
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
    letter_scores = {
        "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3,
        "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
    }
    
    score = 0
    for letter in word:
        score += letter_scores[letter.upper()]
    if len(word) in [7, 8, 9, 10]:
        score += 8
    return score

def get_highest_word_score(word_list):

    winning_score = 0
    tied_words = []

    for word in word_list:
        score = score_word(word)
        # print(word + " " + str(score)) # for debugging
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
      

        

    