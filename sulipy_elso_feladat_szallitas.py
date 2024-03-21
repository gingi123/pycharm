delivery_items = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2 ]


print('2. Feladat')
allbox =sum(delivery_items)
print(f'Tárgyak tömegének összege: {allbox} KG')

print('3. feladat')
boxes = []
x = 0
for item in delivery_items:
    if x + item <= 20:
        x = x + item
    else:
        boxes.append(x)
        x = 0
        x = item
boxes.append(x)
print(f'Dobozok tartalmának tömege (kg):' ,*boxes)
print(f'A szükséges dobozok száma: ',len(boxes))














