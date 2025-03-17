# import requests
# import pandas as pd

# # Your API Key
# API_KEY = "1f180e0c7cb62ff9f166d058"

# # API Base URL
# BASE_URL = "https://v6.exchangerate-api.com/v6/"

# def get_exchange_rate(from_currency, to_currency):
#     """
#     Fetch the exchange rate from ExchangeRate-API.
#     """
#     url = f"{BASE_URL}{API_KEY}/latest/{from_currency}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         if to_currency in data['conversion_rates']:
#             return data['conversion_rates'][to_currency]
#         else:
#             print(f"Error: Currency {to_currency} not found in exchange rates.")
#             return None
#     else:
#         print(f"API Error: {response.status_code}, {response.text}")
#         return None

# def convert_currency(amount, from_currency, to_currency):
#     """
#     Convert an amount from one currency to another.
#     """
#     rate = get_exchange_rate(from_currency, to_currency)
#     if rate:
#         converted_amount = round(amount * rate, 2)
#         return converted_amount
#     else:
#         return None

# def convert_expenses_to_base(base_currency="USD"):
#     """
#     Convert all expenses in expenses_sample.csv to a base currency.
#     If the 'Currency' column is missing, assume all amounts are in USD.
#     """
#     try:
#         df = pd.read_csv('expenses_sample.csv')

#         # If there's no "Currency" column, assume all expenses are in USD
#         if 'Currency' not in df.columns:
#             print("Warning: No 'Currency' column found. Assuming all expenses are in USD.")
#             df['Currency'] = "USD"

#         # Convert each expense
#         converted_amounts = []
#         for _, row in df.iterrows():
#             amount = row['Amount']
#             from_currency = row['Currency']

#             # Convert to base currency if different
#             if from_currency != base_currency:
#                 converted = convert_currency(amount, from_currency, base_currency)
#                 converted_amounts.append(converted if converted else amount)  # Keep original if conversion fails
#             else:
#                 converted_amounts.append(amount)  # No conversion needed

#         df['Converted_Amount'] = converted_amounts
#         df['Base_Currency'] = base_currency

#         # Save updated CSV file
#         df.to_csv('converted_expenses.csv', index=False)
#         print(f"All expenses converted to {base_currency} and saved in converted_expenses.csv")

#     except FileNotFoundError:
#         print("Error: expenses_sample.csv not found.")
#     except Exception as e:
#         print(f"Unexpected Error: {e}")

# # Menu to choose conversion type
# def main():
#     print("\nCurrency Converter")
#     print("1. Convert a single amount")
#     print("2. Convert all expenses in CSV to base currency")
#     choice = input("Enter choice (1/2): ")

#     if choice == "1":
#         amount = float(input("Enter amount: "))
#         from_currency = input("Enter from currency (e.g., USD): ").upper()
#         to_currency = input("Enter to currency (e.g., EUR): ").upper()
#         converted = convert_currency(amount, from_currency, to_currency)
#         print(f"{amount} {from_currency} = {converted} {to_currency}" if converted else "Conversion failed.")
    
#     elif choice == "2":
#         base_currency = input("Enter base currency (default is USD): ").upper() or "USD"
#         convert_expenses_to_base(base_currency)

# if __name__ == "__main__":
#     main()

import requests
import pandas as pd

# Your API Key
API_KEY = "1f180e0c7cb62ff9f166d058"
BASE_URL = "https://v6.exchangerate-api.com/v6/"

def get_exchange_rate(from_currency, to_currency):
    url = f"{BASE_URL}{API_KEY}/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if to_currency in data['conversion_rates']:
            return data['conversion_rates'][to_currency]
        else:
            print(f"Error: Currency {to_currency} not found in exchange rates.")
            return None
    else:
        print(f"API Error: {response.status_code}, {response.text}")
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        return round(amount * rate, 2)
    return None

def convert_expenses_to_base(input_file='expenses_sample.csv', output_file='converted_expenses.csv', base_currency="USD"):
    try:
        df = pd.read_csv(input_file)

        if 'Currency' not in df.columns:
            print("Warning: No 'Currency' column found. Assuming all expenses are in USD.")
            df['Currency'] = "USD"

        converted_amounts = []
        for _, row in df.iterrows():
            amount = row['Amount']
            from_currency = row['Currency']

            if from_currency != base_currency:
                converted = convert_currency(amount, from_currency, base_currency)
                converted_amounts.append(converted if converted else amount)
            else:
                converted_amounts.append(amount)

        df['Converted_Amount'] = converted_amounts
        df['Base_Currency'] = base_currency
        df.to_csv(output_file, index=False)
        print(f"Expenses converted to {base_currency} and saved in {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    print("\nCurrency Converter")
    print("1. Convert a single amount")
    print("2. Convert all expenses in CSV to base currency")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        from_currency = input("Enter from currency (e.g., USD): ").upper()
        to_currency = input("Enter to currency (e.g., EUR): ").upper()
        converted = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted} {to_currency}" if converted else "Conversion failed.")
    
    elif choice == "2":
        base_currency = input("Enter base currency (default is USD): ").upper() or "USD"
        convert_expenses_to_base(base_currency=base_currency)
