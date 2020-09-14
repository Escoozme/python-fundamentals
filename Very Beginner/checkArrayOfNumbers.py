TWELVE = 12; END = 999
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
INPUTS = []
foundIt = False

number = int(input("Enter numbers:\n"))

while number != END:
    
    for x in range(0, TWELVE):
        if number == NUMBERS[x]:
            foundIt = True
            INPUTS.append(number)

    if foundIt == False:
        print("NO. NOT THAT NUMBER.\n")

    foundIt = False
    number = int(input())

INPUTS.reverse()

print(INPUTS)

print(NUMBERS.index(6))
