"""
@Author: Ayur Ninawe
@Date: 2021-07-06 14:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 14:15:30
@Title : Write a Python function that takes a list of words and returns the length of the longest one.
"""
import loggerfile

def find_longest_word(words_list):
    try:
        word_len = []
        for n in words_list:
            word_len.append((len(n), n))
        word_len.sort()
        return word_len[-1][0], word_len[-1][1]
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
        
result = find_longest_word(["Exercises", "Python", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])