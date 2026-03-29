import csv
from datetime import datetime
import statistics

FILE_NAME = "expenses.csv"

# Initialize CSV file
def init_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    except FileExistsError:
        pass

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    category = categorize(description)

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully.")

# View expenses
def view_expenses():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Simple AI categorization
def categorize(description):
    description = description.lower()
    if "food" in description or "restaurant" in description:
        return "Food"
    elif "uber" in description or "bus" in description:
        return "Transport"
    elif "movie" in description or "netflix" in description:
        return "Entertainment"
    else:
        return "Other"

# Analyze expenses
def analyze_expenses():
    amounts = []
    categories = {}

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row["Amount"])
            amounts.append(amt)

            cat = row["Category"]
            categories[cat] = categories.get(cat, 0) + amt

    if not amounts:
        print("No data available.")
        return

    print("Total Spending:", sum(amounts))
    print("Average Spending:", statistics.mean(amounts))

    print("Category-wise Spending:")
    for k, v in categories.items():
        print(k, ":", v)

# Predict spending
def predict_spending():
    amounts = []

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amounts.append(float(row["Amount"]))

    if len(amounts) < 2:
        print("Not enough data for prediction.")
        return

    avg = statistics.mean(amounts)
    print("Predicted next expense (approx):", round(avg, 2))

# Menu
def menu():
    init_file()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Predict Spending")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            analyze_expenses()
        elif choice == '4':
            predict_spending()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
