"""
@Author: Ayur Ninawe
@Date: 2021-07-06 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-06 20:15:30
@Title : Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
"""

import loggerfile

def match_words(words):
    """
    Description:
        Function to count the number of strings where the string length
        is 2 or more and the first and last character are same from a given list of strings.
    Parameter:
        words : giving input list
    Return:    
    """
    try:
        ctr = 0
        for word in words:
            if len(word) > 1 and word[0] == word[-1]:
                ctr += 1
        return ctr
    except Exception :
        loggerfile.Logger("debug", "Invalid program")
    
if __name__ == '__main__':    
    print(match_words(['abc', 'xyz', 'aba', '1221']))