"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:25:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:25:30
@Title : Write a Python script to generate and print a dictionary that 
         contains a number (between 1 and n) in the form (x, x*x).
"""
import loggerfile

def Generate(num):
    try:
        dct = {}
        for iterate in range(1, num+1):
            dct[iterate] = iterate*iterate
        print(dct)
    except Exception as e:
        loggerfile.Logger("debug", "Invalid")
Generate(5)
Generate(15)