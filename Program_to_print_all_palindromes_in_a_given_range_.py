m=int(input())
n=int(input())
for i in range(m,n+1,1):
    temp=i
    rev=0
    while i!=0:
        r=i%10
        rev=rev*10+r
        i=i//10
    if temp==rev:
        print(rev,end=' ')
        