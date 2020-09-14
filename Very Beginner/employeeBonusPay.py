BONUS_1 = 50.00; BONUS_2 = 75.00; BONUS_3 = 100.00; BONUS_4 = 200.00

employeeFirstName = input("Enter employee's first name: ")
employeeLastName = input("Enter employee's last name: ")

numShifts = float(input("\nEnter number of shifts: "))
numTransactions = float(input("Enter number of transactions: "))

dollarValue = float(input("Enter dollar value of transactions: "))

score = (dollarValue / numTransactions) / numShifts

if score <= 30:
    bonus = BONUS_1
elif score >= 31 and score <= 69:
    bonus = BONUS_2
elif score >= 70 and score <= 199:
    bonus = BONUS_3
else:
    bonus = BONUS_4

print("Employee Name:", employeeFirstName, employeeLastName)
print("Employee Bonus: $", bonus)
