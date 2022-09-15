"""
Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string
"""
while True:
    print("-"*50)
    print("\nSTRING OPERATIONS")
    print("1. To display word with the longest length")
    print("2. To determines the frequency of occurrence of particular character in the string")
    print("3. To check whether given string is palindrome or not")
    print("4. To display index of first appearance of the substring")
    print("5. To count the occurrences of each word in a given string")
    print("6. Exit")
    
    menu = int(input("\nChoose which operation you would like to perform: "))

    if menu == 1:
        def str_list(str):
            L=[]
            LI=[]
            D={}
            word=""
            cnt=0
            for i in str:
                if i != " " :
                    word += i
                    cnt+=1
                else :
                    L.append(word)
                    LI.append(cnt)
                    word=""
                    cnt=0
            L.append(word)
            LI.append(cnt)
            D={L[m]:LI[m] for m in range(len(L))}
            return D

        def longest(D):
            v= list(D.values())
            k= list(D.keys())
            return k[v.index(max(v))],max(v)
        
        s = input("Enter your desired string: ")
        print("The longest word in the string is =",longest(str_list(s))[0],"whose length is" ,longest(str_list(s))[1])

    elif menu == 2:
        def freq(word,char):
            cnt=0
            for i in word :
                if i== char :
                    cnt+=1
            return cnt 
        b=input("Enter your word :")
        c=input("Enter your letter :")
        print("The frequency of given character in the string is = ", freq(b,c))

    elif menu == 3:
        def pal(a):
            n=len(a)
            j=0
            b=""
            for i in a:
                b+=a[n-1]
                j+=1
                n-=1
            if a == b:
                print("entered word is palindrome")
            else :
                print(" entered word is not a palindrome")
        x=input("Enter your word :")
        pal(x)    
        
    elif menu == 4:
        def firap(word,char):
            cnt=0
            for i in word :
                if i== char :
                    print(cnt) 
                    break
                cnt+=1        
        w=input("Enter your word :")
        h=input("Enter the substring:")
        print("The first appearance of this substring in the given string is at index = ")
        firap(w,h)
        
    elif menu == 5:
        def occur(str2):
            dict={}
            Lw=[]
            word = ""
            for i in str2:
                if i != " " :
                    word += i
                else :
                    Lw.append(word)
                    word=""
            Lw.append(word)
            for i in Lw:
                cnt = 0
                for j in Lw:
                    if i==j:
                        cnt += 1
                dict.update({i:cnt})
            return dict
        s2 = input("Enter the desired string : ")
        print("The occurences of each word in the given string are : ", occur(s2))
    
    elif menu == 6:
        break
    
    else:
        print("ENTER A VALID INPUT.")
