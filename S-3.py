n=int(input())
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
print(a[350-1])

