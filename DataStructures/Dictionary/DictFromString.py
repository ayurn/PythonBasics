"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:30:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:30:30
@Title : Write a Python program to create a dictionary from a string.
        Note: Track the count of the letters from the string.
        Sample string : 'w3resource'
"""
import loggerfile
from collections import defaultdict, Counter

def from_string():
    try:
        str1 = 'w3resource' 
        my_dict = {}
        for letter in str1:
            my_dict[letter] = my_dict.get(letter, 0) + 1
        print(my_dict)
    except Exception as e:
        loggerfile.Logger("debug", print(e))

if __name__ == '__main__':
    from_string()