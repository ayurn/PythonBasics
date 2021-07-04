"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:15:30
@Title : Write a Python script to sort (ascending and descending) a dictionary by value.
"""

import operator

def ascdes():
    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print('Original dictionary : ',d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    print('Dictionary in ascending order by value : ',sorted_d)
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    print('Dictionary in descending order by value : ',sorted_d)
    
if __name__ == '__main__':
    ascdes()