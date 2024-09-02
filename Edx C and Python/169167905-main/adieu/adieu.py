def main():
    import sys
    import inflect

    # Initialize the inflect engine
    p = inflect.engine()

    # List to store names
    names = []

    # Prompt the user for names until EOF (control-d)
    print("Enter names (press ctrl-d when done):")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    # Construct the farewell message
    farewell_message = "Adieu, adieu, to " + p.join(names)

    # Print the farewell message
    print(farewell_message)


if __name__ == "__main__":
    main()
