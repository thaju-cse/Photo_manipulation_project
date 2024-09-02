def borrow_number():
    number1=int(input())
    number2=int(input())
    count=0
    if(number1< number2):
        return -1
    else:
        flag=0
        while(number1!=0 and number2!=0):
            temp1=0
            temp2=number2%10
            if(flag):
                temp1=number1%10-1
            else:
                temp1=number1%10
            if(temp1< temp2):
                count+=1
                flag=1
            else:
                flag=0
            number1=number1//10
            number2=number2//10 
        return count
print(borrow_number())