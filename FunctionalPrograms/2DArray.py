"""
@Author: Ayur Ninawe
@Date: 2021-06-28 15:23:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-06-28 15:23:30
@Title : A library for reading in 2D arrays of integers, doubles, or booleans from
         standard input and printing them out to standard output.

"""

import numpy as np
# array function is used to complete the task
class Matrix:

    # array function is created
    def twoDArray(self, row, col):
        
    """
    Description:
        Function generates array in the form of matrix
    Parameter:
        row: no of row
        col: no of col
    Return:
        array output
    """

        try:  # try is used for locating the error
            array = [[[np.random.randint(0, 10)] for i in range(row)] for j in range(col)]  # array is created by this function
            print(array)
            return array  # array is returned
        except IndexError:
            print("index error please check ")

if __name__ == "__main__":
    row = int(input("number of rows : "))
    col = int(input("number of coloumn : "))
    matrix=Matrix()
    matrix.twoDArray(row,col)