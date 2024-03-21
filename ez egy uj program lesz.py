#def osztas (szam1,szam2):
#    eredmeny= szam1/szam2
#    printeredmeny = print(f"{szam1} / {szam2} = {eredmeny}")
#    return printeredmeny


#szam1 = 30
#szam2 = 10

#osztas(szam1,szam2)

#osztas(30,10)

#def osztas(x,y):
    #return x/y         # ez ugyan az mint alatta a lambda return fontos

#osztas = lambda x, y: x / y   #ha nem definiális szal osztas= akkor eltűnik
         #(lambda x, y: x / y)(30,2) # igy is lehet írni ez is ugyan az

#print(osztas(30,2))


def atlag(sorrend):
    return sum(sorrend)/len(sorrend)

students =[
    {"name":"Rolf","grade": {67,90,95,10}},
    {"name":"Bob","grade": {56,78,80,90}},
    {"name":"Jen","grade": {98,90,95,99}},
    {"name":"Anne","grade": {100,100,95,100}}
]
legjobb = students[0]["grade"]
legjobbatlaga = sum(legjobb)/len(legjobb)
#print(legjobbatlaga)
#print(legjobb)
for item in students:
    szamitas = (atlag(item["grade"]))
    if szamitas > legjobbatlaga:
        legjobb = item
        #legjobbatlaga < (atlag(item['grade'])):
        #legjobbatlaga = item



#print(legjobbatlaga)
print(f"Ez a legjobb tanulo {legjobb['name']} ezzel az átlaggal {atlag(legjobb['grade'])}")

