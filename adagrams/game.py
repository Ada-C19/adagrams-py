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
    letter_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'X', 'Y', 'Y', 'Z']
    players_hand = []


    while len(players_hand) < 10:
        random_letter = random.choice(letter_list) 
        players_hand.append(random_letter)
        
        letter_list.remove(random_letter)

    return players_hand




def uses_available_letters(word, letter_bank):
    word = word.upper()

    for letter in word:
        if word.count(letter) > letter_bank.count(letter):
            return False
    
    return True 
        


    
def score_word(word):
    score_dict = {
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

    result = 0
    for letter in word.upper():
        result += score_dict[letter]
    if len(word) >= 7:
        result += 8
    
    return result



def get_highest_word_score(word_list):
    high_score = 0
    best_word = ""

    for word in word_list:
        score = score_word(word)

        if score > high_score:
            high_score = score
            best_word = word


        elif score == high_score:
            if len(best_word) == 10:
                continue
            elif len(word) == 10:
                high_score = score
                best_word = word

            elif len(word) < len(best_word) :
                high_score = score
                best_word = word 
    

    return best_word, high_score 

# - Has one parameter: `word_list`, which is a list of strings
# - Returns a tuple that represents the data of a winning word and it's score.  The tuple must contain the following elements:
#   - index 0 ([0]): a string of a word
#   - index 1 ([1]): the score of that word
# - In the case of tie in scores, use these tie-breaking rules:
#     - prefer the word with the fewest letters...
#     - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
#     - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list



