import datetime
# total_expense = 0 
# print("--- welcome to the ankush's expense tracker ---")
# print("Type 'stop' to finish the program and see the total)")
# while True:
   # expense = input("Enter your expense: ")
   # if expense.lower() == "stop":
      # break
   # else:
       # try:
           # total_expense += float(expense)
       # except ValueError:
           # print("Invalid input. Please enter a number or 'stop'.")
#print(f"Total expense: {total_expense}")
#if total_expense > 1000:
   # print("Warning: Your total expenses exceed 1000.")
# else:
   # print("Great! Your total expenses are within the limit.")
#print("="*30)
expenses = {}
print("--- Advance Expense Tracker ---")
while True:
    item = input("Enter the item name (or type 'stop' to finish): ")
    if item.lower() == "stop":
        break
    try:
        price = float(input(f"How much did {item} cost? "))
        expenses[item] = price
    except ValueError:
        print("Invalid input. Please enter a number for the price.")

print("Expenses entered:")
for item, price in expenses.items():
    print(f"{item}: {price}")
print(f"Total advanced expense: {sum(expenses.values())}")
with open("expenses.txt", "a") as file:
    for item, price in expenses.items():
        file.write(f"{datetime.datetime.now()} - {item}: {price}\n")
