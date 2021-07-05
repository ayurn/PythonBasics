"""
@Author: Ayur Ninawe
@Date: 2021-07-03 18:15:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-03 18:15:30
@Title : Write a Python script to concatenate following dictionaries to create a new one.
        Sample Dictionary :
        dic1={1:10, 2:20}
        dic2={3:30, 4:40}
        dic3={5:50,6:60}
        Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
import loggerfile

def concat():
    try:
        dic1 = {1:10, 2:20}
        dic2 = {3:30, 4:40}
        dic3 = {5:50,6:60}
        dct = dict()
        for d in (dic1, dic2, dic3):
            dct.update(d)
        print("New Dictionary: ", dct)
    except Exception as e:
        loggerfile.Logger("debug", "Invalid")
    
if __name__ == '__main__':
    concat()
