s='(()())((()))'
count=0
a=''
j=0
k=0
s1=''
for i in s:
    if i=='(':
        count+=1
    elif i==')':
        count-=1
    j+=1
    if count==0:
        s1=s1+s[k+1:j-1]
        k=j
print(s1)
