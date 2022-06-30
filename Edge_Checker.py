a,b=input().split()
a=int(a)
b=int(b)
f=0
if b==a+1:
    print("Yes")
    f=1
if b==a+9:
    print("Yes")
    f=1
if a==b+1:
    print("Yes")
    f=1
if a==b+9:
    print("Yes")
    f=1
if f==0:
    print("No")