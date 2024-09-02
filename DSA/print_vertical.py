def print_vertical(s):
    split = s.split()
    result = []
    maxWordLength = max(len(word) for word in split)
    for indexInWord in range(maxWordLength):
        partialResult = []
        for word in split:
            if len(word) > indexInWord:
                partialResult.append(word[indexInWord])
            else:
                partialResult.append(" ")
        result.append(partialResult)
    output = []
    for partialResult in result:
        output.append(''.join(partialResult).rstrip())
    return output
s=input()
print(print_vertical(s))
