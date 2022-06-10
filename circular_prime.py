n=int(input())
c=0
rev=0
for i in range(1,n+1,1):
    r=n%i
    if r==0:
        c+=1
if c==2:
    t=n
    c=0
    while t!=0:
        r=t%10
        rev=rev*10+r
        t=t//10
    for i in range(1,rev+1,1):
        r=rev%i
        if r==0:
            c+=1
    if c==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    
        