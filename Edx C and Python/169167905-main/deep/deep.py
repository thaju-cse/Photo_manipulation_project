print("What is the Answer to the Great Question of Life, the Universe, and Everything? ",end="")
temp = input()
if (temp.strip() == "42" or temp.lower() == "forty-two" or temp.lower() == 'forty two'):
    print("Yes")
else:
    print("No")
