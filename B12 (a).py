"""a) Write a python program to store names and mobile numbers of your friends in sorted
order on names. Search your friend from list using binary search (recursive and nonrecursive). Insert friend if not present in phonebook
"""
import math
def sort(phnbk):
    for i in range(len(phnbk)):
        swp = 0
        j = 0
        while j < len(phnbk) - 1:
            if phnbk[j][0] > phnbk[j+1][0]:
                phnbk[j],phnbk[j+1] = phnbk[j+1],phnbk[j]
                swp = 1
            j += 1
        if swp == 0:
            break
        print("Phonebook:: ")
        print(phnbk)
        main()
    





    
def rec_bin_search(arr,left,right,x):
    if right >= left:
        mid = (right + left)//2
        if phnbk[mid][0] == x:
            return mid
        elif phnbk[mid][0] > x:
            return rec_bin_search(arr,left,mid-1,x)
        else:
            return rec_bin_search(arr,mid+1,right,x)
    else:
        return -1
    
def nr_bin_search(phnbk,left,right,key):
    mid = 0
    while(left<=right):
        s1 = left + right
        m1 = s1/2
        mid = math.ceil(m1)
        if (phnbk[mid][0] == key):
            return mid
        elif (phnbk[mid][0] < key):
            left = mid + 1
        elif (phnbk[mid][0] > key):
            right = mid - 1
    return -1
            


def insert_dir():
    r = 0
    while r == 0:
        temp = []
        name = input("Enter name: ")
        phone = int(input("Enter phone number: "))
        temp.append(name)
        temp.append(phone)
        phnbk.append(temp)
        temp = []
        cnt = input("Insert more?(y/n): ")
        if cnt == "y":
            insert_dir()
        elif cnt == "n":
            main()
        else:
            print("Incorrect choice!")
            main()






#main
def main():
    print("#MENU#")
    print("1) Store data")
    print("2) Print directory(sorted)")
    print("3) Perform binary search")
    print("4) Exit")
    inp = int(input("Insert your choice: "))
    if inp == 1:
        insert_dir()
    elif inp == 2:
        sort(phnbk)
    elif inp == 3:
        x = input("Name of friend, you want to search: ")
        
        print("1) Recursive")
        print("2) Non-recursive")
        choice = int(input("Select from above: "))
        if choice == 1:
            result = rec_bin_search(phnbk,0,len(phnbk)-1,x)
            if result != -1:
                print("Name is present at index",str(result))
                main()
            else:
                print("Name of friend is not present.")
                print("Proceeding to add it to the dir.")
                insert_dir()
        elif choice == 2:
            result = nr_bin_search(phnbk,0,len(phnbk)-1,x)
            if result != -1:
                print("Name is present at index",str(result))
                main()
            else:
                print("Name of friend is not present.")
                print("Proceeding to add it to the dir.")
                insert_dir()
            

        else:
            print("Invalid choice!")
            main()
    elif inp == 4:
        exit()
    else:
        print("Incorrect choice!")
        main()

phnbk = []#empty directory
main()
