
##arr = []
##for i in range(10):
##    arr.append([])
##    for j in range(5):
##        arr[i].append(i*j)
##
##print(arr)

##enemies = []
##counterX, counterY = 284, 219
##for r in range(6):
##    enemies.append([])
##    for c in range(6):
##        enemies[r].append([counterX, counterY])
##        counterX += 85
##    counterY += 55
##    counterX = 284
##
##print(enemies)

enemies1 = []
for counterX in range(284, 794, 85):
    enemies1.append([counterX, 219])

print(enemies1)

#test