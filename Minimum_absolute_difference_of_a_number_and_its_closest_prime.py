import math
n=int(input())
t=n
c=0
for i in range(1,n+1,1):
    r=n%i
    if r==0:
        c+=1
if c==2:
    print("0")
else:
    for i in range(n-1,0,-1):
        c=0
        for j in range(1,i+1,1):
            r=i%j
            if r==0:
                c+=1
        if c==2:
            min=i
            break
    for k in range(n+1,2000,1):
        c=0
        for l in range(1,k+1,1):
            r=k%l
            if r==0:
                c+=1
        if c==2:
            max=k
            break
    d1=abs(n-min)
    d2=abs(n-max)
    if d1<d2:
        print(d1)
    elif d2<d1:
        print(d2)
    else:
        print(d1)
    
                

        
    