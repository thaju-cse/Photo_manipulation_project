def main():
    sentence = input("Input: ")
    print(shorten(sentence))


def shorten(sentence):
    value = ''
    for i in sentence:
        _ = i.lower()
        if (_=='a' or _=='e' or _=='i' or _=='o' or _=='u'):
            continue
        value = value + i
    return value


if __name__ == '__main__':
    main()
