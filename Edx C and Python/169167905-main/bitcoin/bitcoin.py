import sys
import requests

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Check if the argument can be converted to a float
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Fetch the current price of Bitcoin
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    # Calculate the total cost
    total_cost = num_bitcoins * price_per_bitcoin

    # Output the cost with thousands separator and four decimal places
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
