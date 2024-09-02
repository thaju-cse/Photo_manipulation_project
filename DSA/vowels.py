def vowels():
    sentence=input()
    vowels=['a','e','i','o','u']
    sentence=sentence.lower()
    for i in vowels:
        if i in sentence:
            pass
        else:
            break
    else:
        return True
    return False
print(vowels())