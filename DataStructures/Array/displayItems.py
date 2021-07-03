"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:10:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:10:30
@Title : Write a Python program to create an array of 5 integers and display 
         the array items. Access individual element through indexes.
"""

import array as arr

class Arrayelement():
    def display(self):
        ar = arr.array('i', [1, 3, 5, 9, 7])
        print(ar)
        print(ar[0])
        print(ar[3])
        
if __name__ == '__main__':
    Arrayelement.display(0)