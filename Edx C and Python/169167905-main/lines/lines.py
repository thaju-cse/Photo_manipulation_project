import sys

#First condition
"""Second condition
"""
'''third condition
'''
"hello"


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)


elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)


elif sys.argv[1][-3:] !=".py":
    print("Not a Python file")
    sys.exit(1)

try:
    with open(sys.argv[1]) as file:
        count = 0
        for line in file:
            stripped_line = line.strip()

            if stripped_line and not stripped_line.startswith('#'):
                count +=1
            #print(line)
        print(count)

except FileNotFoundError:
    print("File does not exist")
