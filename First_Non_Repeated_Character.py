n=int(input())
for j in range(n):
    x=int(input())
    s=input()
    for i in s:
        if s.count(i)==1:
            print(i)
            break
    else:
        print("-1")