import os

import json

try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

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
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            
            expense = {"amount": amount, "category": category}
            expenses.append(expense)
            
            with open("expenses.json", "w") as file:
                json.dump(expenses, file, indent=4)
            
            print("Expense added!")
            
        except ValueError:
            print("Invalid amount")
            
    elif choice == "2":
        if not expenses:
            print("No expenses yet")
            
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['amount']}, {exp['category']}")
                
    elif choice == "3":
        total = sum(exp["amount"] for exp in expenses)
        print("Total spending", total)
        
    elif choice == "4":
        print("Exiting...")
        break
    
    elif choice == "5":
        if not expenses:
            print("No expense to remove")
            
        else:
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['amount']}, {exp['category']}")
                
            while True:       
                try:        
                    index = int(input("Expense no. to remove: ")) -1
                    
                    if 0<= index < len(expenses):
                        expenses.pop(index)
                        with open("expenses.json", "w") as file:
                            json.dump(expenses, file, indent=4)
                            
                        print("Expense removed")
                        break
                        
                    else:
                        print("Invalid index")
                                                
                except ValueError:
                    print("Please enter a valid number")
            
    else:
        print("Invalid choice")

    input("Press Enter to continue")