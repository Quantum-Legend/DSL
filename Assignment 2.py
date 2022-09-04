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
        Sum = Sum + i
    Avg = Sum/len(L)
    return Avg

#Highest score and lowest score of class 
def Highest(L):
    Hi = 0
    for i in L:
        if i > Hi:
            Hi = i
    return Hi

def Lowest(L):
    Lo = 100
    for i in L:
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
""" def Mode(L):
    mode = 0
    pos = L[0]
    check = 0
    for i in L:
        c = -1
        if check == 1:
            continue
        else:
            for j in L:
                if j==i:
                    c+=1
                    check = 1 """

""" #Display mark with highest frequency
def Mode(List):
    Max = 0
    res = List[0]
    for i in List:
        freq = List.count(i)
        if freq > Max:
            Max = freq
            res = i
    return res """

n = int(input("Enter class strength "))
Marks = []
for i in range(0,n):
    L = int(input("Enter marks of the student (Type NA if absent):"))
    Marks.append(L)

print ("The average score of the class is:", Average(Marks))
print ("The highest score in the class is:", Highest(Marks))
print ("The lowest score in the class is:", Lowest(Marks))
print ("The number of students absent for the test are:", Absent(Marks))
#print ("Marks with highest frequency is:", Mode(Marks))
