"""
@Author: Ayur Ninawe
@Date: 2021-06-28 16:23:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-06-28 16:23:30
@Title : Sum of three Integer adds to ZERO

"""

class Triplet:


    def findTriplets(self,arr, num):
        
    """
    Description:
        Function generates tripelets whose sum is zero
    Parameter:
        arr: array of elements
        num: no elements
    Return:
        array output
    """
        found = True
        for i in range(0, num - 2):

            for j in range(i + 1, num - 1):

                for k in range(j + 1, num):

                    if (arr[i] + arr[j] + arr[k] == 0):
                        print("*************Triplet **********")
                        print(arr[i], arr[j], arr[k])
                        found = True

        # If no triplet with 0 sum
        # found in array
        if (found == False):
            print(" not exist ")


if __name__ == '__main__':
    arr = []
    size = int(input("Enter the no of element: "))
    for i in range(size):
        element = int(input("Enter an elemnt : "))
        arr.append(element)
    print("*****Array Element***********")
    print(arr)
    print()

    num = len(arr)

    triplet=Triplet()
    triplet.findTriplets(arr,num)
