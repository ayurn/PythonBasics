"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:30:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:30:30
@Title : Write a Python program to print all unique values in a dictionary.
"""

dta =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
lst = []

def unique():
    for i in dta:
        for key, value in i.items():
            if value not in lst:
                lst.append(value)
    print("Unique values: ",set(lst))
    
if __name__ == '__main__':
    unique()