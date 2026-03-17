import os

import json

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
        
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        
        expense = {"amount": amount, "category": category}
        expenses.append(expense)
        
        save_expenses(expenses)
        
        print("Expense added!")
        
    except ValueError:
        print("Invalid amount")
        
def view_expenses(expenses):
    if not expenses:
        print("No expense yet")
    else:
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}, {exp['amount']}, {exp['category']}")
            
def show_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending: {total}")
    
def get_valid_index(expenses, message):
    while True:
        try:
            index = int(input(message)) -1
            
            if 0 <= index < len(expenses):
                return index
            else:
                print("Invalid index")
                
        except ValueError:
            print("Please enter a valid number")
            
def delete_expense(expenses):
        if not expenses:
            print("No expense to remove")
            return
            
        view_expenses(expenses)
                
        index = get_valid_index(expenses, "Expense no. to remove: ")
        
        removed = expenses.pop(index)
        save_expenses(expenses)
        
        print(f"Removed: {removed['amount']} - {removed['category']}")
        
def edit_expense(expenses):
    if not expenses:
        print("No expense to edit")
        return
    view_expenses(expenses)
    
    index = get_valid_index(expenses, "Expense no. to edit: ")
    
    new_amount = float(input("Enter new amount: "))
    new_category = input("Enter new category: ")
    
    expenses[index]["amount"] = new_amount
    expenses[index]["category"] = new_category
    
    save_expenses(expenses)
    
    print("Expense updated!")
    
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
    
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        print("-------Expense Tracker-------")
        print("1.Add Expense")
        print("2.View expense")
        print("3.Show Total Spending")
        print("4.Exit")
        print("5.Delete Expense")
        print("6.Edit Expenses")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_expense(expenses)
                
        elif choice == "2":
            view_expenses(expenses)
                    
        elif choice == "3":
            show_total(expenses)
            
        elif choice == "4":
            print("Exiting...")
            break
        
        elif choice == "5":
            delete_expense(expenses)
            
        elif choice == "6":
            edit_expense(expenses)
                
        else:
            print("Invalid choice")

        input("Press Enter to continue")
        
if __name__ == "__main__":
    main()