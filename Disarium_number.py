import math
n=int(input())
t=n
sum=0
dc=0
while t!=0:
    r=t%10
    dc+=1
    t=t//10
t=n
while dc!=0:
    r=n%10
    sum=sum+pow(r,dc)
    n=n//10
    dc-=1
if t==sum:
    print("True")
else:
    print("False")

    