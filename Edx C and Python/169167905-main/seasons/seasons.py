from datetime import date, datetime
import sys
import inflect

def main():
    birthdate = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format")

    minutes = calculate_minutes(birthdate)
    print(f"{minutes_to_words(minutes)} minutes")
def calculate_minutes(birthdate):
    today = date.today()
    difference = today - birthdate
    return difference.days * 24 * 60

def minutes_to_words(minutes):
    p = inflect.engine()
    temp1 = p.number_to_words(minutes).replace(" and", "").replace(",", "").replace('thousand','thousand,').replace('million','million,')
    temp2 = temp1[0].upper()+temp1[1:]
    return temp2
if __name__ == "__main__":
    main()
