num1 = 53; num2 = -50; num3 = 78
largest = num1; smallest = num1

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3

print("The largest value is", largest)
print("The smallest value is", smallest)
