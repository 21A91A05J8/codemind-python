n=int(input())
sum=0
while n!=0:
    while n!=0:
        r=n%10
        sum=sum+r
        n=n//10
    if sum<10:
        print(sum)
        break
    else:
        n=sum
        sum=0