import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif sys.argv[1][-4:] !=".csv":
    print("Not a CSV file")
    sys.exit(1)


try:
    with open(sys.argv[1]) as file:
        flag = True
        rows = []
        for line in file:
            if flag:
                header = list(map(str, line.split(",")))
                header [-1] = header[-1].replace("\n", "")
                flag = False
                continue
            rows.append(list(map(str, line.strip().split(","))))
        # print(rows)
        # print(headers)
        print(tabulate(rows, header, tablefmt = 'grid'))


        # print(file,headers, tablefmt = 'grid')
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
