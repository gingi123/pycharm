




#with open('pizzeria.txt','r',encoding='utf=8') as file:
#    readfilein = file.read()
#    readfilein1= readfilein[:-1].split('\n')
#for line in readfilein1:
#    formating = line.split('\n')
#    print(formating[0])


#sorted_pizza = sorted(menu, key=lambda x: menu[0])





menu = []

with open('pizzeria.txt','r',encoding='utf=8') as file:
    readfilein = file.read()
    formating = readfilein.split('\n')
#x = 0
for item in range(0, len(formating)):
    if item % 3 == 0:
        menu.append({
            'PIZZA':formating[item],
        })
    if item % 3 == 1:
        pizza_price=formating[item]
        splitprice = pizza_price.split(' ')
        menu.append({
            'AR':splitprice[0],
            'FT': splitprice[1]
        })

print(*menu)




