def absolute_difference():
    elements=list(map(int,input().split()))
    elements=sorted(elements)
    min=100000
    num1=num2=0
    for i in range(len(elements)-1):
        temp=abs(elements[i]-elements[i+1])
        if min>temp:
            min=temp
            num1=elements[i]
            num2=elements[i+1]
    print(min)
    return [num1,num2]
print(absolute_difference())