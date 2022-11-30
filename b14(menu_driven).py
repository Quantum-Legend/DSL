"""Write a pythonprogram to store first year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores"""

def sel_sort_asc():
    for i in range(tot_stu):
        min_ele = i
        for j in range(i+1,tot_stu):
            if marks[min_ele] > marks[j]:                
                min_ele = j
                

        marks[i],marks[min_ele] = marks[min_ele],marks[i]

    print("Score after selection sort(ascending):", marks)
    input1 = int(input(">>>go back or continue?(1/2): "))
    if input1 == 1:
        menu()
    elif input1 == 2:
        sel_sort_desc()
    else:
        exit()

def sel_sort_desc():
    for i in range(tot_stu):
        min_ele = i
        for j in range(i+1,tot_stu):
            if marks[min_ele] < marks[j]:                
                min_ele = j
                

        marks[i],marks[min_ele] = marks[min_ele],marks[i]

    print("Score after selection sort(descending):", marks)
    input2 = int(input(">>>go back or continue?(1/2): "))
    if input2 == 1:
        menu()
    elif input2 == 2:
        bub_sort_asc()
    else:
        exit()

def bub_sort_asc():
    n = tot_stu
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Score after bubble sort(ascending):",marks)
    input3 = int(input(">>>go back or continue?(1/2): "))
    if input3 == 1:
        menu()
    elif input3== 2:
        bub_sort_desc()
    else:
        exit()
        
def bub_sort_desc():
    n = tot_stu
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] < marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Score after bubble sort(descending):",marks)
    print(marks)
    input4 = int(input(">>>go back or continue?(1/2): "))
    if input4 == 1:
        menu()
    elif input4 == 2:
        top_five()
    else:
        exit()
    
def top_five():
    n = tot_stu
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] < marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                
    top5 = []
    for value in range(0,5):
        top5.append(marks[value])
    print("Top 5 score of students",top5)
    print("=="*50)
        
        

    
    

def menu():
    print("=="*50)
    print("1) Selection sort")
    print("2) Bubble sort")
    print("3) Exit")

    i1 = int(input("Enter your choice: "))
    if i1 == 1:
        print("=="*50)
        print("1) Ascending")
        print("2) Descending")
        print("3) Go back")
        inp1 = int(input("Enter your choice: "))
        if inp1  == 1:
            sel_sort_asc()
        elif inp1 == 2:
            sel_sort_desc()
        elif inp1 == 3:
            menu()
        else:
            exit()
    elif i1 == 2:
        print("=="*50)
        print("1) Ascending")
        print("2) Descending")
        print("3) Top 5 percentages")
        print("4) Go back")
        inp2 = int(input("Enter your choice: "))
        if inp2 == 1:
            bub_sort_asc()
        elif inp2 == 2:
            bub_sort_desc()
        elif inp2 == 3:
            top_five()
        elif inp2 == 4:
            menu()
        else:
            exit()
    elif i1 == 3:
        exit()
    else:
        print("invalid coice!")
        menu()


marks = []
print("===="*30)
print("0~~~~|Enter the required data|~~~~00")
tot_stu = int(input("Total number of students: "))
print("===="*30)
for i in range(tot_stu):
    mks = int(input("Enter Percentage obtained by the students: "))
    marks.append(mks)
print("Score of",tot_stu,"students are",marks)
menu()
