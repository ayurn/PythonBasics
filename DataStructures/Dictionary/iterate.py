"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:15:30
@Title : Write a Python program to iterate over dictionaries using for loops.
"""

def Iterate(dct):
    for key, value in dct.items():
        print(f"{key}--->{value}")
Iterate({'x': 10, 'y': 20, 'z': 30} )