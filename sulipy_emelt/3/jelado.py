import math
#1.feladat

kordinatak = []
with open('jel.txt','r',encoding='utf=8') as file:
    for item in file:
        database = item.strip().split(" ")
        kordinatak.append(list(map(int,database)))




print(kordinatak)

print("2.feladat")
sorsz_bevitel = 3#int(input('Adja meg a jel sorszámát!: '))


print(f"x={kordinatak[sorsz_bevitel-1][3]} y={kordinatak[sorsz_bevitel-1][4]}")

# print('\n3.feladat')

def eltelt(ido1,ido2):
    return abs((ido2[0] - ido1[0]) * 3600 + (ido2[1] - ido1[1]) * 60 + (ido2[2] - ido1[2]))


print('\n4.feladat')

kulonbseg = eltelt(kordinatak[0], kordinatak[-1])
ora = kulonbseg // 3600
perc = (kulonbseg % 3600) // 60
mperc = kulonbseg % 60
print(f'Időtartam: {ora}:{perc}:{mperc}')


print("\n5.feladat")
    
minx = 10000
maxx = -10000
miny = 10000
maxy = -10000
for jel in kordinatak:
    minx = min(minx, jel[3])  # if jel[3] < miny: "csere"
    maxx = max(maxx, jel[3])
    miny = min(miny, jel[4])
    maxy = max(maxy, jel[4])
print(f'Bal alsó: x:{minx} y:{miny}, jobb felső: x:{maxx} y:{maxy}')

print("\n6.feladat")

jelek_szama = len(kordinatak)


def tav(jel1, jel2):
    return math.sqrt((jel2[3]-jel1[3])**2 + (jel2[4]-jel1[4])**2)


osszesen = 0
for index in range(jelek_szama - 1):
    osszesen = osszesen + tav(kordinatak[index], kordinatak[index + 1])
print(f'Elmozdulás: {osszesen:0.3f} egység')

#7.feladat

with open ('kimaradt.txt','w',encoding='utf8') as kimenet:
    for index in range(jelek_szama - 1):
        kimaradt_tavolsag_szerint = 0
        kimaradt_ido_szerint = 0

        idokulonbseg = eltelt(kordinatak[index], kordinatak[index + 1])
        if idokulonbseg > 300:
            kimaradt_ido_szerint = (idokulonbseg - 1) // 300

        tavolsag = max(abs(kordinatak[index + 1][3] - kordinatak[index][3]), abs(kordinatak[index + 1][4] - kordinatak[index][4]))
        if tavolsag > 10:
            kimaradt_tavolsag_szerint = (tavolsag - 1) // 10

        if kimaradt_tavolsag_szerint > kimaradt_ido_szerint:
            print(kordinatak[index + 1][0], kordinatak[index + 1][1], kordinatak[index + 1][2], 'koordináta-eltérés',
                  kimaradt_tavolsag_szerint, file=kimenet)
        if kimaradt_tavolsag_szerint <= kimaradt_ido_szerint != 0:
            print(kordinatak[index + 1][0], kordinatak[index + 1][1], kordinatak[index + 1][2], 'időeltérés', kimaradt_ido_szerint,
                  file=kimenet)