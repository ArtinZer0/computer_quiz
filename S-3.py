n=int(input())
# n=8 or n=9
A=[]
a="xy"
for i in range(n):
    for i in range(len(a)):
        if a[i]=="x":
            A.append("xy")
        else:
            A.append("yx")
    a=""
    for i in A:
       a=a+i
    A=[]
print(a[::-1])
a=a[::-1]
#print(a[200-1]) or print(a[350-1])


