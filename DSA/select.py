l=list(map(int,input().split()))
for i in range(len(l)):
    ind=min(l[i:])
    ind1=l.index(ind)
    l[i],l[ind1]=l[ind1],l[i]
    
print(l)

                            
