""" 
Write a python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix
"""

#Input matrix
def MxOrigin():
    R = int(input("Enter no. of rows: "))
    C = int(input("Enter no. of columns: "))
    M =[]
    for i in range(R):
        #Iterating over rows of the matrix
        L=[] #List to store each row
        for j in range(C):
            #Iterating over columns of the matrix
            L.append(int(input("Enter element: "))) #Reading elements 
        M.append(L) #Appending each row as an element in the list
    return M

#Initializing a null matrix of order R x C
def MxInitial(R, C):
    M =[]
    for i in range(R):
        L=[]
        for j in range(C):
            L.append(0) 
        M.append(L)
    return M 

#Matrix dislayed in 2D format
def MxDisplay(M):
    if M != "Incorrect Input":
        for i in range(len(M)):
            for j in range(len(M[0])):
                print(M[i][j], '\t', end = '')
            print()
        print()
    else :
        print(M)

#Addition of two matrices
def MxAdd(M1, M2):
    if len(M1) == len(M2) and len(M1[0]) == len(M2[0]): #Addition of two matrices only possible if they have same order
        M3 = MxInitial(len(M1), len(M1[0]))
        for i in range(len(M1)):
            for j in range(len(M1[0])):
                M3[i][j] = M1[i][j] + M2[i][j]
        return M3
    else :
        return "Incorrect Input"

#Subtraction of two matrices
def MxSub(M1, M2):
    if len(M1) == len(M2) and len(M1[0]) == len(M2[0]): #Subtraction of two matrices only possible if they have same order 
        M3 = MxInitial(len(M1), len(M1[0]))
        for i in range(len(M1)):
            for j in range(len(M1[0])):
                M3[i][j] = M1[i][j] - M2[i][j]
        return M3
    else :
        return "Incorrect Input"

#Multiplication of two matrices
def MxMult(M1,M2):
    if len(M1[0]) == len(M2): #Multiplication of two matrices only possible if C1 = R2
        M3 = MxInitial(len(M1), len(M1[0])) #Order of the product matrix is R1 x C2
        for i in range(len(M1)): #iterating over R1 (Row of M1)
            for j in range(len(M2[0])): ##iterating over C2 (Column of M2)
                for k in range(len(M2)): ##iterating over R2 (Row of M2)
                    M3[i][j] += M1[i][k] * M2[k][j] #Sum of Products
        return M3
    else :
        return "Incorrect Input"


#Transpose of a matrix
def MxTrans(M):
    Mt = MxInitial(len(M[0]), len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            Mt[j][i] = M[i][j] 
    return Mt

#Main program
print("Enter elements of matrix left to right row-wise")
print("First Matrix: ")
M1 = MxOrigin()
print("Second Matrix: ")
M2 = MxOrigin()

print("First matrix: ")
MxDisplay(M1)
print("Second matrix: ")
MxDisplay(M2)
print("Sum of the 2 matrices: ")
MxDisplay(MxAdd(M1,M2))
print("Difference of the 2 matrices: ")
MxDisplay(MxSub(M1,M2))
print("Product of the 2 matrices: ")
MxDisplay(MxMult(M1,M2))
print("Transpose of 1st matrix: ")
MxDisplay(MxTrans(M1))
print("Transpose of 2nd matrix: ")
MxDisplay(MxTrans(M2))
