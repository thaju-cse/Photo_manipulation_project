def remove_space():
    sentence=input()
    out=''
    for i in sentence:
        if i==" ":
            continue
        out+=i
    return out
print(remove_space())