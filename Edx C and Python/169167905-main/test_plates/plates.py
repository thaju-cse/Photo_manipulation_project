def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not has_valid_length(s):
        return False
    if not starts_with_two_letters(s):
        return False
    if not valid_numbers_position(s):
        return False
    if not has_only_allowed_characters(s):
        return False
    return True


def has_valid_length(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return s[:2].isalpha()


def valid_numbers_position(s):
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if i == 0 or i == 1:  # the first or second character is a digit
                return False
            if s[i] == '0' and (i == 2 or s[i-1].isalpha()):  # first number is '0'
                return False
            number_started = True
        elif number_started:  # found a letter after number started
            return False
    return True


def has_only_allowed_characters(s):
    return s.isalnum()  # checks if all characters are either letters or numbers

if __name__ == '__main__':
    main()


