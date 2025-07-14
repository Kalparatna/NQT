'''

Q2.Write a program that continuously takes user input for the following details:
•	Income (amount earned).
•	Type of Material (category of expenditure).
•	Expenditure on that Material (amount spent).
The input process continues until the user enters “done”.
After input completion, the program should:
•	Display the total income.
•	Calculate and display the total savings (Income – Total Expenditure).
•	List where the money was spent along with respective expenditure.


Enter type of material: Food
Enter expenditure on Food: 1000

Enter income (or 'done' to finish): 2000
Enter type of material: Transport
Enter expenditure on Transport: 500

Enter income (or 'done' to finish): done

'''

total_income = 0
total_expenditure = 0
expenses = [] 

while True:
    income = input("Enter income (or 'done' to finish): ")

    if income.lower() == "done":
        break  

    income = int(income)
    total_income += income  

    while True:
        material = input("Enter type of material (or 'done' to enter new income): ")
        if material.lower() == "done":
            break  

        exp = int(input(f"Enter expenditure on {material}: "))
        total_expenditure += exp  
        expenses.append((material, exp))  #stroing as touple


savings = total_income - total_expenditure

print("Total Income: ₹", total_income)
print("Total Expenditure: ₹", total_expenditure)
print("Total Savings: ₹", savings)

print("\nWhere the money was spent:")
for material, amount in expenses:
    print(f"- {material}: ₹{amount}")

