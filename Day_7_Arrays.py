#Objective
#Today, we’re learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!
#Task
#Given an array, , of integers, print ‘s elements in reverse order as a single line of space-separated numbers.
#Sample Input
#4
#1 4 3 2
#Sample Output
#2 3 4 1
#Constraints:
#1<=N<=1000
#1<=A[i]<=1000, where A[i] is the ith integer in the array

#Code:
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    for o in reversed(arr):
        print(o, end=" ")
