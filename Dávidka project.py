#import math

#bevitel = int(input("Kérem adjon megy egy számot: "))

#x= math.sqrt(bevitel)
#while True:
#    if math.sqrt(bevitel)*math.sqrt(bevitel)==bevitel:
#        print("ez négyzetszám ")
#    else:
#        print("ez nem négyzetszám")
#    bevitel = int(input("Kérem adjon megy egy számot: "))
#
#while True
#    inputo1 = int(input("Adgyá meg egy számot: "))
#    inputo2 = int(input("Adgyá még egyet: "))
#    inputo3 = int(input("megin agyá jó?: "))


#    if inputo1 >= inputo2 and inputo1 >= inputo3:
 #       print(f"Első szamod vót a legnagyobb.. vagyis: {inputo1}")
#    elif inputo2 >= inputo1 and inputo2 >= inputo3:
#        print(f"A második számod vót a legnágyobbb vagyis: {inputo2}")
#    elif inputo3 >= inputo1 and inputo3 >= inputo2:
#       print(F"Háá a harmadik a legnagyobb: {inputo3}")
#    elif inputo1 == inputo2 == inputo3:
#        print("Dikk ez mind egyforma")
#    else:
#        print("Valamit elbasztál!! nagyon ha ezt látod")

import random

def dobokocka_dobas():
    return random.randint(1, 6)  # 1 és 6 közötti véletlen számot ad vissza

dobasok_szama = int(input("Hányszor dobjon a dobókockákkal? "))

dobasok = []
for _ in range(dobasok_szama):
    dob1 = dobokocka_dobas()
    dob2 = dobokocka_dobas()
    dobasok.append(dob1 + dob2)  # Az eredmény hozzáadása a listához

# Eredmények számolása
eredmenyek = {}
for item in dobasok:
    if item in eredmenyek:
        eredmenyek[item] = eredmenyek[item] + 1
    else:
        eredmenyek[item] = 1

# Eredmények kiírása
print("Dobások eredményei:")
for item, szamlalo in sorted(eredmenyek.items()):
    print(f"{item}: {szamlalo} alkalommal")



print(dobasok)
print(eredmenyek)