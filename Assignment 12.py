"""
a) Write a python program to store names and mobile numbers of your friends in sorted 
order on names. Search your friend from list using binary search (recursive and non-recursive). Insert friend if not present in phonebook
b) Write a python program to store names and mobile numbers of your friends in sorted 
order on names. Search your friend from list using Fibonacci search. Insert friend if not 
present in phonebook. 
"""

# Non Recursive Binary Search function
def binarySearch_nonRecursive(arr, x):
    hi = len(arr) - 1
    low = 0
    while True:
        mid = (low + hi)//2
        if x == arr[mid]:
            return mid
        elif low == hi:
            return -1
        elif x > arr[mid]:
            low = mid + 1
        else:
            hi = mid - 1

# Recursive Binary Search function
def binarySearch_Recursive(arr, x, low, hi):
    mid = (low + hi)//2
    if x == arr[mid]:
        return mid
    elif low == hi:
        return -1
    elif x > arr[mid]:
        low = mid + 1
        return binarySearch_Recursive(arr, x, low, hi)
    else:
        hi = mid - 1
        return binarySearch_Recursive(arr, x, low, hi)

#def fibonacci search function
def fibsearch(a,x):
    n=len(a)
    f1=0
    f2=1
    F=f1+f2

    while(F<n):
        f1=f2
        f2=F
        F=f1+f2
    offset=-1
    while(F>1):

        i=min(offset+f1,n-1)

        if a[i] < x :
            F = f2
            f2=f1
            f1=F-f2
            offset=i
        elif a[i] > x:
            F=f1
            f2=f2-f1
            f1=F-f2
        else :
            return i    
        
    if (f2 and a[n-1] == x):
        return n-1

    return -1

#Driver code
seq = [1,2,4,5,6,8,9,12]
ch = 0
while(ch != 4):
    ch = int(input("\nEnter your choice-\n1. Binary Search Non Recursive Method\n2. Binary Search Recursive Method\n3. Fibonacci Search\n4. Exit\n>> "))
    if ch !=4:
        x = int(input("Which element do you want to search?\n>> "))
        if ch == 1:
            i = binarySearch_nonRecursive(seq, x)
        elif ch == 2:
            i = binarySearch_Recursive(seq, x, 0, len(seq) - 1)
        elif ch == 3:
            i = fibsearch(seq, x)
        else:
            print("Wrong input! Please try again:")

        if i >= 0:
            print(f"The element {x} is at {i} position")
        else:
            print(f"The element {x} is not present in the list")
    else:
        print("Exiting...")
