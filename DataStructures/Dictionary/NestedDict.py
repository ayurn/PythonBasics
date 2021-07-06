"""
@Author: Ayur Ninawe
@Date: 2021-07-04 20:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-04 20:15:30
@Title :Write a Python program to convert a list into a nested dictionary of keys.
"""
import loggerfile        
        
def nested():        
    try:    
        num_list = [1, 2, 3, 4]
        new_dict = current = {}
        for name in num_list:
            current[name] = {}
            current = current[name]
        print(new_dict)
    except Exception :
        loggerfile.Logger("debug", "Invalid")
        
if __name__ == '__main__':
    nested()