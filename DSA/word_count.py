def count_words():
    sentence = list(map(str,input().split()))
    words=0
    word_count={}
    for i in sentence:
        i=i.lower()
        words+=1
        cou=0
        for j in sentence:
            j=j.lower()
            if i in j:
                cou+=1
        if cou>1:
            word_count[i]=cou
    print(words)
    return word_count
print(count_words())