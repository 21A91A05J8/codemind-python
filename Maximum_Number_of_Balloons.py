s=input()
b='balloon'
x=0
y=1
while y:
    c=0
    for i in b:
        if i in s:
            s=s.replace(i,'',1)
            c+=1
        else:
            y=0
            break
    if c==len(b):
        x+=1
print(x)