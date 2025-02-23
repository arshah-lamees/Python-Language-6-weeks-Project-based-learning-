import csv

def analyze_expenses(file_path="expenses_sample.csv"):
    """Reads CSV file, prints the data, calculates the total expenses and ask user to add a new expense."""
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader) # Skip header row
            print("Header:", header)

            total_expenses = 0
            print("\nData:")
            expenses=[] #stire expenses for later writing
            for row in csv_reader:
                print(row)  # Print each row
                expenses.append(row)
                try:
                  total_expenses += float(row[2]) #row[2]=amount, float(row[2])->type casting
                except ValueError:
                  print(f"Warning: Skipping row due to invalid amount: {row}")
            print(f"\nTotal Expenses: {total_expenses}")

        # ask the user to add a new expense
        add_new = input("Do you want to add a new expense? (y/n): ")
        if add_new.lower() == "y":
            new_date = input("Enter the date (MM/DD/YYYY): ")
            new_category = input("Enter the category: ")
            new_amount = (input("Enter the amount: ")) # Changed to a float to match other amounts
            new_description = input("Enter the description: ")

            new_expense = [new_date, new_category, new_amount, new_description]
            expenses.append(new_expense)  # Add the new expense to the list

            write_expenses(file_path, header, expenses) #Calling the write function

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_expenses(file_path, header, expenses):
    """Writes the expenses data to a CSV file."""
    try:
        with open(file_path, 'w', newline='') as file:  # Open in write mode ('w')
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)  # Write the header row
            csv_writer.writerows(expenses)  # Write all the expense rows
        print(f"\n----Successfully wrote the expenses to '{file_path}'.-----")
        analyze_expenses(file_path)

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

analyze_expenses()
