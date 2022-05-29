n=int(input())
sum=0
while n!=0:
    while n!=0:
        r=n%10
        sum=sum+r*r
        n=n//10
    if sum<10:
        if sum==1 or sum==7:
            print("True")
            break
        else:
            print("False")
            break
    else:
        n=sum
        sum=0
    
        