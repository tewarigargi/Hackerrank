#Given an integer,n, perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20 , print Not Weird

#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

def weirdinteger(N):
    if N%2 == 1:
        print("Weird")
    elif N%2 == 0 and 2<=N<=5:
        print('Not Weird')
    elif N%2 == 0 and 6<= N <= 20:
        print('Weird')
    else:
        print('Not Weird')
    return 

if __name__ == '__main__':
    N = int(input())
    weirdinteger(N)
