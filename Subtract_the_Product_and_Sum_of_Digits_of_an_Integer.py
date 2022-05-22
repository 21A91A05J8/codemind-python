n=int(input())
temp=n
p=1
s=0
while n!=0:
    r=n%10
    p=p*r
    s=s+r
    n=n//10
dif=p-s
print(dif)