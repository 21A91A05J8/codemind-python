n=int(input())
temp=n;
e=0
o=0
dc=0
while n!=0:
    r=n%10
    dc=dc+1
    n=n//10
n=temp
while n!=0:
    r=n%10
    if r%2==0:
        e=e+1
    else:
        o=o+1
    n=n//10
if dc==e:
    print("Even")
elif dc==o:
    print("Odd")
else:
    print("Mixed")
        