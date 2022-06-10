n=int(input())
t=n
dc=0
c=0
mc=0
while t!=0:
    r=t%10
    dc+=1
    t=t//10
for i in range(1,n+1,1):
    r=n%i
    if r==0:
        c+=1
if c==2:
    while n!=0:
        c=0
        r=n%10
        for i in range(1,r+1,1):
            if r%i==0:
                c+=1
        if c==2:
            mc+=1
        n=n//10
    if mc==dc:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
                
else:
    print("Not Mega Prime")