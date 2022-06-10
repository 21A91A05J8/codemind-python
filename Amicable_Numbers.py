m=int(input())
n=int(input())
c=0
sum=0
for i in range(1,m,1):
    r=m%i
    if r==0:
        sum=sum+i
if sum==n:
    c+=1
sum=0
for i in range(1,n,1):
    r=n%i
    if r==0:
        sum=sum+i
if sum==m:
    c+=1
if c==2:
    print("Amicable")
else:
    print("Not Amicable")
        
    
        