import sys
import random
import pyfiglet

def main():
    # List of available fonts
    available_fonts = pyfiglet.FigletFont.getFonts()

    # Handle command-line arguments
    if len(sys.argv) == 1:
        # No font specified, choose a random font
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        font = sys.argv[2]
        if font not in available_fonts:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Prompt user for input
    user_input = input("Input: ")

    # Create FIGlet object with the specified or random font
    figlet = pyfiglet.Figlet(font=font)

    # Output the text in FIGlet font
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
