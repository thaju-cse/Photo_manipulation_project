def main():
    temp = input("Greeting: ")
    print("$",end='')
    print(value(temp))


def value(temp):
    temp = temp.strip()
    temp = temp.lower()
    if len(temp)==0:
        return 100
    if (temp[0:5] == "hello"):
        return 0
    elif (temp[0] == 'h'):
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
