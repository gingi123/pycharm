


# 1.feladat

new_list = []

with open('melyseg.txt','r',encoding='UTF=8') as banya:
    for item in banya:
        format_item = item.strip().split(" ")
        new_list.append(format_item)

maga_abanya = new_list[2:]
maga_a_to = []

print("2.feladat")
sor = 12#int(input('A mérés sorának azonosítója='))
oszlop = 6#int(input('A mérés oszlopának azonosítója='))
print(f'A mért mélység az adott helyen {maga_abanya[sor-1][oszlop-1]} dm')

print('\n3.feladat')
for item in maga_abanya:
    for item2 in item:
        item3 = int(item2)
        if item3 > 0:
            maga_a_to.append(item3)

print(f"A tó felszíne: {len(maga_a_to)}m2, átlagos mélysége:{sum(maga_a_to)/len(maga_a_to)/10:0.2F}m")

print('\n4.feladat')
legmelyebb = 0
#a = 0
#b = 0
for item1 in maga_abanya:
    for item2 in (item1):
        itemint = int(item2)
        if itemint > legmelyebb:
            legmelyebb = itemint
#        b +=1
#    a += 1



print(f'A tó legnagyobb mélysége: {legmelyebb} dm ')
print(f'A legmélyebb helyek sor-oszlop koordinátái:')
for index,item in enumerate(maga_abanya):
    for index2,item2 in enumerate(item):
        megnezendo = int(maga_abanya[index][index2])
        if megnezendo == legmelyebb:
            print(f'{index+1};{index2+1}\t',end=" ")

print('\n\n5.feladat')
partvonal = 0
for index11,item11 in enumerate(maga_abanya):
    for index22,item22 in enumerate(item11):
        vizsgalt_szelet = int(item22)
        if maga_abanya[index11][index22] != "0" and maga_abanya[index11][index22-1] == "0": #baloldal szamol
            partvonal += 1
        if maga_abanya[index11][index22] != "0" and maga_abanya[index11][index22+1] == "0":# jobboldal
            partvonal += 1
        if maga_abanya[index11][index22] != "0" and maga_abanya[index11+1][index22] == "0":# alatta levot szamol
            partvonal += 1
        if maga_abanya[index11][index22] != "0" and maga_abanya[index11-1][index22] == "0": # folotte levot szamol
            partvonal += 1
print(f"A tó partvonala {partvonal}m hosszú")

print('\n6.feladat')
oszlop_azonosito = 6#int(input("A vizsgált szelvény oszlopának azonosítója="))


with open('diagram.txt','w')as kiiras:
    for index111,item111 in enumerate(maga_abanya,start=1):
        for index222,item222 in enumerate(item111,start=1):
            if index222 == oszlop_azonosito:
                printelendo = int(item222)/10

                print(f'{index111:02d}',round(printelendo)*"*",file=kiiras )

# for item in maga_abanya:
#     print(item,end="\n")

#print(maga_abanya[0][0])











