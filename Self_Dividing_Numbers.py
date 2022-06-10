m=int(input())
n=int(input())
dc=0
c=0
for i in range(m,n+1,1):
    t=i
    dc=0
    c=0
    while t!=0:
        r=t%10
        dc=dc+1
        t=t//10
    t=i
    while t!=0:
        r=t%10
        if r==0:
            t=t//10
            continue
        re=i%r
        if re==0:
            c=c+1
        t=t//10
    if c==dc:
        print(i,end=" ")
        
            
        