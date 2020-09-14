name = ""
gross = 0; deduct = 0; net = 0; RATE = 0.25
QUIT = "XXX"
REPORT_HEADING = "Payroll Report "
END_LINE = "***End of Report "

print(REPORT_HEADING)
name = input("Enter employee's name: ")

while name != QUIT:
    gross = float(input("Enter employee's gross pay: "))

    deduct = gross * RATE
    net = gross - deduct

    print("Name: ", name)
    print("Gross Pay: ", gross)
    print("Deductions: ", deduct)
    print("Net Pay: ", net)

    name = input("Enter employee's name: ")

print(END_LINE)
