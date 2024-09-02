# int main():
#     rates = {
#         "Baja Taco": 4.25,
#         "Burrito": 7.50,
#         "Bowl": 8.50,
#         "Nachos": 11.00,
#         "Quesadilla": 8.50,
#         "Super Burrito": 8.50,
#         "Super Quesadilla": 9.50,
#         "Taco": 3.00,
#         "Tortilla Salad": 8.00
#         }
#     item = 'a'
#     total = 0
#     while (item != ''):
#         item = input("Item: ")
#         try:
#             total+=rates[item]
#             print("Total: $"+str("{:.2f}".format(total) ))
#         except:
#             pass
#     return 0
# main()
def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
        try:
            item = input("Item: ").strip().title()
            if item in menu:
                total_cost += menu[item]
                print(f"Total: ${total_cost:.2f}")
        except EOFError:
            print()  # Print a newline when control-d is pressed
            break

if __name__ == "__main__":
    main()
