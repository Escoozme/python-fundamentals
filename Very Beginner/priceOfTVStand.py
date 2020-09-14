itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
salePrice = 0
profit = 0
saleProfit = 0

profit = retailPrice - wholesalePrice
salePrice = retailPrice - retailPrice * .25
saleProfit = salePrice - wholesalePrice

print("Item Name:", itemName)
print("Retail Price: $", retailPrice)
print("Wholesale Price: $", wholesalePrice)
print("Profit: $", profit)
print("Sale Price: $", salePrice)
print("Sale Profit: $", saleProfit)
