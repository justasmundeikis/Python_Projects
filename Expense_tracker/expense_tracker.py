import os
import calendar
import datetime
from expense import Expense

def main():
    """Main function to run the expense tracker."""
    print("Running Expense Tracker")
    
    # Path to the CSV file where expenses will be recorded.
    expense_file_path = 'expenses.csv'
    
    # User-defined budget for the month.
    budget = 400
    
    # Get the current date and time.
    now = datetime.datetime.now()

    # Check if the expense file exists; if not, create it and add the header.
    if not os.path.exists(expense_file_path):
        with open(expense_file_path, 'w') as f:
            f.write("date,name,category,amount\n")

    # Get a new expense entry from the user.
    expense = get_user_expense(now)
    
    # Save the expense to the file.
    save_expense_to_file(expense, expense_file_path)
    
    # Summarize the expenses and compare them against the budget.
    summarize_expenses(expense_file_path, budget, now)

def get_user_expense(now):
    """Prompt user for expense details and return an Expense object."""
    while True:
        try:
            # Prompt user for the name and amount of the expense.
            expense_name = input("Enter expense name: ")
            expense_amount = float(input("Enter expense amount: "))
            break  # Exit loop if input is valid.
        except ValueError:
            # Handle invalid numeric input for the expense amount.
            print("Invalid amount. Enter a numeric value.")
    
    # Predefined list of expense categories.
    expense_categories = ["🍔 Food", "🏠 Home", "👜 Work", "🥳 Fun", "📣 Misc"]
    
    while True:
        print("Select a category:")
        
        # Display categories for user selection.
        for index, category_name in enumerate(expense_categories, start=1):
            print(f" {index}. {category_name}")
        
        try:
            # Prompt user to select a category by its number.
            selected_index = int(input(f"Enter a category number (1-{len(expense_categories)}): ")) - 1
            if selected_index in range(len(expense_categories)):
                # Return an Expense object if the selection is valid.
                selected_category = expense_categories[selected_index]
                return Expense(date=now.strftime('%Y-%m-%d'), name=expense_name, category=selected_category, amount=expense_amount)
            else:
                # Notify the user if the selected number is not valid.
                print("Invalid selection. Please try again.")
        except ValueError:
            # Handle non-integer input for the category selection.
            print("Please enter a valid number.")

def save_expense_to_file(expense: Expense, file_path: str):
    """Save the given expense to the specified file."""
    try:
        # Write the expense details to the file with the current date.
        with open(file_path, "a") as file:
            file.write(f"{expense.date},{expense.name},{expense.category},{expense.amount}\n")
    except IOError as e:
        # Handle errors that may occur during file writing.
        print(f"Failed to write to file {file_path}: {e}")

def summarize_expenses(file_path: str, budget: float, now):
    """Summarize expenses from the file and compare against the budget."""
    expenses = []
    
    # Read the expenses from the file, skipping the header row.
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]  # Skip the header
        for line in lines:
            expanse_date, expense_name, expense_category, expense_amount = line.strip().split(",")
            # Create an Expense object for each entry in the file.
            expense = Expense(
                date = expanse_date,
                name=expense_name, 
                category=expense_category, 
                amount=float(expense_amount)
            )
            expenses.append(expense)
    
    # Calculate the total amount spent per category.
    amount_by_category = {}

    for expense in expenses:
        if expense.category in amount_by_category:
            amount_by_category[expense.category] += expense.amount
        else:
            amount_by_category[expense.category] = expense.amount
    
    # Print the amount spent in each category.
    for category, amount in amount_by_category.items():
        print(f"{category}: {amount}")

    # Calculate and print the total amount spent.
    total_spent = sum(exp.amount for exp in expenses)
    print(f"You have spent {total_spent}")
    
    # Calculate and print the remaining budget.
    remaining_budget = budget - total_spent
    print(f"Remaining budget: {remaining_budget}")
    
    # Provide warnings if the budget is exceeded or nearly exceeded.
    if remaining_budget < 0:
        print(f"Warning! You have exceeded your budget by {-remaining_budget}!")
    elif remaining_budget < budget * 0.1:
        print(f"Warning! You are close to exceeding your budget. Only {remaining_budget} left!")
    
    # Calculate and print the average remaining budget per day.
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    average_remaining_per_day = round(remaining_budget / remaining_days, 1)
    print(f"Remaining budget per day: {average_remaining_per_day}")

# Entry point for the program.
if __name__ == "__main__":
    main()