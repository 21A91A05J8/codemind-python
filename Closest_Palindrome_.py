import math
n=int(input())
for i in range(n-1,1,-1):
    t=i
    rev=0
    while t!=0:
        r=t%10
        rev=rev*10+r
        t=t//10
    if i==rev:
        min=rev
        break
for j in range(n+1,10000,1):
    t=j
    rev=0
    while t!=0:
        r=t%10
        rev=rev*10+r
        t=t//10
    if rev==j:
        max=rev
        break
d1=abs(n-min)
d2=abs(n-max)
if d1<d2:
    print(min)
elif d2<d1:
    print(max)
else:
    print(min,max)

        