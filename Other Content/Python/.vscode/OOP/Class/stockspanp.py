N = 7
i = 0
price = [100,80, 60 ,75 ,60, 75, 85 ]

for i in N:
    if price[i] >= 60:
        price[i] = 1
        price.append(i)
    if price[i] <= 60 or price[i]== 60:
        price[i] = 2 
        price.append(i)

print(price[i])