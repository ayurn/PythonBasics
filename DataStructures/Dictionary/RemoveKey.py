"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:15:30
@Title : Write a Python program to remove a key from a dictionary.
"""

def DeleteKey(dct, key):
    print("Original Dictionary: ", dct)
    if key in dct:
        del dct[key]
    print("After Delete key, dictionary is: ", dct)
DeleteKey({'a':1,'b':2,'c':3,'d':4}, 'c')