"""
Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency
"""

#The average score of class 
def Average(L):
    Sum = 0
    for i in L:
        if i != 'NA' or i != 'na' or i != 'Na' or i != 'nA':
            Sum = Sum + i
    Avg = Sum/len(L)
    return Avg

#Highest score and lowest score of class 
def Highest(L):
    Hi = 0
    for i in L:
        if i != 'NA' or i != 'na' or i != 'Na' or i != 'nA':
            if i > Hi:
                Hi = i
    return Hi

def Lowest(L):
    Lo = 100
    for i in L:
        if i != 'NA' or i != 'na' or i != 'Na' or i != 'nA':
            if i < Lo:
                Lo = i
    return Lo

#Count of students who were absent for the test
def Absent(L):
    c = 0
    for i in L:
        if i == 'NA' or i == 'na' or i == 'Na' or i == 'nA':
            c +=1
    return c

#Display mark with highest frequency
def Mode(L):
    max = 0
    res = L[0]
    for i in L:
        c=0
        for j in L:
            if i != 'NA' or i != 'na' or i != 'Na' or i != 'nA':
                if i == j:
                    c+=1
        if c>max:
            max=c
            res=i
    return i

n = int(input("Enter class strength "))
Marks = []
for i in range(0,n):
    L = input("Enter marks of the student (Type NA if absent):")
    if i != 'NA' or i != 'na' or i != 'Na' or i != 'nA':
        L = int(L)
    Marks.append(L)

print ("The average score of the class is:", Average(Marks))
print ("The highest score in the class is:", Highest(Marks))
print ("The lowest score in the class is:", Lowest(Marks))
print ("The number of students absent for the test are:", Absent(Marks))
print ("Marks with highest frequency is:", Mode(Marks))
