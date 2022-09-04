#The average score of class 
def Average(List, count):
    Sum = 0
    for i in List:
        Sum = Sum + i
    Avg = Sum/count
    return Avg

#Highest score and lowest score of class 
def Highest(List):
    return max(List)

def Lowest(List):
    return min(List)

#Count of students who were absent for the test
def Absent(Strength, Present):
    return Strength - Present

#Display mark with highest frequency
def Mode(List):
    Max = 0
    res = List[0]
    for i in List:
        freq = List.count(i)
        if freq > Max:
            Max = freq
            res = i
    return res

N = int(input("Strength of class:"))
n = int(input("No. of students present for test:"))
Marks = []
for i in range(0,n):
    L = int(input("Enter marks of the student:"))
    Marks.append(L)

print ("The average score of the class is:", Average(Marks,n))
print ("The highest score in the class is:", Highest(Marks))
print ("The lowest score in the class is:", Lowest(Marks))
print ("The number of students absent for the test are:", Absent(N,n))
print ("Marks with highest frequency is:", Mode(Marks))
