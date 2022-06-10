n=int(input())
c=0
while n>0:
    n=n//10
    c+=1
if c==10:
    print("Valid")
elif (n//1000000000!=0):
    print("Valid")
else:
    print("Invalid")
