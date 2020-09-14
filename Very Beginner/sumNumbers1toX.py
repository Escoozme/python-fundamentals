number = int(input("Enter number: "))

summed = 0

for counter in range(1, number + 1):
    summed += counter

print("Sum of every number from 1 to", number, "is:", summed)
