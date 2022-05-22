import math
x,y,m=map(int,input().split())
s=math.pow(x,y)
n=int(s%m)
print(n)
