


print("1. feladat")

new_list = []

with open("melyseg.txt","r",encoding='utf-8') as godrocskek:
    for item in godrocskek:
        new_list.append(int(item.strip()))
        #godor = item.strip().split("    ")
        #new_list.append(list(map(int,godor)))


darabszam = 0
for item in new_list:
    darabszam += 1

print(f"A fájl adatainak száma: {darabszam}")

print("\n2.feldat")
distance = 9#int(input("Adjon megy egy távolság értéket: "))

for index,melyseg in enumerate(new_list,start=1):
    if index == distance:
        print(f"Ezen a helyen a felszín {new_list[index]} méter mélyen van ")

# print(new_list)

# for index in range(1,len(new_list)):
#     if distance == index:
#         print(f"Ez a kuyta fasza {new_list[index]}")

print("\n3.feladat")
erintetlen_darab = 0
for item in new_list:
    if item == 0:
        erintetlen_darab += 1
szazalek_szamitas = (erintetlen_darab/len(new_list))*100
print(f"Az érintetlen terület aránya {szazalek_szamitas:0.2f}%")


#4.feldat
elolozo_item = 0
sor_godor_ami_nullazva_lesz = []
godrok_lista = []
for item in new_list:
    if item > 0:
        sor_godor_ami_nullazva_lesz.append(item)
    if item == 0 and elolozo_item > 0:
        godrok_lista.append(sor_godor_ami_nullazva_lesz)
        sor_godor_ami_nullazva_lesz = []
    elolozo_item = item
with open('godrok.txt','w')as kimenet:
    for item in godrok_lista:

        print(F"{item}",file=kimenet)



print("\n5.feladat")
print(f"A gödrök száma: {len(godrok_lista)}")

print("\n6.feladat")
kezdopont = 0
vegpont = 0

if new_list[distance-1] == 0:
    print("Az adott helyen nincs gödör")
else:
    print("a,")
    for index in range(1,len(new_list)+1):
        if new_list[distance-1-index] == 0:
            kezdopont = distance-index+1
            break

    for index in range(1,len(new_list)+1):
        if new_list[distance-1+index] == 0:
            vegpont = distance+index-1
            break

print(f"A gödör kezdete: {kezdopont} méter, a gödör vége: {vegpont} méter.")

print("b,c")
legmelyebb_pont = 0
pozicio = kezdopont #- 1
holvagyunk = new_list[pozicio]
holakovetkezo = new_list[pozicio-1]
while new_list[pozicio] >= new_list[pozicio-1] and pozicio <= vegpont:  # persze mert ha mélyülés véget ér kilép a cilusból új ujra nem tud mélyülni
    pozicio += 1
    if new_list[pozicio-1] > legmelyebb_pont:
        legmelyebb_pont = new_list[pozicio-1]
while new_list[pozicio] <= new_list[pozicio-1] and pozicio <= vegpont:
    pozicio += 1
    if new_list[pozicio-1] > legmelyebb_pont:
        legmelyebb_pont = new_list[pozicio-1]
    #print("Poz: ",pozicio)
if pozicio > vegpont:
    print("A gödör folyamatosan mélyül")
else:
    print("A gödör nem mélyül")

print("c, második fele")
print(f"A legnagyobb mélysége {legmelyebb_pont} méter")

# print("c)")
# print(f'A legnagyobb mélysége {max(mélységek[kezdő - 1:záró])} méter.')
#
print("d,")
terfogat = 10 * sum(new_list[kezdopont - 1 :vegpont])
print(f'A térfogata {terfogat} m^3.')


print("e,")
biztonsagos = terfogat - 10 * (vegpont - kezdopont + 1)
print(f'A vízmennyiség {biztonsagos} m^3.')










