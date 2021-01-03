Today, we're learning and practicing an algorithmic concept called Recursion. Check out the Tutorial tab for learning materials and an instructional video!

Recursive Method for Calculating Factorial


#Task
#Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

#Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

#Input Format
#2 <= N <= 12
#A single integer, N (the argument to pass to factorial).
#Output Format
#Print a single integer denoting N!.

#Sample Input
#3 
#Sample Output
#6
#Code:


import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
   if n<=1:
    return 1
   else:
    return (n* factorial(n-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
