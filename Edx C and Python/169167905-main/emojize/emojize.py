import emoji

def main():
    user_input = input("Input: ")
    emojized_str = emoji.emojize(user_input, language='alias')
    print(f"Output: {emojized_str}")

if __name__ == "__main__":
    main()
