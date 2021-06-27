"""
@Author: Ayur Ninawe
@Date: 2021-06-26 16:37:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-06-26 16:37:30
@Title : Computes the prime factorization of N using brute force.

"""

import math

class Factors:
    def Factors(self):
        
        print("Enter Number : ")
        n = int(input())
        print("Prime factors for", n, "is")
        #Printing the factors of a given number until it is divided by 2.
        while n % 2 == 0:
                print("2")
                n = n / 2

        #If the given number is not even then this loop will print the remaining factors.
        for i in range(3, int(math.sqrt(n)+1)):
            while n % i == 0:
                print(i)
                n = n / i
            i+=2

        #If the remaining factor is greater than 2 it will be printing
        if n > 2:
            print(n)
        else:
            print()
nums = Factors()
nums.Factors()
