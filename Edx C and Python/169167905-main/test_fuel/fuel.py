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

