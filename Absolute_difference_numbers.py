import math
n,x=map(int,input().split())
t1=n
t2=x
lre=0
l=0
rev=0
f=0
while x!=0:
    r=n%10
    lre=lre*10+r
    x=x-1
    n=n//10
while lre!=0:
    r=lre%10
    l=l*10+r
    lre=lre//10
n=t1
x=t2
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
while x!=0:
    r=rev%10
    f=f*10+r
    rev=rev//10
    x=x-1
dif=f-l
dif=abs(dif)
print(dif)

    
    
    