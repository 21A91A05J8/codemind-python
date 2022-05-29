n=int(input())
t=n
sum=0
while n!=0:
    r=n%10
    f=1
    for i in range(1,r+1,1):
        f=f*i
    sum=sum+f
    n=n//10
if t==sum:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")
    
        
        