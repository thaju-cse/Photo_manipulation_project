import sys
import csv

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

elif len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

elif (sys.argv[1][-4:] != ".csv") or (sys.argv[2][-4:] != ".csv") :
    print("Invalid extension")
    sys.exit(1)

try:
    with open(sys.argv[1], 'r') as before:
        reader = csv.DictReader(before)
        # if reader.fieldnames != ['name', 'house']:
        #     sys.exit(f"Invalid columns in {input_file}")

        with open(sys.argv[2], 'w') as after:
            writer = csv.DictWriter(after, fieldnames=['first', 'last', 'house'])
            writer.writeheader()

            for row in reader:
                last, first = row['name'].split(', ')
                writer.writerow({'first': first, 'last': last, 'house': row['house']})

except FileNotFoundError:
    print("File does not exist 2")
    sys.exit(1)

