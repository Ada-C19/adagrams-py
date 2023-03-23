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



# How do I get a big list with A * 9 etc?
# Why do I need to make a copy of my dictionary?
# letter_pool_list = list(LETTER_POOL)

# ********* SOLUTION 1 ******************

def draw_letters():
    big_list = []

    for letter, letter_quantity in LETTER_POOL.items():
        # loop needs to restart here
        big_dict = letter * letter_quantity
        for single_char in big_dict:
            big_list.append(single_char)
        # return big_list
    # print(big_list)

# we want to draw 10 random letters from the big_list
    draw_of_10_letters = []
    while len(draw_of_10_letters) < 10:
        random_letter = random.choice(big_list)
        draw_of_10_letters.append(random_letter)
        big_list.remove(random_letter)
    print(draw_of_10_letters)

    # for item in big_list:    
    #     random_letter = random.choice(big_list)
    #     draw_of_10_letters.append(random_letter)
    #     if len(draw_of_10_letters) == 9:
    #         print(draw_of_10_letters)
    return draw_of_10_letters

draw_letters()   

# we need to pop() a letter each iteration/draw
# ************ SOLUTION 1 END ******************



# def letter_frequency():
# We should only have the values as the quantity of the letters
# How do we establish
# What does distribution mean?
# keys * values?

    # The value of the keys of LETTER_POOL is its quantity
    # 


# ******* TEST 2 **********
def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass