one, operand, two = input("Expression: ").split(" ")
one = float(one)
two = float(two)
if (operand == "+"):
    print(one+two)
elif (operand == "-"):
    print(one-two)
elif (operand == "*"):
    print(one*two)
elif (operand == "/"):
    print(one/two)
