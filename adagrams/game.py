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
    '''
    This function returns a list of 10 random letters. It represents the 
    hand of letters that a player has drawn. It takes into account 
    the number of letters available for each letter. 
    Input: no parameters
    Output: Returns a list of 10 letters. 
    '''
    
    #creating a copy of LETTER_POOL
    letter_amount_dict = LETTER_POOL.copy()
    letters_list = []


    while len(letters_list) < 10:

        #getting random letter and resepctive number_of_letters,
        #first converted letter_amount_dict to a list ea. element has (key-value pair)
        letter, number_of_letters = random.choice(list(letter_amount_dict.items()))

        if number_of_letters > 0:
            #decrement number_of_letters from our letter_amount_dict
            letter_amount_dict[letter] = number_of_letters -1 
            #append the current letter to our letters_list
            letters_list.append(letter)

    return letters_list

def uses_available_letters(word, letter_bank):
    """
    This function takes in two parametrs. Return true if word is available
    w/ right quantities from letter_bank. Return False if letter in word is 
    not in letter_bank.
    input: word is some word and it's a string
         letter_bank is an array of 10 strings that represent drawn letters
    output: return True or False
    """
    
    #change word to all upper case
    uppercase_word = word.upper()

    #created a copy of letter_bank
    letter_bank_copy = letter_bank.copy()

    #converted capital_word to list and set it to letter_list
    letter_list = list(uppercase_word)


    #for each letter in the word_list
    for letter in letter_list:
        #if letter is in the updated_bank
        if letter in letter_bank_copy:
            #remove that letter from updated_bank
            letter_bank_copy.remove(letter)
        #if letter is not in letter_bank_copy
        elif letter not in letter_bank_copy:
            return False
    
    return True


def score_word(word):
    """
    This function returns the score of a given word. If 
    length of the word is 7-10, then word gets an additional 8 points.
    input: one parameter: word, which is a string
    output: returns an integer that represents the score
    """
    score_pool = {
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
    #initalize score to 0
    score = 0

    word_length = len(word)
    #for each letter in uppercase word
    for letter in word.upper():
        #add score of letter from score_pool
        score += score_pool[letter]
    #if word is between 7-10 length
    if word_length >= 7 and word_length <= 10:
        score += 8 
    return score

def get_highest_word_score(word_list):
    """
    This function finds the highest scored word from word_list. If there's a 
    tie: the word with 10 letters wins. if no ten letters, then prefer word
    with fewest word. If a tie and same length, pick first word in supplied
    list.
    input: one parameter: word_list is a list of strings
    output: returns a tuple of highest scored word (word, score)
    """
    word_dict = {}
    highest_scored_word = ""
    highest_scored_word_score = 0
    score_set = set()
    lengths_of_words = []
    

    for word in word_list:
      word_score = score_word(word)
      #append scores to score_set
      score_set.add(word_score)
      #creating a dict too hahah
      word_dict[word] = word_score
      #create a list of length of words ....
      lengths_of_words.append(len(word))
      
    #high score of set
    # high_score = max(score_set)
    high_score = max(word_dict.values())
    common_high_score = 0
    #create common numnnersof high score
    for score in word_dict.values():
      if score == high_score:
        common_high_score += 1

    #smallest length of word as a number.
    # smallest_length_word = min(lengths_of_words)


    # print("highscore", high_score)
    # print("commonhighscore", common_high_score)


    if common_high_score == 1:
      score = high_score
      word = max(word_dict, key=word_dict.get)
      return word, score
    else:
      for word, score in word_dict.items():
        if len(word) == 10:
          return word, score
        # elif len(word) == smallest_length_word:
        #   smallest_word = min(word_dict, key=len)
        #   return smallest_word, score
        elif max(lengths_of_words) < 10:
          print(word_dict, "dict")
          smallest_word = min(word_dict, key=len)
          smallest_word_score = word_dict[smallest_word]
          return smallest_word, smallest_word_score




