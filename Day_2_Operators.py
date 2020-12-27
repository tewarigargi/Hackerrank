#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

#Example
#A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value  and return from the function.

#Function Description
#int meal_cost: the cost of food before tip and tax
#int tip_percent: the tip percentage
#int tax_percent: the tax percentage
#Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

#Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

#Input Format

#There are  lines of numeric input:
#The first line has a double, meal cost (the cost of the meal before tax and tip).
The second line has an integer,tip percent (the percentage of meal cost being added as tip).
The third line has an integer, tax percent  (the percentage of meal cost being added as tax).

CODE
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

   
        tip_amt= float((tip_percent*meal_cost)/100)
        tax_amt= float((tax_percent*meal_cost)/100)
        total_cost=float(meal_cost+tip_amt+tax_amt)
        print(round(total_cost))
        return


if __name__ == '__main__':
        meal_cost = float(input())

        tip_percent = int(input())

        tax_percent = int(input())
        
        solve(meal_cost, tip_percent, tax_percent)
