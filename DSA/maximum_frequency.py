def maximum_frequecy():
    sentence=input()
    unique=[]
    sentence=sentence.lower()
    for i in sentence:
        if i.isalpha():
            unique.append(i)
    unique=list(set(unique))
    unique_dict={}
    counted=[]
    for i in unique:
        cou=sentence.count(i)
        counted.append(cou)
        unique_dict[cou]=i
    counted=sorted(counted)
    if counted[-1]==counted[-2]:
        return 0
    return unique_dict[counted[-1]]
print(maximum_frequecy())