import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        print(e)

def convert(s):
    pattern = r'^(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)$'
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid input format")

    start_time, start_period, end_time, end_period = match.group(1, 3, 4, 6)

    start_24hr = convert_to_24hr(start_time, start_period)
    end_24hr = convert_to_24hr(end_time, end_period)

    return f"{start_24hr} to {end_24hr}"

def convert_to_24hr(time, period):
    if ':' in time:
        hours, minutes = map(int, time.split(':'))
    else:
        hours = int(time)
        minutes = 0
    if hours < 1 or hours > 12 or minutes < 0 or minutes >= 60:
        raise ValueError("Invalid time")

    if period == "AM":
        if hours == 12:
            hours = 0
    elif period == "PM":
        if hours != 12:
            hours += 12

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
