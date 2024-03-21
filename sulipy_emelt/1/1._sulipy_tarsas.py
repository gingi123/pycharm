#1.feladat

with open('tarsas_dobasok.txt','r') as file1:
    read_dobasok_in = file1.read()
    F_read_dobasok_in = read_dobasok_in[:-1].split(' ')
#print(F_read_dobasok_in)

for i in range(0,len(F_read_dobasok_in)): # innentől elvileg a dobások listám int
    F_read_dobasok_in[i] = int(F_read_dobasok_in[i])

with open('tarsas_osvenyek.txt','r') as file2:
    read_osvenye_in = file2.read()
    F_read_osvenye_in = read_osvenye_in.split('\n')
#print(F_read_osvenye_in)

#2.feladat
x = 0
for item1 in F_read_dobasok_in:
    x = x + 1
y = 0
for item2 in F_read_osvenye_in:
    y = y+1
print("2.feladat")
print(f"A dobások száma: {x}")
print(f"Az ösvények száma: {y}")

#3.feladat
the_longest = ""
the_longest_number = ""
for index,item4 in enumerate(F_read_osvenye_in,start=1):
    if len(item4) > len(the_longest):
        the_longest = item4
        the_longest_number = index
lang_the_longest = len(the_longest)
print("\n3.feladat")
print(f"Az egyik leghosszabb a(z) {the_longest_number}. ösvény hossza {lang_the_longest}")

#4.feladat
print("\n4.feladat")
#path_number = 0
#while path_number < 2:
path_number =9 #int(input("Adja meg az ösvény sorszámát: "))
#players_number = 100000
#while players_number  > 5:
players_number =5 #int(input("Adja meg a játékosok számát: "))

#5.feladat
print("\n5.feladat")
path = F_read_osvenye_in[path_number-1]
M_piece = path.count("M")
E_piece = path.count("E")
V_piece = path.count("V")

if M_piece:
    print(f"M: {M_piece}")
if E_piece:
    print(f"E: {E_piece}")
if V_piece:
    print(f"V: {V_piece}")

#6. feladat
#print("\n6.feladat")
with open ('tarsas_kulonleges.txt','w') as fileout:
    for number,itemm in enumerate(path,start=1):
        if itemm == "E" or itemm == "V":
            print(number, '\t' , itemm, file=fileout)

print("\n7.feladat")
print(len(path))

#long_chosen_path = len(path)
# player1 = 0
# player2 = 0
# player3 = 0
# player4 = 0
# player5 = 0
# round = 0
# while player1 >= long_chosen_path or player2 >= long_chosen_path or player3 >= long_chosen_path or player4 >= long_chosen_path or player5 >= long_chosen_path:
#     if players_number == 2:
#         for index,item in enumerate(F_read_dobasok_in,start=1):
#
#             if index % 3 == 0 or index == 1:
#                 player1 = player1 + item
#             if index % 2 == 0:
#                 player2 = player2 + item
#             round = round + 1
#     print(f"ennyi round: {round} player1: {player1} és player2: {player2}")

x = 0
ciklus = [0, 0, 0, 0, 0]
jatek = True
while jatek:
    for jatekos_idx in range(players_number):
        dobas = F_read_dobasok_in[ x * players_number + jatekos_idx]
        uj_mezo = ciklus[jatekos_idx] + dobas
        ciklus[jatekos_idx] = uj_mezo
        if uj_mezo >= len(path):
            jatek = False
    x = x + 1
print(f'A játék a(z) {x}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: ', end='')
for jatekos, mezo in enumerate(ciklus, start=1):
    if mezo >= len(path):
        print(jatekos, end='')

print('\n8. feladat')
print(f'{len(path) =}')
x = 0
allas = [0, 0, 0, 0, 0]
jatek = True
while jatek:
    for jatekos_idx in range(players_number):
        dobas = F_read_dobasok_in[x * players_number + jatekos_idx]
        uj_mezo = allas[jatekos_idx] + dobas
        allas[jatekos_idx] = uj_mezo
        if uj_mezo-1 < len(path):
            if path[uj_mezo-1] == 'E':
                allas[jatekos_idx] += dobas
            elif path[uj_mezo-1] == 'V':
                allas[jatekos_idx] -= dobas
        if allas[jatekos_idx] >= len(path):
            jatek = False
    x += 1
print('Nyertes(ek):', end='')
for jatekos, mezo in enumerate(allas, start=1):
    if mezo >= len(path):
        print(jatekos, end='')
print(f'\nA többiek pozíciója:')
for jatekos, mezo in enumerate(allas, start=1):
    if mezo < len(path):
        print(f'{jatekos}. játékos, {mezo}. mező')

