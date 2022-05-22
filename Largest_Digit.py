n=int(input())
m=0
while n!=0:
    r=n%10;
    if r>m:
        m=r
    n=n//10
print(m)
    