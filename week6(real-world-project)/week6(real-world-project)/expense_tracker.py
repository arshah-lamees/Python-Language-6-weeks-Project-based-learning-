import pandas as pd
from datetime import datetime
import csv


# Create DataFrame to store expenses
expenses_df = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

# Save expenses to a CSV file
def save_expenses():
    global expenses_df
    # Write the entire DataFrame back to the CSV file, replacing its contents
    expenses_df.to_csv('expenses_sample.csv', index=False)
    print("Expenses saved successfully!")

# Load expenses from a CSV file
def load_expenses():
    global expenses_df
    try:
        # Load the CSV into the DataFrame
        expenses_df = pd.read_csv('expenses_sample.csv')
        # Convert 'Date' column to datetime for proper handling
        expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])
    except FileNotFoundError:
        print("No existing expense data found. Starting fresh.")

# Add a new expense or modify an existing one
def add_expense():
    load_expenses()
    
    while True:
       
        try:
            date = input("Enter date (YYYY-MM-DD): ")
            input_date = pd.to_datetime(date)
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Enter category: ")
    description = input("Enter description: ")

    global expenses_df

    # Check if an identical expense already exists
    existing_expense = expenses_df[
        (expenses_df['Date'] == input_date) &
        (expenses_df['Category'] == category) &
        (expenses_df['Description'] == description)
    ]

    if not existing_expense.empty:
        # If an identical expense exists, ask user what to do
        print("An expense with the same date, category, and description already exists:")
        print(existing_expense)

        while True:
            choice = input("Do you want to (1) Modify the amount, (2) Overwrite the expense, or (3) Cancel? Enter 1, 2, or 3: ")
            if choice == '1':
                # Modify the amount of the existing expense by adding to it
                index = existing_expense.index[0]
                expenses_df.at[index, 'Amount'] += amount
                print(f"Amount updated. New total: {expenses_df.at[index, 'Amount']}")
                break
            elif choice == '2':
                # Overwrite the existing expense with new details
                index = existing_expense.index[0]
                expenses_df.at[index, 'Amount'] = amount
                expenses_df.at[index, 'Date'] = input_date
                expenses_df.at[index, 'Category'] = category
                expenses_df.at[index, 'Description'] = description
                print("Expense overwritten successfully.")
                break
            elif choice == '3':
                # Cancel the operation without making any changes
                print("Operation canceled. No changes made.")
                return
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        # If no identical expense exists, add it as a new expense at the end of the DataFrame
        new_expense = pd.DataFrame({
            'Date': [input_date],
            'Amount': [amount],
            'Category': [category],
            'Description': [description]
        })
        expenses_df = pd.concat([expenses_df, new_expense], ignore_index=True)
        print("New expense added successfully.")

    # Save changes to CSV file (overwrite or add new data)
    save_expenses()

# Edit an existing expense in place without adding a new entity
def edit_expense():
    load_expenses()
    
    view_expenses()
    
    try:
        index = int(input("Enter the index of the expense to edit: "))
        
        if 0 <= index < len(expenses_df):
            print("Current expense details:")
            print(expenses_df.iloc[index])
            
            date = input("Enter new date (YYYY-MM-DD) or press enter to keep current: ")
            amount = input("Enter new amount or press enter to keep current: ")
            category = input("Enter new category or press enter to keep current: ")
            description = input("Enter new description or press enter to keep current: ")
            
            if date:
                expenses_df.at[index, 'Date'] = pd.to_datetime(date)
            if amount:
                expenses_df.at[index, 'Amount'] = float(amount)
            if category:
                expenses_df.at[index, 'Category'] = category
            if description:
                expenses_df.at[index, 'Description'] = description
            
            save_expenses()
            print("Expense updated successfully!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input! Please enter a valid index.")

# View all expenses in the CSV file with their indices for reference
def view_expenses():
    load_expenses()
    
    if len(expenses_df) == 0:
        print("No expenses recorded yet.")
    else:
        print(expenses_df.to_string(index=True))

# Calculate monthly totals for all recorded expenses
def calculate_monthly_totals():
    load_expenses()
    
    monthly_totals = expenses_df.groupby(expenses_df['Date'].dt.to_period('M'))['Amount'].sum()
    
    print("\nMonthly Totals:")
    for period, total in monthly_totals.items():
        print(f"{period}: {total}")

# Main function to run the program menu loop
def main():
    load_expenses()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. View Expenses")
        print("4. Calculate Monthly Totals")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            edit_expense()
        elif choice == '3':
            view_expenses()
        elif choice == '4':
            calculate_monthly_totals()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()