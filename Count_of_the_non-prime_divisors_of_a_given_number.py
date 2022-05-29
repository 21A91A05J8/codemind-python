n=int(input())
c=0
for i in range(1,n+1,1):
    r=n%i
    if r==0:
        f=0
        for j in range(1,i+1,1):
            r=i%j
            if r==0:
                f=f+1
        if f==1 or f>2:
            c=c+1
print(c)