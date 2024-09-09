

# # 1. feladat
# rift = []
# with open('vonat.txt','r') as file:
#     for item in file:
#         rawdata = item.strip().split("\t")
#         rift.append(rawdata)
#
# #print(rift)
# #2. feladat
# train_id = []
# station_id = []
#
# for item1 in rift:
#     if item1[0] not in train_id:
#         train_id.append(item1[0])
#
#     if item1[1] not in station_id:
#         station_id.append(item1[1])
# print(f"2. feladat\nAz állomások Száma: {len(station_id)} \nA Vonatok száma: {len(train_id)} ")
#
# #3. feladat
#
# mittudomenmiez = []
#
# leghosszabb_allas = 0
#
#
# for item2 in rift:
#     mittudomenmiez.append({
#
#         'vonat': item2[0],
#         'allomas' : item2[1],
#         'ora' : int(item2[2])*60,
#         'perc' : int(item2[3]),
#         'indul-erkez' : item2[4]
#     })
#
#
#
# tarolo_dict = {}
# x = 1
# y = 1
# while x != 13:
#     for item3 in mittudomenmiez:
#         vonat_szama = int(item3['vonat'])
#         # if vonat_szama == y:
#         #     tarolo_dict[item3['vonat']] = tarolo_dict[
#         print(item3)
#
#     x += 1
#
#





menetrend = {}
with open('vonat.txt', 'r', encoding='utf-8') as fajl:
  for sor in fajl:
      adatok = sor.strip().split()          #  1    0	5	45	I
      for index, item in enumerate(adatok):
          if index != 4:
              adatok[index] = int(item)
                                              # adatok[0] = vonat szama
      if adatok[0] not in menetrend:          # adatok[1] = allomas szama
          menetrend[adatok[0]] = {}            #   adatok[0] = 1 mint int mert intnek neveztük a txt ből jövő str
      if adatok[1] not in menetrend[adatok[0]]:
          menetrend[adatok[0]][adatok[1]] = {}
      if adatok[4] == 'I':
                    #  ide mindig KEY                    # ide mindig VALUE
          menetrend[adatok[0]][adatok[1]]['indulas'] = adatok[2] * 60 + adatok[3]
      else:
          menetrend[adatok[0]][adatok[1]]['erkezes'] = adatok[2] * 60 + adatok[3]

#2. feladat


print('2. feladat')
print(f'Az állomások száma: {len(menetrend[1])}')
print(f'A vonatok száma: {len(menetrend)}')

#print(menetrend)


print('3. feladat')
maxx = {'allasido': menetrend[1][1]['indulas'] - menetrend[1][1]['erkezes'], 'vonat': 1, 'allomas': 1}
for vonat in menetrend:
  for allomas in range(1, len(menetrend[vonat]) - 1):
      if menetrend[vonat][allomas]['indulas'] - menetrend[vonat][allomas]['erkezes'] > maxx['allasido']:
          maxx['allasido'] = menetrend[vonat][allomas]['indulas'] - menetrend[vonat][allomas]['erkezes']
          maxx['vonat'] = vonat
          maxx['allomas'] = allomas
print(f"A(z) {maxx['vonat']}. vonat a(z) {maxx['allomas']}. állomáson {maxx['allasido']} percet állt.")


print("\n4. feladat")

azonosito = 2#int(input("Kérem adja meg a vonat azonositót! "))
ora_perc = '7 16'#input("Kérem adja meg a(z) óra percet! ")


print('\n5. feladat')
eloirt = 2 * 60 + 22
elteres = eloirt - (menetrend[azonosito][len(menetrend[azonosito])-1]['erkezes'] - menetrend[azonosito][0]['indulas'])

if elteres < 0:
  print(f'A(z) {azonosito}. vonat útja {abs(elteres)} perccel rövidebb volt az előírtnál.')
elif elteres == 0:
  print(f'A(z) {azonosito}. vonat útja pontosan az előírt ideig tartott.')
else:
  print(f'A(z) {azonosito}. vonat útja {abs(elteres)} perccel hosszabb volt az előírtnál.')


print("\n6.feladat")

txtfajlnev = 'halad' + str(azonosito) + '.txt'

with open(txtfajlnev,'w',encoding='utf-8') as kiiras:
    for allomas in range(1,len(menetrend[azonosito])):
        szamolas1 = menetrend[azonosito][allomas]['erkezes'] // 60
        szamolas2 = menetrend[azonosito][allomas]['erkezes'] % 60
        print(f"{allomas}. állomas: {szamolas1}:{szamolas2}",file=kiiras)


print("\n7.feladat")
ido = ora_perc.split()
beadott_ido = int(ido[0])*60 + int(ido[1])


for vonat in menetrend:
  if menetrend[vonat][0]['indulas'] < beadott_ido < menetrend[vonat][1]['erkezes']:
      print(f"A(z) {vonat}. vonat a 0. és a 1. állomás között járt. ")
  for allomas in range(1, len(menetrend[vonat])-1):
      if menetrend[vonat][allomas]['erkezes'] <= beadott_ido <= menetrend[vonat][allomas]['indulas']:
          print(f"A(z) {vonat}. vonat a {allomas}. állomáson állt.")
      if menetrend[vonat][allomas]['indulas'] < beadott_ido < menetrend[vonat][allomas + 1]['erkezes']:
          print(f"A(z) {vonat}. vonat a {allomas}. és a {allomas + 1}. állomás között járt. ")



print("\n")
print("\n")
# print(menetrend[1])
# print(menetrend[2])
for item in menetrend:
    print(item,menetrend[item])


