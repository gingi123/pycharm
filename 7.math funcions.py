import math
import random


# pi = 3.14
# x = 1
# y = 2
# z = 3
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(42))
#print(max(x,y,z))
#print(min(x,y,z))

# myTuple = ("John", "Peter", "Vicky")
#
# x = "#".join(myTuple)
#
# print(x)




def valami():
    def intersection(lista, inputo):
        list3 = [value for value in lista if value in inputo]
        return list3
    lista = []
    nemtom = input("fasztudja mit irj ide koma ")
    print(f"Ezt irtad ide {nemtom}")
    print("És most választok 5 random szamot koma (1 tő 5 ig)")
    valasztokeotszamot = set(random.sample(range(1,6),5))
    for item in valasztokeotszamot:
        baszki= str(item)
        lista.append(baszki)
    #print(f"A nyeroszamok {valasztokeotszamot}")
    indputo = input("Most hogy beirtal elöbb valamit kéne számot beírni 5 öt(de szóközzel te buta))").split(" ")

    intersection123 = intersection(lista,indputo)
    kozosesdarabja = len(intersection123)
    print(f"Megmondjam hány darabot találtá el belőlük koma? he? {kozosesdarabja}")
    print(f"Megmondajam azt is melyikek vótak? na jo {intersection123}")

    if indputo == lista:
        print(f"Dikk mindent eltaláltad ezekvótak {valasztokeotszamot}")
        print(f"oszt ezeket tippeted {indputo}")
    elif kozosesdarabja == 4:
        print(f"Dikk 4 et eltaláltá ezekvótak {valasztokeotszamot}")
        print(f"oszt ezeket tippeted {indputo}")
    elif kozosesdarabja == 3:
        print(f"Dikk 3 at eltaláltá ezekvótak {valasztokeotszamot}")
        print(f"oszt ezeket tippeted {indputo}")
    elif kozosesdarabja == 2:
        print(f"Dikk 2 őt  eltaláltá ezekvótak {valasztokeotszamot}")
        print(f"oszt ezeket tippeted {indputo}")
    elif kozosesdarabja == 1:
        print(f"Dikk 1 et  eltaláltá ezekvótak {valasztokeotszamot}")
        print(f"oszt ezeket tippeted {indputo}")
    else:
        print("Ja hát ez rád vall lófaszt nem találtá el.. hihi")

# valami1 = valami()
# print(valami1)

valami()




