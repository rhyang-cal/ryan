# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph.

def counting_vowels_and_consonants(string):
    vowels_list = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in string:
        if char.isalpha():
            if char in vowels_list:
                v_count += 1
            else:
                c_count += 1
    return (v_count, c_count) 

def average_vowels_and_consonants(string):
    number_of_sentences = 0
    sentence_enders = ["?","!","."]
    for char in string:
        if char in sentence_enders:
            number_of_sentences += 1
    v_total, c_total = counting_vowels_and_consonants(string)
    avg_vowel_per_sentence = v_total/number_of_sentences
    avg_con_per_sentence = c_total/number_of_sentences
    return (number_of_sentences,avg_vowel_per_sentence,avg_con_per_sentence)

num_sen, avg_v_sen, avg_c_sen = average_vowels_and_consonants(paragraph)
        
print(f"The average vowels per sentence of the paragraph is {avg_v_sen} and the average consonants per sentence of the paragraph is {avg_c_sen}")