salary = 0

salary = float(input("Enter salary: $"))

numDependents = int(input("Enter number of dependents: "))

stateTax = salary * 0.065
print("\nState Tax: $", round(stateTax, 2))

federalTax = salary * .28
print("Federal Tax: $", round(federalTax, 2))

dependentDeduction = numDependents * (salary * .025)
print("Dependents: $", round(dependentDeduction, 2))

totalWithholding = stateTax + federalTax
takeHomePay = salary - totalWithholding + dependentDeduction

print("Salary: $", round(salary, 2))
print("Take-Home Pay: $", round(takeHomePay, 2))
