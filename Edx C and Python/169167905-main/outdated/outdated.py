def taking_input():
    inp=True
    while inp:
        date = input("Date: ")
        try:
            month,day,year = date.split("/")
            if month.isalpha():
                continue
            inp = False
        except:
            try:
                monday,year = date.split(",")
                month, day = monday.split(" ")
                if day.isnumeric():
                    inp = False
            except:
                pass
    return [day,month,year]
def print_year(year):
    print(year,end='-')
    return 0
def print_month(month):
    if int(month)>9:
        print(month,end='-')
    else:
        print("0"+month,end='-')
    return 0
def print_day(day):
    if int(day)>9:
        print(day)
    else:
        print("0"+day)
    return 0

def main():
    months = {
        "January":'1',
        "February":'2',
        "March":'3',
        "April":'4',
        "May":'5',
        "June":'6',
        "July":'7',
        "August":'8',
        "September":'9',
        "October":'10',
        "November":'11',
        "December":'12'
    }
    while True:
        day,month,year = taking_input()
        day= day.strip()
        month = month.strip()
        year = year.strip()
        try:
            if month.isalpha():
                month = months[month]
        except:
            continue
        if int(day)>31 or int(month)>12:
            continue
        break
    print_year(year)
    print_month(month)
    print_day(day)



main()

