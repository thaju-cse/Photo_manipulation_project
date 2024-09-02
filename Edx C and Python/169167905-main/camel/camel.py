camel = input("camelCase: ")
temp = ""
for i in camel:
    if i.islower():
        temp+=i
    elif i.isupper():
        temp+="_"
        temp+=i.lower()
print("snake_case:",temp)
