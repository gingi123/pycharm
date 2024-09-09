def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    return d2-d1


utazasok = []
utazas = {}
#results = []
with open('utasadat.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:

        adatok = sor.strip().split()

        dat_ip = adatok[1].split('-')

                                                                  #
        utazas['megallo'] = int(adatok[0])                        #  0 20190326-0700 6572582 RVS 20210101
                                                                  #  0 20190326-0700 8808290 JGY 7
        utazas['datum'] = int(dat_ip[0])
        utazas['idopont'] = dat_ip[1]
        utazas['azonosito'] = adatok[2]
        utazas['tipus'] = adatok[3]
        utazas['ervenyes'] = int(adatok[4])
        utazasok.append(utazas)
        utazas = {}

        # results.append({
        #     'megallo': int(adatok[0]),
        #     'datum' : dat_ip[0],
        #     'idopont' : dat_ip[1],
        #     'azonosito' : adatok[2],
        #     'tipus' : adatok[3],
        #     'ervenyes' : adatok[4],
        # })


#
# for item in utazasok:
#     print(item)
# print(results)
print("1.feldat")

print("\n2.feladat")
print(f"A buszra {len(utazasok)} utas akart felszállni.")

print("\n3.feladt")
x = 0
for utasok in utazasok:
    if  utasok['ervenyes'] == 0:
        x += 1
    elif utasok['datum'] - utasok['ervenyes'] > 0 and utasok['ervenyes'] > 10:
        x += 1
    #print(utasok)
print(f'A buszra {x} utas nem szállhatott fel.')


print("\n4.feladat")
legtobb_utas = 0
UTAS = 0
Megallo_kör = 0
legtobb_megallo = 0
for item in utazasok:
    if Megallo_kör < item['megallo']:                # ha masik allomast szamol már akkor X az az utasok nullázva és Z atlep uj megalloba
        UTAS = 0
        Megallo_kör += 1                    #ezzel allitom be eppen az aktualis megallot

    UTAS += 1                   # ez szamolja az utasokat
    if UTAS > legtobb_utas:     # ha az összeszamolt utasok több mint az eddigi legtöbb  akkor ez a megallo a legtöbb
        legtobb_megallo = Megallo_kör  # de ha X kisszabakkor legtöbb megallo a regi marad
    legtobb_utas = max(legtobb_utas,UTAS)      # itt max fuggvény legtöbb utas


print(f'A legtöbb utas ({legtobb_utas})fő a {legtobb_megallo}. megállóban próbált felszállni.')

print("\n5.feladat")
ingye = ['NYP','RVS','GYK']
kedv = ['TAB','NYB']
kedvezmenyes = 0
ingyenes = 0

utasok['ervenyes'] > 10

for utasok_5 in utazasok:
    ervenyes = utasok_5['datum'] - utasok_5['ervenyes']

    if utasok_5['tipus'] in kedv and ervenyes <= 0 and utasok_5['ervenyes'] > 0 :
        kedvezmenyes += 1
    elif utasok_5['tipus'] in ingye and ervenyes <= 0 and utasok_5['ervenyes'] > 0:
        ingyenes += 1
print(f'Ingyenesen utazók száma: {ingyenes} fő')
print(f'A kedvezményesen utazók száma: {kedvezmenyes}fő')


print("\n6.feladat 'Függvény fent' ")  # függvény fent

print("\n7.feladat")
figyelmeztetesek = []

with open("figyelmeztetes.txt","a",encoding='utf-8') as figyelm:
    for item111 in utazasok:
        date = str(item111["datum"])    #20190326-0700
        erv_date = str(item111["ervenyes"])    #  20210101  vagy 0 ,1 ,6 ,7
        if item111["tipus"] != "JGY":
            ev1 = int(date[0:4])
            ho1 = int(date[4:6])
            nap1 = int(date[6:8])

            ev2 = int(erv_date[0:4])
            ho2 = int(erv_date[4:6])
            nap2 = int(erv_date[6:8])
            #print(f"{ev1,ho1,nap1} \t {ev2,ho2,nap2}")

            kulonbseg = napokszama(ev1, ho1, nap1, ev2, ho2, nap2)

            if 0 < kulonbseg < 4:
                print(f"{item111["azonosito"]} {ev2}-{ho2}-{nap2}",file=figyelm)


