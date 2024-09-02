# percentage = -1
# while (percentage == -1):
#     try:
#         a,b = input("Fraction: ").split("/")
#         if int(a)!=float(a) or int(b)!=float(b):
#             continue
#     except:
#         continue
#     a = int(a)
#     b = int(b)
#     if (a>b):
#         continue
#     try:
#         percentage = (a/b)*100
#         if (percentage >=0 and percentage<=1):
#             print("E")
#         elif (percentage >=99 and percentage<=100):
#             print("F")
#         else:
#             percentage = str(round(percentage))
#             print(percentage+"%",)
#     except:
#         pass

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        percentage = (x / y) * 100
        return round(percentage)
    except ValueError:
        raise ValueError("Invalid input.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be zero.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
