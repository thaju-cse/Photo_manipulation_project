import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define a regular expression for a valid IPv4 address
    pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
    if not pattern.match(ip):
        return False

    # Split the IP address into its components
    parts = ip.split(".")

    # Check each part to ensure it is within the range 0-255
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()

