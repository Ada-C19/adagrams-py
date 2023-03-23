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

SCORE_CHART = {
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

SCORE_CHART_LOWERCASE = {
  'a': 1,
  'b': 3,
  'c': 3,
  'd': 2,
  'e': 1,
  'f': 4,
  'g': 2,
  'h': 4,
  'i': 1,
  'j': 8,
  'k': 5,
  'l': 1,
  'm': 3,
  'n': 1,
  'o': 1,
  'p': 3,
  'q': 10,
  'r': 1,
  's': 1,
  't': 1,
  'u': 1,
  'v': 4,
  'w': 4,
  'x': 8,
  'y': 4,
  'z': 10
}

temp_list = []
LETTER_POOL_LIST = []
hand = []
hand_quantity = 10

def draw_letters():

  # Create a comprehensive list which includes the total quanity of each available letter from the LETTER_POOL dictionary as individual elements. 
  for key, value in LETTER_POOL.items():
    temp_list.append([key] * value)
  
  for sublist in temp_list:
    for letter in sublist:
      LETTER_POOL_LIST.append(letter)
  #print(LETTER_POOL_LIST)

  # Choose 10 random letters as hand, excluding the ones that are already chosen.
  return random.sample(LETTER_POOL_LIST, hand_quantity)
  #print(random.sample(LETTER_POOL_LIST, hand_quantity))

def uses_available_letters(word, letter_bank):       
    word_verification = []
    hand_letter_count = {}
    word_letter_count = {}
    count = 0
    capitalized_word = word.upper()

    for letter in letter_bank:
        if letter not in hand_letter_count:
            count = 1
            hand_letter_count[letter] = count
            #print(hand_letter_count)
        else: 
            count += 1
            hand_letter_count[letter] = count
            #print(hand_letter_count)
    
    for letter in capitalized_word:
        letter_quantity = capitalized_word.count(letter)
        word_letter_count[letter] = letter_quantity
        #print(word_letter_count)

        if letter in letter_bank and word_letter_count[letter] <= hand_letter_count[letter]:
            word_verification.append("True")
            #print(word_verification)
        else:
            word_verification.append("False")
            #print(word_verification)
    
    if "False" in word_verification:
        return False
        #print("False")
    else:
        return True
        #print("True")
    

def score_word(word):
    word_score = {}
    for letter in word:
       if letter in SCORE_CHART:
          word_score[letter] = SCORE_CHART[letter]
       elif letter in SCORE_CHART_LOWERCASE:
          word_score[letter] = SCORE_CHART_LOWERCASE[letter]
    #print(word_score)

    return sum(word_score.values())


def get_highest_word_score(word_list):
    pass