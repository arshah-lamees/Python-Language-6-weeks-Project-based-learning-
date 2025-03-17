import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the static directory exists for saving images
os.makedirs("static", exist_ok=True)

def load_expenses():
    global expenses_df
    try:
        expenses_df = pd.read_csv('expenses_sample.csv')
        expenses_df['Date'] = pd.to_datetime(expenses_df['Date'])
    except FileNotFoundError:
        print("No existing expense data found. Starting fresh.")
        expenses_df = pd.DataFrame(columns=["Date", "Category", "Amount"])

def plot_expense_trends(expenses_df):
    if expenses_df.empty:
        print("No expenses recorded yet. Unable to generate trend visualization.")
        return
    
    monthly_expenses = expenses_df.groupby(expenses_df['Date'].dt.to_period('M'))['Amount'].sum()
    
    plt.figure(figsize=(8, 5))
    monthly_expenses.plot(kind='line', marker='o')
    plt.title('Monthly Expense Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Expenses')
    plt.grid(True)
    plt.tight_layout()
    
    plt.savefig('static/monthly_expense_trends.png')
    plt.close()
    print("Monthly expense trends saved as 'static/monthly_expense_trends.png'.")

def plot_category_expenses(expenses_df):
    if expenses_df.empty:
        print("No expenses recorded yet. Unable to generate category visualization.")
        return

    category_expenses = expenses_df.groupby('Category')['Amount'].sum()
    
    plt.figure(figsize=(8, 5))
    plt.pie(category_expenses, labels=category_expenses.index, autopct='%1.1f%%', startangle=90)
    plt.title('Expense Breakdown by Category')
    plt.axis('equal')  # Ensures pie chart is a circle
    plt.tight_layout()
    
    plt.savefig('static/category_expenses.png')
    plt.close()
    print("Category expense breakdown saved as 'static/category_expenses.png'.")

def generate_visualizations():
    load_expenses()
    plot_expense_trends(expenses_df)
    plot_category_expenses(expenses_df)

if __name__ == "__main__":
    generate_visualizations()
