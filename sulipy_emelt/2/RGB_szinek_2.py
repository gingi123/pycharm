# 0 85 112 0 86 113 0 86 113 0 86 113 0 86 113 0 86 113 0 86 113
#
#
#
#
#
kep = []
feladat_II_lista = []
with open('kep.txt') as file:
    for item in file:
        database = item.strip().split(' ')

        kesz_sor = []
        tarolo = []
        for item in database:
            tarolo.append(int(item))
            if len(tarolo) == 3:
                kesz_sor.append(tarolo)
                feladat_II_lista.append(tarolo)
                tarolo = []
        kep.append(kesz_sor)


print("2.feladat")
sor_in = 180#input("Kérem a képpont adatai! \nSor:")
oszlop_in = 320#input("Oszlop:")
print(f"A képpont színe RGB{kep[sor_in-1][oszlop_in-1]}")

print("\n3.feladat")
x = 0
leg_kissebb = 60000000
leg_kissebb_list = []
for item2 in feladat_II_lista:
    if sum(item2) < leg_kissebb:
        leg_kissebb = sum(item2)

    if sum(item2) == leg_kissebb:
        leg_kissebb_list.append(item2)
    if sum(item2) > 600:
        x += 1

print(f"A világos képpontok száma: {x}")

print("\n4.feladat")
print(f"A legsötétebb pont RGB összege: {leg_kissebb}")
print(f"A legsötétebb pixelek színe:")
for item3 in leg_kissebb_list:
    print(f"{item3}")


print("\n5.feladat")


def hatar(sorsz, elteres):     #ezt komplett nem értem sajnos // azért mostmár kezdem erősen kapizsgálni
    sor = kep[sorsz-1]
    for idx in range(len(sor)-1):
        if abs(sor[idx][2] - sor[idx+1][2]) > elteres:
            return True
    return False


print("\n6.feladat")


felho_sorok = []
for index in range(len(kep)):
    if hatar(index+1, 10):
        felho_sorok.append(index+1)

print(f'A felhő legfelső sora: {felho_sorok[0]}')
print(f'A felhő legalsó sora: {felho_sorok[-1]}')



print(kep)
















