n=int(input())
for i in range(1,n//2,1):
    sq=i*i
    if sq==n:
        print("True")
        break
else:
    print("False")