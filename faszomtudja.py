#with open('pizzeria.txt', 'r', encoding='utf=8') as file:
#    raw = file.read()
#    pizza_and_prices = raw[:-1].split('\n')

#menu = []
#modified = []
#for i in range(0, len(pizza_and_prices)):
#    if i % 3 == 0:
#        menu.append({
#            'PIZZA': pizza_and_prices[i]
#        })
#        print(pizza_and_prices[i])
#    if i % 3 == 1:
        #menu[len(menu)- 1]['AR'] = pizza_and_prices[i]
#        pizza_and_prices[i] = int(pizza_and_prices[i].split(" "))
#        menu.append({
#            'AR': pizza_and_prices[i]
#        })
#        print(pizza_and_prices[i])
#
#
#
#
#   megvan mondjuk változoban hogy 800 Ft
#       ar.split(" ")[0]
#    hát bele kell rakni uj propként
#
#   pizza_item["ar_szammal"] = int(ar.split(" ")[0])
#
#    az ár helyére a szöveges ár kell
#
#
#
#
#
#sorted_menu = sorted(menu, key=lambda x: x['AR'])#,reverse=True)

#menu_plitting = dict(item.split(" ") for item in str.split (';'))
#print(menu)
#print(modified)
#print(menu[-1])
#print(len(menu))
#print(sorted_menu)












































with open('pizzeria.txt', 'r', encoding='utf=8') as file:
    raw = file.read()
    pizza_and_prices = raw[:-1].split('\n')

menu = []
#pizza_name = ""
#pizza_price = ""
for i in range(0, len(pizza_and_prices)):
    if i % 3 == 0:
        pizza_name = pizza_and_prices[i]
    if i % 3 == 1:
        pizza_price = pizza_and_prices[i]
        pizza_and_prices_mod = int(pizza_price.split(" ")[0])
        pizza_and_prices_mod2 = (pizza_price.split(" ")[1])
    if i % 3 == 2:
        menu.append({
            'PIZZA': pizza_name,
            'AR': pizza_and_prices_mod,
            'ARFT': pizza_and_prices_mod2,
       })



sorted_menu = sorted(menu, key=lambda x: x['AR'])#,reverse=True)

print(menu)
print(sorted_menu)