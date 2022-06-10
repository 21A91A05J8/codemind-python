n=int(input())
t=n
dc=0
rev=0
mr=0
while t!=0:
    r=t%10
    dc+=1
    t=t//10
t=n
sq=n*n
while dc!=0:
    r=sq%10
    rev=rev*10+r
    sq=sq//10
    dc-=1
while rev!=0:
    r=rev%10
    mr=mr*10+r
    rev=rev//10
if n==mr:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
    
