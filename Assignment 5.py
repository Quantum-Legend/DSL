"""
Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string
"""

def listing(str):
    Ls=[]
    Ll = []
    D = {}
    word = ""
    cnt = 0
    for i in str:
        if i != " ":
            word += i
            cnt +=1
        else:
            Ls.append(word)
            Ll.append(cnt)
            word =""
            cnt = 0
    Ls.append(word)
    Ll.append(cnt)
    D = {Ls[m]: Ll[m] for m in range(len(Ls))}
    return D

def longest(D):
    v= list(D.values())
    k= list(D.keys())
    return k[v.index(max(v))], max(v)

def frequency(txt, chr):
    counter = 0
    for s in txt:
        if s != chr:
            continue
        counter += 1
    return counter

S = "This is string"
print("word with the longest length:", longest(listing(S))[0], longest(listing(S))[1], frequency(S, 'a'))
