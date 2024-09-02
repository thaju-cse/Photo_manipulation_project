def string_count_reducer():
    s=input()
    i=1
    c=1
    while i<len(s):
        if s[i]==s[i-1]:
            c+=1
        else:
            print(s[i-1],end="")
            print(c,end="")
            c=1
        i+=1
    print(s[i-1],end="")
    print(c)
string_count_reducer()