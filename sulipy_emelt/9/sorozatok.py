
#1. feladat

new_list = []

with open('lista.txt','r',encoding='UTF=8') as file:
    #x = 1
    temporari_list = []
    for item in file:
        item1 = item.strip()
        temporari_list.append(item1)
        if len(temporari_list) == 5:
            new_list.append({
                'Dátum': temporari_list[0],
                'Név': temporari_list[1],
                'Évad_ep': temporari_list[2],
                'Perc': int(temporari_list[3]),
                'Megtekintés': temporari_list[4],
            })
            temporari_list = []
            #x = 1
        #x += 1

#2. feladat
def adasbakerules(new_list):
    x = 0
    for index,item in enumerate(new_list):
        if len(new_list[index]['Dátum']) > 2:
            x += 1
    return print(f"2. feladat\nA listában {x} db vetítési dátummal rendelkező epizód van\n")


#3. feladat
def megnezett_szazelek(new_list):
    x = 0
    osszes_film = len(new_list)
    for i in range(len(new_list)):
        if new_list[i]["Megtekintés"] == '1':
            x += 1
    return print(f"3. feladat\nA litában lévő epizódok {100*(x/osszes_film):0.2f}% -át látta.\n")

#4. feladat
def mennyi_idot(new_list):
    all_time = 0
    for i in range(len(new_list)):
        if new_list[i]["Megtekintés"] == '1':
            part = int(new_list[i]["Perc"])
            all_time += part

    napok = all_time // (24*60)
    orak = all_time % (24*60) // 60
    percek = all_time % 60
    return print(f"4.feladat\nA sorozatnézéssel {napok} napot {orak} orat és {percek} percet\n")

#5.feladat
def adjon_egy_datumot(new_list):
    print("\n5.feladat")
    whole_new_list = []
    bekeres_list = []


    bekeres = '2017.10.18' #input("Adjon meg egy dátumot: ")
    sp_bekeres = bekeres.split(".")
    for item in sp_bekeres:
        bekeres_list.append(item)
    for index,item in enumerate(new_list):
        if not new_list[index]["Dátum"] == "NI" and new_list[index]["Megtekintés"] == "0":
            vizs_date = new_list[index]["Dátum"].split(".")
            if int(bekeres_list[0]) >= int(vizs_date[0]) and int(bekeres_list[1]) >= int(vizs_date[1]) and int(bekeres_list[2]) >= int(vizs_date[2]):
                print(f"{new_list[index]["Évad_ep"]}        {new_list[index]["Név"]}")


#6.feladat

def hetnapja(ev, honap, nap):
    napok = ['v', 'h', 'k', 'sze', 'cs', 'p', 'szo']
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if honap < 3:
        ev -= 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev //
                      400 + honapok[honap - 1] + nap) % 7]
    return hetnapja


#7.feladat
def vizsgalt_nap(new_list):
    print("\n7.feladat")
    vizsgalt_nap = "cs"#input('Adja meg a hét egy napját (például cs)! Nap=')
    aznapi_sororozatok = set()
    for index,item in enumerate(new_list):
        if 'NI' not in item['Dátum']:
            epizod_datuma = item['Dátum'].split('.')
            epizod_napja = hetnapja(int(epizod_datuma[0]), int(epizod_datuma[1]), int(epizod_datuma[2]))
        if vizsgalt_nap == epizod_napja:
            aznapi_sororozatok.add(item['Név'])
    if len(aznapi_sororozatok):
        for item in aznapi_sororozatok:
            print(item)

    else:
        print('Az adott napon nem kerül adásba sorozat.')


#8.feladat
def another_universe(new_list):
    multiple_value_dict = {}                                        #item["Perc"]   "45"  perc ugye
    for index,item in enumerate(new_list):                         #multiple_value_dict[item]["Név"]  "Games"
        if multiple_value_dict.get(item["Név"],0): #ha a kulcs mar benn a kulcsal ter vissza ha nem akkor a veszo utani ertekkel  true false
            multiple_value_dict[item["Név"]]["Darab_resz"] += 1
            multiple_value_dict[item["Név"]]["Ossz_hossz"] += item["Perc"]
        else:
            multiple_value_dict[item["Név"]] = {}
            multiple_value_dict[item["Név"]]["Darab_resz"] = 1
            multiple_value_dict[item["Név"]]["Ossz_hossz"] = item["Perc"]

    # multiple_value_dict = {
    #   'Games': {
    #       'darab_resz': 7,
    #       'ossz_hossz': 420
    #       },
    #    ...
    #  }


    with open('sum.txt','w',encoding='utf-8') as file2:
        for item in multiple_value_dict:
            print(item,"\t",multiple_value_dict[item]["Darab_resz"],"\t",multiple_value_dict[item]["Ossz_hossz"],file=file2)



adasbakerules(new_list)
megnezett_szazelek(new_list)
mennyi_idot(new_list)
adjon_egy_datumot(new_list)
vizsgalt_nap(new_list)
another_universe(new_list)













