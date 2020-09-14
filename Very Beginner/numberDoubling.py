originalNumber = int(input("Enter number to double or 0 to end: "))

while originalNumber != 0:
    calculatedAnswer = originalNumber * 2

    print(originalNumber, "doubled is", calculatedAnswer)

    originalNumber = int(input("Enter number to double or 0 to end: "))
