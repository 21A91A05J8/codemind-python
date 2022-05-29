n=int(input())
t=n
sum=0
for i in range(1,n,1):
    r=n%i
    if r==0:
        sum=sum+i
if sum==t:
    print("True")
else:
    print("False")
        