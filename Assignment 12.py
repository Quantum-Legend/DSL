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
            return "Element not Found!"
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
        return "Element not Found!"
    elif x > arr[mid]:
        low = mid + 1
        return binarySearch_Recursive(arr, x, low, hi)
    else:
        hi = mid - 1
        return binarySearch_Recursive(arr, x, low, hi)

#Fibonacci Search function
def FibonacciSearch(arr, x):
    return 0

seq = [1,2,4,5,6,8,9,12]
ch = 0
while(ch != 4):
    ch = int(input("\nEnter your choice-\n1. Binary Search Non Recursive Method\n2. Binary Search Non Recursive Method\n3. Fibonacci Search\n4. Exit\n>> "))
    n = int(input("Which element do you want to search?\n>> "))
    if ch == 1:
        print(f"The element is at {binarySearch_nonRecursive(seq, n)} position")
    elif ch == 2:
        print(f"The element is at {binarySearch_Recursive(seq, n, 0, len(seq)-1)} position")
    elif ch == 3:
        print("Fibonacci Search!")
    elif ch == 4:
        print("Exiting...")
    else:
        print("Wrong input! Please try again:")
