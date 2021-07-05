"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:15:30
@Title : Write a Python program to iterate over dictionaries using for loops.
"""
import loggerfile

def Iterate(dct):
    try:
        for key, value in dct.items():
            print(f"{key}--->{value}")
    except Exception as e:
        loggerfile.Logger("debug", "Invalid")
            
Iterate({'x': 10, 'y': 20, 'z': 30} )