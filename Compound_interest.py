import math
p,r,t=map(int,input().split())
ci=(p)*(math.pow(1+(r/100),t))
ci="{:.2f}".format(ci)
print(ci)