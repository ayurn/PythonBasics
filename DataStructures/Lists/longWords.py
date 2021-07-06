"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to find the list of words that are longer than n from a
given list of words.
"""

import loggerfile

def long_words(n, str):
    
    """
    Description:
        Function to find the list of words that are longer than n from a given list of words.
    Parameter:
        n: length of word
        str : input string
    Return:
        words which are greater than n.
    """
    try:        
        word_len = []
        txt = str.split(" ")
        for x in txt:
            if len(x) > n:
                word_len.append(x)
        return word_len
    except Exception :
        loggerfile.Logger("debug", "Invalid program")	
        
if __name__ == '__main__':
    print(long_words(4, "The quick brown fox jumps over the lazy dog"))