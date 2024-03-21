

inputo_taj = input('Kérem a TAJ- számot: ')
TAj_lastnumber = int(inputo_taj[-1])

TAJ_works = []
NUMBERS_for_kontroll = []


for item in inputo_taj:
    TAJ_works.append(int(item))

TAJ_works1 = TAJ_works[:-1]


for item1 in range(0,8):
    if item1 % 2 == 0:
        even = TAJ_works1[item1]*3
        NUMBERS_for_kontroll.append(even)
    if item1 % 2 == 1:
        odd = TAJ_works1[item1]*7
        NUMBERS_for_kontroll.append(odd)

SUM_Kontroll = sum(NUMBERS_for_kontroll)%10
Szorzatok_osszege = sum(NUMBERS_for_kontroll)

print(f"Az ellenőrző számjegy: {TAj_lastnumber}")
print(f"A Szorzatok összege: {Szorzatok_osszege}")


if TAj_lastnumber == SUM_Kontroll:
    print("Helyes a Szám!")
else:
    print("Hibás a Szám!!!!!!!!!!!!")
#print(TAJ_works)
print(TAJ_works1)
#print(NUMBERS_for_kontroll)















