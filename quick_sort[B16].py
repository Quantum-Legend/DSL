""" 
Write a python program to store first year percentage of students in array.
Write functionfor sorting array of floating point numbers in ascending order
using quick sort and display top five scores.
"""

#Quick Sort
def quicksort(seq):
    if len(seq) > 1:
        p = seq[0]
        i = 1
        j = len(seq)-1
        while i <= j:
            if not(seq[i] < p and seq[j] >= p):
                seq[i], seq[j] = seq[j], seq[i]
            if seq[i] < p:
                i+=1
            if seq[j] >= p:
                j-=1
        seq[0], seq[j] = seq[j], seq[0]
        p = j
        L1 = []
        L2 = []
        for x in range(0, p):
            L1.append(seq[x])
        for x in range(p+1, len(seq)):
            L2.append(seq[x])
        return quicksort(L1) + [seq[p]] + quicksort(L2)
    else:
        return seq

#Top five percentage:
def top5(L):
    if len(L) >= 5:
        for i in range(1,6):
            A = L[len(L)-i]
            print(A)
    else:
        for i in range(len(L)):
            print(L[i])

#Main
n = int(input("Enter no. of students: "))
L = []
for i in range(n):
    L.append(int(input("Enter percentage of student {0:d}: ".format(i+1))))
print(f"The percentages entered are: {L}")
print("Top five percentages:-")
top5(quicksort(L))

