
#1.feladat


y = 0
lako_adatok = []
lako_adatok_dic = []
szorzo_szamok = []
with open('utca.txt','r') as adatok:
    for item in adatok:
        beolvasas = item.strip().split(" ")
        egydarabos = []
        for item in beolvasas:
            egydarabos.append(item)
            y = y + 1
            # if len(egydarabos) == 3 and len(szorzo_szamok) == 0:
            if y > 1 and y < 3 :
                szorzo_szamok.append(egydarabos)
            if len(egydarabos) == 5:
                lako_adatok.append(egydarabos)
                egydarabos = []


# lako_adatok.pop(0)


darab_telek = len(lako_adatok)
print(f"2.feladat. A mintában {darab_telek} telek szerepel")

input_ado = str(68396)#input("3.feladat. Egy tulajdonos adószáma:")
szamlalo = len(lako_adatok)
x = 0
for index in range(szamlalo):
    if input_ado == lako_adatok[index][0]:
        print(f"{lako_adatok[index][1]} utca {lako_adatok[index][2]}")
        x = x + 1
if x == 0:
    print("Nem szerepel az adatállományban")

#4.feladat

def ado(adosav,alapterulet):
    # a = 800
    # b = 600
    # c = 100
    fizetendo_ado = (adosav * alapterulet)
    if fizetendo_ado < 10000:
        return 0
    else:
        return fizetendo_ado

print("5.feladat")
a=0
b=0
c=0
A_szorzo = int(szorzo_szamok[0][0])
B_szorzo = int(szorzo_szamok[0][1])
C_szorzo = int(szorzo_szamok[0][2])
AAdo_osszesen = 0
BAdo_osszesen = 0
CAdo_osszesen = 0
for index in range(szamlalo):
    if lako_adatok[index][3] == "A":
        A_adomerteke = ado(A_szorzo,int(lako_adatok[index][4]))
        AAdo_osszesen = AAdo_osszesen + A_adomerteke
        a=a+1

    if lako_adatok[index][3] == "B":
        B_adomerteke = ado(B_szorzo, int(lako_adatok[index][4]))
        BAdo_osszesen = BAdo_osszesen + B_adomerteke
        b=b+1
    if lako_adatok[index][3] == "C":
        C_adomerteke = ado(C_szorzo, int(lako_adatok[index][4]))
        CAdo_osszesen = CAdo_osszesen + C_adomerteke
        c=c+1

print(f"A sávba {a} telek esik, az adó {AAdo_osszesen} Ft")
print(f"B sávba {b} telek esik, az adó {BAdo_osszesen} Ft")
print(f"C sávba {c} telek esik, az adó {CAdo_osszesen} Ft")

print("6.feladat")
felhaborodott_utcak = []
for index in range(szamlalo-1):

    if lako_adatok[index][1] == lako_adatok[index+1][1] and lako_adatok[index][3] != lako_adatok[index+1][3] and lako_adatok[index][1] not in felhaborodott_utcak:
            felhaborodott_utcak.append(lako_adatok[index][1])

for item in felhaborodott_utcak:
    print(item)

#7.feladat
ado_lebontva_lakokra = []


ado_lebontvahossz = len(ado_lebontva_lakokra)
A_szorzo = int(szorzo_szamok[0][0])
B_szorzo = int(szorzo_szamok[0][1])
C_szorzo = int(szorzo_szamok[0][2])



for index in range(szamlalo):

    if lako_adatok[index][3] == "A" :
        A_adomerteke = ado(A_szorzo,int(lako_adatok[index][4]))
        ado_lebontva_lakokra.append({
            "ADOSZAM":lako_adatok[index][0],
            "ÖSSZADO":A_adomerteke})



    if lako_adatok[index][3] == "B":
        B_adomerteke = ado(B_szorzo, int(lako_adatok[index][4]))
        ado_lebontva_lakokra.append({
            "ADOSZAM": lako_adatok[index][0],
            "ÖSSZADO": B_adomerteke})


    if lako_adatok[index][3] == "C":
        C_adomerteke = ado(C_szorzo, int(lako_adatok[index][4]))
        ado_lebontva_lakokra.append({
            "ADOSZAM": lako_adatok[index][0],
            "ÖSSZADO": C_adomerteke})


#7.feladat

new_dict = {}

for item in ado_lebontva_lakokra:
    adoszam = item["ADOSZAM"]
    ado = int(item["ÖSSZADO"])
    if adoszam in new_dict:
        new_dict[adoszam] = new_dict[adoszam] + ado
    else:
        new_dict[adoszam] = ado

with open('fizetendo.txt', 'w', encoding='utf-8') as fizetendo:
    for item in new_dict:
        print(item, new_dict[item], file=fizetendo)




# print(ado_lebontva_lakokra)
#print(new_dict)
#print(new_dict[item])
# print("\n kitudja még itt mi lesz")
# for item in new_dict:
#    print(item,new_dict[item])

#print(new_dict["38522"])

print(ado_lebontva_lakokra)

print(new_dict)







