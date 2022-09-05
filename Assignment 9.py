""" 
Write a python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix
"""
def MxOrigin():
    R = int(input("Enter no. of rows: "))
    C = int(input("Enter no. of columns: "))
    M =[]
    for i in range(R):
        L=[]
        for j in range(C):
            L.append(int(input("Enter element: ")))
        M.append(L)
    return M

#Addition of two matrices
def MxAdd(M1, M2):
    M3 = M1
    if len(M1) == len(M2) and len(M1[0]) == len(M2[0]):
        for i in range(len(M1)):
            for j in range(len(M1[0])):
                M3[i][j] = M1[i][j] + M2[i][j]
    return M3

#Subtraction of two matrices
def MxSub(M1, M2):
    M3 = M1
    if len(M1) == len(M2) and len(M1[0]) == len(M2[0]):
        for i in range(len(M1)):
            for j in range(len(M1[0])):
                M3[i][j] = M1[i][j] - M2[i][j]
    return M3

#Transpose of a matrices
def MxTrans(M):
    Mt = M
    if len(M1) == len(M2) and len(M1[0]) == len(M2[0]):
        for i in range(len(M1)):
            for j in range(len(M1[0])):
                Mt[i][j] = M[i][j]
    return Mt

#Main program
print("Enter elements of matrix left to right row-wise")
print("First Matrix: ")
M1 = MxOrigin()
print("Second Matrix: ")
M2 = MxOrigin()
Msum = MxAdd(M1,M2)
Mdiff = MxSub(M1,M2)
Mtrans1 = MxTrans(M1)
Mtrans2 = MxTrans(M2)
print(M1)
print(M2)
print(Msum)
print(Mdiff)
print(Mtrans1)
print(Mtrans2)