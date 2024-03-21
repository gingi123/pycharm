


lotto_nyeroszamok = (16,23,30,37,41)

azen_szamaim = [
    {"neve":"tábla1","számok":{18,25,28,33,37}},
    {"neve":"tábla2","számok":{9,21,35,39,47}},
    {"neve":"tábla3","számok":{9,12,25,32,39}},
    {"neve":"tábla4","számok":{13,25,27,39,42}},
    {"neve":"tábla5","számok":{13,22,28,33,42}},
    {"neve":"tábla6","számok":{7,14,28,31,44}},
    {"neve":"tábla7","számok":{9,23,27,39,47}},
    {"neve":"tábla8","számok":{9,17,29,31,39}},
    {"neve":"tábla9","számok":{7,12,25,37,44}},
    {"neve":"tábla10","számok":{6,25,28,37,44}},
]

#passzoloszamok = len(azen_szamaim["számok"])

for item in azen_szamaim:
    passzoloszamok = len(item["számok"].intersection(lotto_nyeroszamok))
    print(f"{item['neve']} eltalált  számot {passzoloszamok}")
    #print(passzoloszamok)