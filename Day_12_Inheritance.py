#Objective
#Today, we’re delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video!

#Task
#You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

#Complete the Student class by writing the following:

#A Student class constructor, which has parameters:
#A string, firstName.
#A string, lastName.
#An integer, idNumber.
#An integer array (or vector) of test scores,
#A char calculate() method that calculates a Student object’s average and returns the grade character representative of their calculated average

#The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

#You are not responsible for reading the following input from stdin:

#Output Format:
Name: Memelli, Heraldo
ID: 8135627
Grade: O

#This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

#Sample Input

#Heraldo Memelli 8135627
#2
#100 80
#Sample Output

#Name: Memelli, Heraldo
#ID: 8135627
#Grade: O
#Explanation

#This student had scores to average: and . The student’s average grade is . An average grade of corresponds to the letter grade , so our calculate() method should return the character’O’.
#Code:
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    
    def calculate(self):
        sum = 0
        for score in self.scores:
            sum += score
        average = int(sum/len(self.scores))
        if average >= 90 and average <=100:
            return 'O'
        elif average >= 80 and average <90:
            return 'E'
        elif average >= 70 and average <80:
            return 'A'
        elif average >= 55 and average <70:
            return 'P'
        elif average >= 40 and average <55:
            return 'D'
        elif average < 40:
            return 'T'
        else:
            return "sum >100 or sum < 0"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

