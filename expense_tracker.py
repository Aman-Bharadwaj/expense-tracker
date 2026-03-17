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
        print("Invaid amount")
        
def view_expenses(expenses):
    if not expenses:
        print("No expense yet")
    else:
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}, {exp['amount']}, {exp['category']}")
            
def show_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending: {total}")
    
def delete_expense(expenses):
        if not expenses:
            print("No expense to remove")
            return
            
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['amount']}, {exp['category']}")
                
            while True:       
                try:        
                    index = int(input("Expense no. to remove: ")) -1
                    
                    if 0<= index < len(expenses):
                        expenses.pop(index)
                        save_expenses(expenses)
                            
                        print("Expense removed")
                        break
                        
                    else:
                        print("Invalid index")
                                                
                except ValueError:
                    print("Please enter a valid number")
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
                
        else:
            print("Invalid choice")

        input("Press Enter to continue")
        
if __name__ == "__main__":
    main()