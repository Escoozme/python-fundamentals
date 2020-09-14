charge = 0.00; numOfChars = 8
charColor = "gold"; woodType = "oak"

charge += (numOfChars - 5) * 4

if charColor == "gold":
    charge += 15
if woodType == "oak":
    charge += 20

charge += 35

print("The charge for this sign is $ ", charge)

