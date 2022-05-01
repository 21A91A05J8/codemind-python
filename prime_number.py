n=int(input())
fc=0
for i in range(1,n+1,1):
    r=n%i
    if r==0:
        fc=fc+1
if fc==2:
    print("prime")
else:
    print("not a prime")