s=input()
t='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'
r=''
for i in range(len(s)):
    if(s[i]!=' '):
        t+=s[i]
    if(s[i]==' ' or i==len(s)-1):
        r+=''.join(reversed(t))
        if(i!=len(s)-1):
            r+=' '
        t='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'
print(r)
        