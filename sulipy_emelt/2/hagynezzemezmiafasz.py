kep = []
with open('kep2.txt') as forrasfajl:
    for adatsor in forrasfajl:
        adatsor = adatsor.strip().split(' ')

        kepsor = []
        tarolo = []
        for item in adatsor:
            tarolo.append(int(item))
            if len(tarolo) == 3:
                kepsor.append(tarolo)
                tarolo = []
        kep.append(kepsor)


print("2.feladat")
sor_in = input("Kérem a képpont adatai! \nSor:")
oszlop_in = input("Oszlop:")
print(f"A képpont színe RGB{}")