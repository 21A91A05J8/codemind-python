a,b=map(int,input().split())
if a>b:
    min=b
else:
    min=a
for k in range(min,0,-1):
    if a%k==0 and b%k==0:
        hcf=k
        break
print(hcf)