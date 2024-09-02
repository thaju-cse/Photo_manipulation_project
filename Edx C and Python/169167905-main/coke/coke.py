amount = 50
insert = 0
while (amount > 0):
    print("Amount Due:", amount)
    insert = int(input("Insert Coin: "))
    if (insert == 25 or insert ==10 or insert == 5):
        amount = amount-insert
print("Change Owed:",amount*(-1))
