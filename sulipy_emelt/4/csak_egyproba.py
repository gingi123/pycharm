# from pprint import pprint
# poba1 = []
# poba2 = []
# poba3 = []
# with open('utca.txt','r',encoding='utf-8') as file:
#     adok = file.readline().strip().split(" ")
#     adosavok = {'A': int(adok[0]), 'B': int(adok[1]), 'C': int(adok[2])}
#     print(adosavok)
#     for sor in file:
#         adatok = sor.strip().split(" ")
#         epitmeny = {'adoszam': adatok[0],
#                     'utca': adatok[1],
#                     'hazszam': adatok[2],
#                     'adosav': adatok[3],
#                     'terulet': int(adatok[4])}
#         poba3.append(epitmeny)
#     # for item in file:
#     #     filereadtin = item.strip().split(" ")
#     #     poba2.append(item)
#     #     tarolo = []
#     #     for item in filereadtin:
#     #         tarolo.append(item)
#     #         if len(tarolo) == 3:
#     #             poba3.append(tarolo)
#     #             tarolo = []
# #print(filein)
# # print(poba1)
# # print(poba2)
# print(poba3)

nagy_halmaz = []
for index in range(szamlalo):

    if lako_adatok[index][3] == "A" and lako_adatok[index] not in ado_lebontva_lakokra:
        halmaz1 = []
        A_adomerteke = ado(A_szorzo,int(lako_adatok[index][4]))
        halmaz1.append(lako_adatok[index][1])
        halmaz1.append(A_adomerteke + int(lako_adatok[index]))
        nagy_halmaz.append.(halmaz1)
        halmaz1 = []
    else:
        A_adomerteke = ado(A_szorzo, int(lako_adatok[index][4]))
        lako_adatok[index][]


    if lako_adatok[index][3] == "B":
        halmaz2 = []
        B_adomerteke = ado(B_szorzo, int(lako_adatok[index][4]))
        ado_lebontva_lakokra.append({
            "ADOSZAM": lako_adatok[index][0],
            "ÖSSZADO": B_adomerteke})


    if lako_adatok[index][3] == "C":
        halmaz3 = []
        C_adomerteke = ado(C_szorzo, int(lako_adatok[index][4]))
        ado_lebontva_lakokra.append({
            "ADOSZAM": lako_adatok[index][0],
            "ÖSSZADO": C_adomerteke})





ado_tulajdonosonkent = {}
    for epitmeny in epitmenyek:
        if epitmeny['adoszam'] in ado_tulajdonosonkent:
            ado_tulajdonosonkent[epitmeny['adoszam']] += ado(adosavok, epitmeny['adosav'], epitmeny['terulet'])
        else:
            ado_tulajdonosonkent[epitmeny['adoszam']] = ado(adosavok, epitmeny['adosav'], epitmeny['terulet'])





