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
#Creating a letter list from dictionary!
#We're splitting letters and then throwing them in the pile :-)
split_box = []
#Pulling keys + values from the letter pool, multiplying keys by values and putting into the split_box
for letter, freq in LETTER_POOL.items():
    letter_multiplied = letter * freq
    split_box.append(letter_multiplied)
#new list for all the new letters we've split up!
letter_pile = [c for letter in split_box for c in letter]

#Wave 1
def draw_letters():
    hand = []
    #Drawing 10 letters
    for i in range(10):
        char = random.choice(letter_pile)
        hand.append(char)
    #When a letter is overused!
    for letter in hand:
        if hand.count(letter) > LETTER_POOL[letter]:
            #Removes letter if it's over the # in pool
            hand.remove(letter)
            #Adds a brand new random letter when the length is under 10.. which it should bc lol
            if len(hand) < 10:
                hand.append(random.choice(letter_pile))
    return hand

#wave 2
def uses_available_letters(word, letter_bank):
    #Ignore cases by making word all upper
    word = word.upper()
    #Loop through each letter in word, and checking if it's the letter bank
    for char in word:
        if char in letter_bank and word.count(char) == letter_bank.count(char):
            result = True
        else:
            result = False
    #Counts + compares to the letter bank
    #if word.count(char) > letter_bank.count(char):
        #return False
    return result

def score_word(word):
    score = 0
    #Setting lists for letters + points
    #one_point = ["A","E","I","O","U","L","N","R","S","T"]
    #two_pts = ["D","G"]
    #three_pts = ["B","C","M","P"]
    #four_pts = ["F","H","V","W","Y"]
    #eight_pts = ["J","X"]
    #ten_pts = ["Q","Z"]
    #Making sure words evaluated are uppercase
    word = word.upper()
    #Loop through each letter + add to get each score
    for letter in word:
        if letter != letter.isalpha():
            score += 0
        if letter == letter in ["A","E","I","O","U","L","N","R","S","T"]:
            score += 1
        elif letter == letter in ["D","G"]:
            score += 2
        elif letter == letter in ["B","C","M","P"]:
            score += 3
        elif letter == letter in ["F","H","V","W","Y"]:
            score += 4
        elif letter == "K":
            score += 5
        elif letter == letter in ["J","X"]:
            score += 8
        elif letter == letter in ["Q","Z"]:
            score += 10
        
    #Lastly, checking to see if that word's length = bonus :)
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    #Calling scores to make scores for each word in list!
    scores = [score_word(word) for word in word_list]
    words = [word for word in word_list]
    high_scores = {word:score for (word,score) in zip(words,scores)}
    #make best_word into an empty list!
    best_word = []
    #storing the max score + word:
    max_word = max(high_scores, key=high_scores.get)
    max_score = max(high_scores.values())
    #So we'll do it by tie conditions. We set Tie to 0.
    tie = 0
#A loop to count how many ties we got
    for word in high_scores:
        if high_scores[word] == max_score:
            tie += 1
        else:
            tie == 0
#Start with the highest amount of ties
    if tie > 4:
        for x in words:
            if len(x) == 10 and len(max_word) != 10:
                max_word = x
                if words.index(x) < words.index(max_word):
                    max_word = x
# When ties are >= 3:
    elif tie >= 3:
        test_word = words[0]
        for y in words:
            if len(y) < len(test_word):
                test_word = y
        max_word = test_word
#When there's a tie of two words and the conditions that need to be met
    elif tie == 2:
        test_word = words[0]
        for y in words:
            if len(test_word) == 10 and len(y) == 10:
                max_word = test_word
            elif len(test_word) != 10 and len(y) == 10:
                max_word = y
            elif len(test_word) != 10 and len(y) != 10:
                    if len(y) < len(test_word):
                        max_word = y
            
        
    elif tie < 2:
        for word, score in high_scores.items():
            if score == max_score and len(word) == 10:
                for x in words:
                    if len(max_word) == 10 and len(x) == 10:
                        if words.index(x) < words.index(max_word):
                            max_word = x
                    else:
                        max_word = word
    best_word.extend([max_word, max_score])
    return best_word