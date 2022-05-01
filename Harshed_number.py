n=int(input())
sum=0
tem=n
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
d=tem%sum
if d==0:
    print("True")
else:
    print("False")