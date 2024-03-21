
tablazat_halmaz = []
print("1.feladat")
open_file_input = 'konnyu.txt'#input("Adja meg a bemeneti fájl nevét! pl:konnyu.txt")
sor_input = 0#int(input("Adja meg a sor számát!(1-9ig)")) - 1
oszlop_input = 0#int(input("Adja meg az oszlop számát!(1-9ig)")) - 1

with open(open_file_input,'r') as sudoku:
    for item in sudoku:
        sudoku1 = item.strip().split(" ")
        tablazat_halmaz.append(list(map(int,sudoku1)))

print("3.feladat")
#3. a résza
#index = sor
#oszlop = item[][oszlop]

if item[sor_input][oszlop_input] == 0:
    print(f"Az adott helyen még nem töltötték ki. ")
else:
    print(f"Az adott helyen szereplő szám: {item[sor_input][oszlop_input]}")
#3.b része
print(f'A hely a(z) {3 * (sor_input // 3) + (oszlop_input // 3) + 1} résztáblához tartozik.')
#3.b része
# for index,item in enumerate(tablazat_halmaz,start=0):
#     if sor_input - 1 >= 0 and sor_input - 1 <= 2 and oszlop_input - 1  :
#         print("A hely a(z) 1 résztáblázathoz tartozik.")
#     if sor_input - 1 >= 3 and oszlop_input - 1 <= 5:
#         print("A hely a(z) 1 résztáblázathoz tartozik.")

print("\n4.feladat")
szazalek = []
b = 0
for item in (tablazat_halmaz[:-4]):
    for item2 in item:
        b = b + 1
        valti = int(item2)
        if valti == 0:

            szazalek.append(item2)

len_szazalek = len(szazalek)
szazalekszamit = (len_szazalek / b * 100)

print(f"Az üres helyek aránya {szazalekszamit:0.1f}%")

print("\n5.feladat")
AZ_igazi_tablazat = tablazat_halmaz[:-4]
lepesek = tablazat_halmaz[9:]
for lepes in lepesek:

    szerepel = False
    szam = lepes[0]
    sor = lepes[1] - 1
    oszlop = lepes[2] - 1
    print(f'A kiválasztott sor: {lepes[1]} oszlop: {lepes[2]} a szám: {lepes[0]}')
                                            #  szam,sor , oszlop
                                            # ['9', '2', '4']
                                            # ['7', '3', '6']
                                            # ['3', '6', '6']
                                            # ['8', '7', '9']

    if AZ_igazi_tablazat[sor][oszlop]:
        print('A helyet már kitöltötték.')
    else:
        if szam in AZ_igazi_tablazat[sor]:
            print('Az adott sorban már szerepel a szám.')
        for s in range(9):
            if AZ_igazi_tablazat[s][oszlop] == szam:
                szerepel = True
                break
        if szerepel:
            print('Az adott oszlopban már szerepel a szám.')
        else:
            for s in range(3 * (sor // 3), 3 * (sor // 3) + 3):
                for o in range(3 * (oszlop // 3), 3 * (oszlop // 3) + 3):
                    if AZ_igazi_tablazat[s][o] == szam:
                        szerepel = True
            if szerepel:
                print('A résztáblázatban már szerepel a szám.')
            else:
                print('A lépés megtehető.')


#print(f"{tablazat_halmaz}\n")
# for item in tablazat_halmaz:
#     print(item,end="\n")
#
#
#






