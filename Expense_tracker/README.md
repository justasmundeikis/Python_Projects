# Expense Tracker

This is a simple Expense Tracker program written in Python. It allows you to track your daily expenses, categorize them, and compare your total spending against a predefined budget. The project was inspired by a video from the Pixegami channel on YouTube, which can be found [here](https://youtu.be/HTD86h69PtE?list=PLZJBfja3V3Rsbiz84Z63IXnTQZH_Rnfuo).

However, this implementation extends the original solution by adding:
- **Additional Error Handling:** Added more `try-except` blocks to handle potential user input errors.
- **Date Tracking:** Each expense entry now includes a date to track when the expenditure was made.

## Project Overview

### Features
- **Expense Entry:** Users can enter expenses, categorize them, and track the date when the expense occurred.
- **Expense Categorization:** Expenses can be categorized into predefined categories like Food, Home, Work, Fun, and Misc.
- **Expense Saving:** All expenses are saved to a CSV file (`expenses.csv`), which can be reused across multiple runs of the program.
- **Expense Summary:** The program summarizes the expenses, showing the total amount spent in each category and comparing it against a monthly budget.

### Inputs
- **Expense Name:** The name or description of the expense.
- **Expense Amount:** The monetary value of the expense (e.g., 10.99).
- **Expense Category:** A predefined category to which the expense belongs (e.g., Food, Home, Work, Fun, Misc).
- **Date:** The date when the expense was made (automatically recorded).

### Outputs
- **Expense Summary:** A summary of the total spending, remaining budget, and average daily spending required to stay within the budget for the rest of the month.
- **Warnings:** Alerts when you are close to exceeding the budget or have already exceeded it.

## How to Use

1. **Clone the Repository:**

```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
```

2. **Run the Program:**

Run the program by executing the following command:

```bash
python3 expense_tracker.py
```

3. **Enter Your Expenses:**

Follow the prompts to enter your expense details. The program will guide you through entering the name, amount, and selecting a category.

4. **View Summary:**

After entering your expenses, the program will display a summary of your spending and compare it against your budget.

## Code Structure

* `expense_tracker.py`: The main script that handles user interaction, file management, and summarizing expenses.
* `expense.py`: A simple Expense class used to represent each expense.

## Example:

```bash
$ python3 expense_tracker.py
Running Expense Tracker
Enter expense name: Lunch
Enter expense amount: 12.50
Select a category:
 1. 🍔 Food
 2. 🏠 Home
 3. 👜 Work
 4. 🥳 Fun
 5. 📣 Misc
Enter a category number (1-5): 1
You have spent 12.5
Remaining budget: 387.5
Remaining budget per day: 12.5
```

## Improvements and Future Work

* Enhanced Reporting: Implement more detailed reporting options, such as weekly summaries, trend analysis, and identification of highest spending categories. This will provide deeper insights into spending habits.
* Reporting Backend: Utilize Pandas for more sophisticated data analysis and calculations. Pandas will allow for efficient manipulation and aggregation of data, improving the accuracy and flexibility of reports.
* Graphical User Interface (GUI): Develop a user-friendly graphical interface to make the application more accessible and easier to use. A GUI could simplify data entry, expense tracking, and report generation.
* Database Integration: Transition from a CSV file to an SQLite database for storing expense data. This will enhance data integrity, scalability, and support advanced querying capabilities. An SQLite database will allow for more robust data management and retrieval.`