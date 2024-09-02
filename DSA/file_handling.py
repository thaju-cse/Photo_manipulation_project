myfile=open("Hello.pyc","r")
count=0
for l in myfile:
    print(l)
    for i in l.split(" "):
        print(i)
print(myfile)
myfile.close()
print(count)
