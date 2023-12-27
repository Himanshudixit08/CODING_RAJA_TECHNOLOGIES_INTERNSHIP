import json
import os

total_income = 0
total_expenses = 0
expenses = {}


# add an expense
def add_expense(category, amount):
  global total_expenses
  total_expenses += amount
  expenses[category] = expenses.get(category, 0) + amount


# add income
def add_income(amount):
  global total_income
  total_income += amount


# calculate remaining budget
def calculate_budget():
  remaining_budget = total_income - total_expenses
  return remaining_budget


# analyze and display spending trends
def analyze_expenses():
  print("\nExpense Analysis:")
  for category, amount in expenses.items():
    print(f"{category.capitalize()}: ₹{amount:.2f}")


# Function to save transactions to a file
def save_data():
  data = {
      'total_income': total_income,
      'total_expenses': total_expenses,
      'expenses': expenses
  }

  with open('budget_data.json', 'w') as file:
    json.dump(data, file)


# load transactions from a file
def load_data():
  global total_income, total_expenses, expenses

  try:
    with open('budget_data.json', 'r') as file:
      data = json.load(file)
      total_income = data.get('total_income', 0)
      total_expenses = data.get('total_expenses', 0)
      expenses = data.get('expenses', {})
  except FileNotFoundError:
    pass


while True:
  print("\nBudget Tracker Menu ")
  print("1. Add Expense")
  print("2. Add Income")
  print("3. Calculate Remaining Budget")
  print("4. Expense Analysis")
  print("5. Save Data")
  print("6. Load Data")
  print("7. Exit")

  choice = input("Enter the number corresponding to your choice: ")

  if choice == '1':
    category = input(
        "Enter the expense category (Where you want to expense your money): ")
    amount = float(input("Enter the expense amount:₹ "))
    add_expense(category, amount)
    print(
        f"Expense of ₹ {amount:.2f} added to {category.capitalize()} successfully!"
    )

  elif choice == '2':
    amount = float(input("Enter the income amount: ₹ "))
    add_income(amount)
    print(f"Income of ₹{amount:.2f} added successfully!")

  elif choice == '3':
    remaining_budget = calculate_budget()
    print(f"\nRemaining Budget: ₹ {remaining_budget:.2f}")

  elif choice == '4':
    analyze_expenses()

  elif choice == '5':
    save_data()
    print("Your data saved successfully!")

  elif choice == '6':
    load_data()
    print("Data loaded successfully!")

  elif choice == '7':
    print("Exiting the Budget Tracker. Have a nice day!")
    break

  else:
    print("Invalid choice. Please enter a number between 1 and 7.")

os.system('cls' if os.name == 'nt' else 'clear')
