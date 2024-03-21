def orara_valt(o, p, msp, ezred_msp):
    return o + (p / 60) + (msp + (ezred_msp / 1000)) / 3600
#1.feladat


meresi_adatok_list = []
with open('meresek.txt','r',encoding='utf-8') as meresek:
    for item in meresek:
        meres = item.strip().split(" ")
        meresi_adatok_list.append(meres)
# meresi_adatok_list.pop(0)
# meresi_adatok_list.pop(-1)



print("2.feladat")
jarmuvek_darabszama = len(meresi_adatok_list)


print(f"A mérés során {jarmuvek_darabszama} jármű adatait rögzítették")

print("\n3.feladat")
y = 0
for index in range(jarmuvek_darabszama):
    ora = int(meresi_adatok_list[index][5])
    if ora < 9:
        y = y+1
print(f"9 óra elött {y} jármű haladt el a végponti mérőnél.")

print("\n4.feladat")

ido_bekerese = input("Adjon meg egy óra és perc értéket: ").strip().split(" ")
meres_kezdete = float(ido_bekerese[0]) + float(ido_bekerese[1]) / 60
meres_vege = float(ido_bekerese[0]) + float(ido_bekerese[1]) / 60 + 59.999 / 3600

z = 0
w = 0
for index in range(jarmuvek_darabszama):
    o = int(meresi_adatok_list[index][1])
    p = int(meresi_adatok_list[index][2])
    msp = int(meresi_adatok_list[index][3])
    ezred_msp = int(meresi_adatok_list[index][4])
    jarmu_be = orara_valt(int(meresi_adatok_list[index][1]),int(meresi_adatok_list[index][2]),int(meresi_adatok_list[index][3]),int(meresi_adatok_list[index][4]))
    jarmu_ki = orara_valt(int(meresi_adatok_list[index][5]),int(meresi_adatok_list[index][6]),int(meresi_adatok_list[index][7]),int(meresi_adatok_list[index][8]))
    ora1 = int(meresi_adatok_list[index][1])
    ora2 = int(meresi_adatok_list[index][2])
    input_ora = int(ido_bekerese[0])
    input_perc = int(ido_bekerese[1])
    if ora1 == input_ora and ora2 == input_perc:
        z = z +1
    if meres_vege > jarmu_be and meres_kezdete < jarmu_ki:
        w = w + 1
print(f"a. A kezdeti méréspontnál elhaladt járművek száma: {z}")
print(f"b. A forgalom sűrűsége {w/10}")
# print(ido_bekerese[0])
# print(ido_bekerese[1])

print("\n5.feladat")

#v = s/t
leggyorsabb_auto = []
legnagyobb_sebesseg = 0
gyorshajtok_szama = 0
gyorshajtok_listaja_buntetve = []
buntetes_A = 30000
buntetes_B = 45000
buntetes_C = 60000
buntetes_D = 200000
new_gyorshajtok_listaja_buntetve = []
harmashalmaz = []
for index in range(jarmuvek_darabszama):
    jarmu_be = orara_valt(int(meresi_adatok_list[index][1]), int(meresi_adatok_list[index][2]),int(meresi_adatok_list[index][3]), int(meresi_adatok_list[index][4]))
    jarmu_ki = orara_valt(int(meresi_adatok_list[index][5]), int(meresi_adatok_list[index][6]),int(meresi_adatok_list[index][7]), int(meresi_adatok_list[index][8]))
    s = 10
    t = jarmu_ki - jarmu_be
    v = s/t
    format_v = round(v)
    if v > legnagyobb_sebesseg:
        legnagyobb_sebesseg = v
    if v > 90:
        gyorshajtok_szama = gyorshajtok_szama + 1
    if v > 104:
        gyorshajtok_listaja_buntetve.append(meresi_adatok_list[index][0])
        gyorshajtok_listaja_buntetve.append(format_v)
        harmashalmaz.append(meresi_adatok_list[index][0])
        harmashalmaz.append(format_v)
        if v > 104 and v <= 121:
            gyorshajtok_listaja_buntetve.append(buntetes_A)
            harmashalmaz.append(buntetes_A)
        if v > 121 and v <= 136:
            gyorshajtok_listaja_buntetve.append(buntetes_B)
            harmashalmaz.append(buntetes_B)
        if v > 136 and v <= 151:
            gyorshajtok_listaja_buntetve.append(buntetes_C)
            harmashalmaz.append(buntetes_C)
        if v > 151:
            gyorshajtok_listaja_buntetve.append(buntetes_D)
            harmashalmaz.append(buntetes_D)
        if len(harmashalmaz) == 3:
            new_gyorshajtok_listaja_buntetve.append(harmashalmaz)
    harmashalmaz = []



for index,item in enumerate(meresi_adatok_list):
    jarmu_be = orara_valt(int(meresi_adatok_list[index][1]), int(meresi_adatok_list[index][2]),int(meresi_adatok_list[index][3]), int(meresi_adatok_list[index][4]))
    jarmu_ki = orara_valt(int(meresi_adatok_list[index][5]), int(meresi_adatok_list[index][6]),int(meresi_adatok_list[index][7]), int(meresi_adatok_list[index][8]))

    s = 10
    t = jarmu_ki - jarmu_be
    v = s / t
    if legnagyobb_sebesseg == v:
        leggyorsabb_auto.append(item)

legnagyobb_sebesseg1 = int(legnagyobb_sebesseg)
# print(legnagyobb_sebesseg1)
# print(leggyorsabb_auto)
elozes = 0
for index,item in enumerate(meresi_adatok_list):
    jarmu_be = orara_valt(int(meresi_adatok_list[index][1]), int(meresi_adatok_list[index][2]),int(meresi_adatok_list[index][3]), int(meresi_adatok_list[index][4]))
    jarmu_ki = orara_valt(int(meresi_adatok_list[index][5]), int(meresi_adatok_list[index][6]),int(meresi_adatok_list[index][7]), int(meresi_adatok_list[index][8]))
    leggyorsabbjarmu_be = orara_valt(int(leggyorsabb_auto[0][1]), int(leggyorsabb_auto[0][2]),int(leggyorsabb_auto[0][3]), int(leggyorsabb_auto[0][4]))
    leggyorsabbjarmu_ki = orara_valt(int(leggyorsabb_auto[0][5]), int(leggyorsabb_auto[0][6]),int(leggyorsabb_auto[0][7]), int(leggyorsabb_auto[0][8]))
    if jarmu_be <= leggyorsabbjarmu_be and leggyorsabbjarmu_ki < jarmu_ki:
        elozes = elozes + 1



print(f"A legnagyobb sebességgel haladó jármű \n\t\trendszáma: {leggyorsabb_auto[0][0]} ")
print(f"\t\tátlagsebessége: {legnagyobb_sebesseg1}km/h")
print(f"\t\tátal elhagyott járművek száma: {elozes}")

#print(f'\n{meresi_adatok_list}')
print('\n6.feladat')

szazalekos_gyorhajtok = gyorshajtok_szama/jarmuvek_darabszama
print(f"A járművek {szazalekos_gyorhajtok*100:0.2f}% volt gyorshajtó")

#print("\n7.feladat")


#print(new_gyorshajtok_listaja_buntetve)


with open('buntetes.txt','w',encoding='utf-8')as bunti:
    for index,item in enumerate(new_gyorshajtok_listaja_buntetve,start=0):
        print(f"{item[0]}\t{item[1]} km/h\t\t{item[2]} Ft",file=bunti)






