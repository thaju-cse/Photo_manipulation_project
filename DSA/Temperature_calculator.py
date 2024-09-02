# Defining the temperature scales
TEMPERATURE_SCALES = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K'
}

# Definition the conversion function
def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value

# Creating the main program

while True:
    # Prompting the user for input
    input_value = input("Enter the temperature value: ")
    # Converting the input value to a float to get accurate result
    try:
        input_value = float(input_value)
    except ValueError:
        print("Invalid input value. Please enter a number.")
        print()
        continue

    input_scale = input("Enter the input temperature scale (C, F, or K): ").upper()
    #Checking the input unit
    if input_scale not in TEMPERATURE_SCALES.values():
        print("Invalid temperature scale. Please enter C, F, or K.")
        print()
        continue


    # Getting the answers according to the input value
    i=['F','C','K']
    i.remove(input_scale)
    for output_scale in i:

        # Convert the temperature and print the result

        output_value = convert_temperature(input_value, input_scale, output_scale)
        print(f"{input_value} {input_scale} = {output_value} {output_scale}")

    # Check if the user wants to quit
    print('If you wants to stop enter "Q" or "Quit" else press enter.')
    exit=0
    try:
        exit=input()

        if exit.lower() in ('q', 'quit'):
            break
    except:
        print()
        print("Now get ready with values. ")
print("Enjoy the day -> :)")