# # def main():
# #     plate = input("Plate: ")
# #     if is_valid(plate):
# #         print("Valid")
# #     else:
# #         print("Invalid")

# # def is_valid(s):
# #     string_count=0
# #     l1=l2=len(s)
# #     num_start = l1
# #     if (l1>6):
# #         return False
# #     for i in s[::-1]:
# #         l1-=1
# #         if i.isalpha():
# #             string_count+=1
# #         if not (i.isalpha() or i.isnumeric()):
# #             return False
# #         if (i.isnumeric()):
# #             num_start = l1
# #     if s[num_start:].isalpha():
# #         return False
# #     if string_count<2:
# #         return False
# #     return True


# # if __name__ == '__main__':
# #     main()

# def main():
#     plate = input("Enter your vanity plate: ")
#     if is_valid(plate):
#         print("Valid ")
#     else:
#         print("Invalid ")

# def is_valid(s):
#     # Rule 1: Must start with at least two letters
#     if not s[:2].isalpha():
#         return False

#     # Rule 2: Can contain a maximum of 6 characters and a minimum of 2 characters
#     if not 2 <= len(s) <= 6:
#         return False

#     # Rule 3: Digits, if any, must be at the end
#     if not s[-1].isdigit():
#         return False

#     # Rule 4: The first digit used cannot be '0'
#     if s[2].isdigit() and s[2] == '0':
#         return False

#     # Rule 5: No periods, spaces, or punctuation marks are allowed
#     if not s.isalnum():
#         return False

#     return True

# if __name__ == "__main__":
#     main()


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
