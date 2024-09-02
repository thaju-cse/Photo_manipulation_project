s1='paper'
s2='title'
d1={}
d2={}
j=0
for i in s1:
    if i not in d1:
        d1[i]=s2[j]
    else:
        if d1[i]!=s1[j]:
            t1=False
            break
        else:
            continue
else:
    t1=True
j=0
for i in s2:
    if i not in d2:
        d2[i]=s1[j]
    else:
        if d2[i]!=s2[j]:
            t2=False
            break
        else:
            continue
else:
    t2=True
if t1 and t2:
    print("morphic")
else:
    print('not morphic')