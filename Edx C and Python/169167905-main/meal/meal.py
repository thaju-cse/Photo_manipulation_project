def main():
    time = input("What time is it? ")
    decimal = convert(time)
    if (decimal >= 7 and decimal <= 9):
        print("breakfast time")
    if (decimal >= 12 and decimal <= 13):
        print("lunch time")
    if (decimal >= 18 and decimal <= 19):
        print("dinner time")
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes/60
    return hours+minutes

if __name__ == "__main__":
    main()
