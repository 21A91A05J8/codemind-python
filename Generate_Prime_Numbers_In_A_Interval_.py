m=int(input())
n=int(input())
for i in range(m+1,n,1):
    f=0
    for j in range(1,i+1,1):
        r=i%j
        if r==0:
            f=f+1
    if f<3:
        print(i)