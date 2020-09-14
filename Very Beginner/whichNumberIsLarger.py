firstNum = 0; secondNum = 0; END = 0

print("Input", END, "for both numbers to end.")

firstNum = float(input("Input first number: "))
secondNum = float(input("Input second number: "))

while firstNum != END or secondNum != END:
    if firstNum > secondNum:
        print("First is larger.\n")
    elif firstNum < secondNum:
        print("Second is larger.\n")
    else:
        print("Numbers are equal.\n")

    firstNum = float(input("Input first number: "))
    secondNum = float(input("Input second number: "))
