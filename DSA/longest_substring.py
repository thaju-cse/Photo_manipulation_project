def longest_substring(s):
    len_sub=[]
    prev=""
    cnt=0
    i=0
    while i <len(s):
        j=i
        cnt=0
        while(j<len(s) and (s[j] not in prev)):
            prev=prev+s[j]
            cnt+=1
            j+=1
        prev=""
        i+=1
        len_sub.append(cnt)
    if(len_sub==[]):
        return 0
    return max(len_sub)
sentence=input()
print(longest_substring(sentence))