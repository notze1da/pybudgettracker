from typing import List
from expense import Expense
import calendar
import datetime


def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000
    #get user to input their expense
    expense = get_user_expense()
    #write their expense to a file
    save_expense_to_file(expense, expense_file_path)
    #read the file and summarize the expenses
    summarize_expense(expense_file_path, budget)    



def get_user_expense():
    """defines get user expense where you will gather the expenses from user"""
    print(f"Getting User Expense!")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input(f"Enter expense amount: "))
    expense_categories = [
        "🦀︎Groceries", "🏠Rent", "⛽Gas", "🍟Restaurants", "🏎️ Car Maintenance", "✨Misc", "💼Work", "✈️ Fun"
    ]

    while True:
        print("Select an expense category: ")
        for i, category_name in enumerate(expense_categories): #enumerate numbers expense categories
            print(f" {i + 1}. {category_name}") #i+1 starts the list at 1 instead of 0
        
        value_range = f"[1 - {len(expense_categories)}]" #creates a range of values to choose from by counting the length of expense categories
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1 #have to add -1 cause of the index starting at zero
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else: 
            print("Invalid category. Please try again!")
        
#want to create categories that are createable next iteration

def save_expense_to_file(expense: Expense, expense_file_path):
    """defines save expense as where the expense gets saved and goes to a file"""
    print(f"Saving Expense to File! {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding='utf-8-sig') as f: #opens a file, if it doesnt exist it will be created. Doesn't override cause we use a
        f.write(f"{expense.name},{expense.category},{expense.amount}\n") #writes in file, creates three columns differnet row


def summarize_expense(expense_file_path, budget):
    """defines summarize expense where the expenses are calculated"""
    print(f"Summarizing Expenses!")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding='utf-8-sig') as f:
        lines = f.readlines() #list of strings
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, 
                amount=float(expense_amount), 
                category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses By Category: 📈")        
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses]) #creates a list of just dlr values for each expense
    print(red(f"You've spent 💸 ${total_spent:.2f} this month!"))

    remaining_budget = budget - total_spent
    print(cyan(f"You have 💰 ${remaining_budget:.2f} left this month!"))



    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget / remaining_days
    print(cyan(f" Budget Per Day ${daily_budget:.2f}"))

def cyan(text):
    return f"\033[92m{text}\033[0m"
def red(text):
    return f"\033[31m{text}\033[0m"

if __name__ == "__main__":
    """Makes it so if I use this in a different file and call to it that it doesn't run the whole thing"""
    main()