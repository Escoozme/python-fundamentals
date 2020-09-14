tuition = 15000

rate = float(input("Enter rate: "))

for counter in range(1, 11):
    print("Year", counter, "tuition: $", round(tuition, 2), "\n")
    
    tuition += (tuition * rate)
