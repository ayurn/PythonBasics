"""
@Author: Ayur Ninawe
@Date: 2021-06-26 12:09:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-06-26 12:09:30
@Title : Print the year is a Leap Year or not.

"""

year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
