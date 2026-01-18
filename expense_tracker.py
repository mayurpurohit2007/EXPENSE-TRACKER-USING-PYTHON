import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\nDate | Category | Description | Amount")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | ₹{row[3]}")
    except FileNotFoundError:
        print("No expenses found.")

def expense_summary():
    summary = {}
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[3])
                total += amount

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\nCategory-wise Summary:")
        for category, amount in summary.items():
            print(f"{category}: ₹{amount}")

        print(f"\nTotal Expense: ₹{total}")

    except FileNotFoundError:
        print("No expenses found.")

def menu():
    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Try again.")

menu()
