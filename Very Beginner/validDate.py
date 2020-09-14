year = 0; month = 0; day = 0

MIN_YEAR = 0; MIN_MONTH = 1; MAX_MONTH = 12; MIN_DAY = 1; MAX_DAY = 31

validDate = True

month = int(input("Enter month: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))

#check to see if date is valid
if year <= MIN_YEAR:     #invalid year
    validDate = False
elif month < MIN_MONTH or month > MAX_MONTH:     #invalid month
    validDate = False
elif day < MIN_DAY or day > MAX_DAY:     #invalid day
    validDate = False

#test to see if date is valid. output date given and whether or not it's valid
if validDate == True:
    print(month, "/", day, "/", year, "is a valid date.\n")
else:
    print(month, "/", day, "/", year, "is an invalid date.\n")
