#checks if sum of two numbers equals the third
firstNum = 0; secondNum = 0;thirdNum = 0; END = 0

print("Input", END, "for all three numbers to end.")

firstNum = float(input("Input first number: "))
secondNum = float(input("Input second number: "))
thirdNum = float(input("Input third number: "))

while firstNum != END or secondNum != END or thirdNum != END:
    if firstNum + secondNum == thirdNum:
        print("The first and second numbers equal the third.\n")
    elif firstNum + thirdNum == secondNum:
        print("The first and third numbers equal the second.\n")
    elif secondNum + thirdNum == firstNum:
        print("The second and third numbers equal the first.\n")
    else:
        print("No two numbers equal the third.")

    firstNum = float(input("Input first number: "))
    secondNum = float(input("Input second number: "))
    thirdNum = float(input("Input third number: "))
