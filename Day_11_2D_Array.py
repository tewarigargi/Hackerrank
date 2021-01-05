#Context Given a 2D Array, :

#1 1 1 0 0 0 
!0 1 0 0 0 0 
#1 1 1 0 0 0 
#0 0 0 0 0 0 
#0 0 0 0 0 0 
#0 0 0 0 0 0 
#We define an hourglass in to be a subset of values with indices falling in this pattern in 's graphical representation:

#a b c 
   #d 
#e f g 
#There are hourglasses in , and an hourglass sum is the sum of an hourglass' values.

#Task Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

#Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

#Input Format

#There are lines of input, where each line contains space-separated integers describing 2D Array ; every value in will be in the inclusive range of to .

#Output Format

#Print the maximum hourglass sum in A

#Sample Input

#1 1 1 0 0 0 0 
#1 0 0 0 0 1 1 
#1 0 0 0 0 0 2 
#4 4 0 0 0 0 2 
#0 0 0 0 1 2 4 
#Sample Output

#19 

#Code:

import sys


a = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   a.append(arr_t)
    
sumslist = []

def calculatesum(i,j):
    return(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2])

for j in range(0,4):
    for i in range(0,4):
        sum = calculatesum(i,j)
        sumslist.append(sum)
    
print(max(sumslist))
