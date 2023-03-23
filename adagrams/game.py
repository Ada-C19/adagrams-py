def draw_letters():
    import random
    RANGE_LOW = 0
    RANGE_HIGH = 25

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

    list_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', "I", "J", "K", \
                       "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    hand = []
    while len(hand) < 10:
        random_number = random.randint(RANGE_LOW, RANGE_HIGH)
        letter = list_of_letters[random_number]
        letter_value = LETTER_POOL.get(letter)

        if letter in hand:
            n = hand.count(letter)
            if n < letter_value:
                hand.append(letter)
        else:
            hand.append(letter)
    print(hand)
    return hand                  


def uses_available_letters(word, letter_bank):
    word = word.upper()
    is_word_valid = True
    for letter in word:
        if letter not in letter_bank:
            is_word_valid = False
        else:
            v = letter_bank.count(letter)
            v2 = word.count(letter)
            if v2 > v:
                is_word_valid = False
    print(is_word_valid)
    return is_word_valid


def score_word(word):
    score_chart = {
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
    
    word = word.upper()
    score_sum = 0
    for letter in word:
        value = score_chart.get(letter)
        score_sum += value
    print(len(word))
    if len(word) >= 7 and len(word) <= 10:
        score_sum += 8
    print(score_sum)
    return(int(score_sum))


def get_highest_word_score(word_list):
    winner = []
    highest_score = 0
    highest_scored_word = ""

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            highest_scored_word = word
        if score == highest_score:
            if len(word) == len(highest_scored_word):
                highest_scored_word =  highest_scored_word
            elif len(word) < len(highest_scored_word) and len(highest_scored_word) != 10:
                highest_scored_word = word
            elif len(word) == 10 :
                highest_scored_word = word
            elif len(highest_scored_word) == 10: 
                highest_scored_word = highest_scored_word
    winner.insert(0, highest_scored_word)
    winner.insert(1, highest_score)
    the_winner = tuple(winner)
    return the_winner
