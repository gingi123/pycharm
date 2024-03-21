with open('pizzeria.txt', 'r', encoding='utf=8') as file:
    raw = file.read()
    pizza_and_prices = raw[:-1].split('\n')

menu = []
for i in range(0, len(pizza_and_prices)):
    if i % 3 == 0:
        menu.append({
            'PIZZA': pizza_and_prices[i]
        })
#        print(pizza_and_prices[i])
    if i % 3 == 1:
        menu[len(menu) - 1]['AR'] = pizza_and_prices[i]
#        print(pizza_and_prices[i])

print(menu)


#############################################################################

with open('pizzeria.txt', 'r', encoding='utf=8') as file:
    raw = file.read()
    pizza_and_prices = raw[:-1].split('\n')

menu = []
pizza_name = ""
pizza_price = ""
for i in range(0, len(pizza_and_prices)):
    if i % 3 == 0:
        pizza_name = pizza_and_prices[i]
    if i % 3 == 1:
        pizza_price = pizza_and_prices[i]
    if i % 3 == 2:
        menu.append({
            'PIZZA': pizza_name,
            'AR': pizza_price
       })

print(menu)


#################################################################


with open('pizzeria.txt', 'r', encoding='utf=8') as file:
    raw = file.read()
    pizza_and_prices = raw[:-1].split('\n\n')

menu = []

for item in pizza_and_prices:
    split_to_pizza_and_prices = item.split("\n")
    menu.append({
        'PIZZA': split_to_pizza_and_prices[0],
        'AR': split_to_pizza_and_prices[1]
    })


print(menu)