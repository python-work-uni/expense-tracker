import csv
from datetime import datetime

# Constants
CSV_FILE = 'expenses.csv'
FIELDS = ['Date', 'Category', 'Description', 'Amount']

# Function to initialize the CSV file
def initialize_csv():
    try:
        with open(CSV_FILE, mode='x', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
    except FileExistsError:
        pass  # File already exists

# Function to add an expense
def add_expense(category, description, amount):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({'Date': date, 'Category': category, 'Description': description, 'Amount': amount})

# Function to view all expenses
def view_expenses():
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Date']} | {row['Category']} | {row['Description']} | ${row['Amount']}")

# Function to get total expenses by category
def total_by_category():
    totals = {}
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount
    return totals

# Main function to run the expense tracker
def main():
    initialize_csv()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total by Category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(category, description, amount)
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            totals = total_by_category()
            for category, total in totals.items():
                print(f"{category}: ${total:.2f}")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()