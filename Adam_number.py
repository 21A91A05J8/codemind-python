n=int(input())
sq=n*n
rev=0
mc=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
sq1=rev*rev
while sq1!=0:
    r=sq1%10
    mc=mc*10+r
    sq1=sq1//10
if mc==sq:
    print("True")
else:
    print("False")

    

    