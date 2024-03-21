#name ="Krisztian "

#print(len(name)
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("i"))
#print(name.replace("i","az"))
#print(name* 3)

oldal1 = int(input("Kérem adja meg az első oldal méretét: "))
oldal2 = int(input("Kérem adja meg az második oldal méretét: "))
oldal3 = int(input("Kérem adja meg az harmadik oldal méretét: "))

if (oldal1 + oldal2 > oldal3) or (oldal2 + oldal3 > oldal1) or (oldal1 + oldal3 > oldal2):
    print(f"Ezekkel az oldalakkal lehet háromszöget szerkeszteni: {oldal1}, {oldal2}, {oldal3}")
else:
    print(f"Ezekkel az oldalakkal nem lehet háromszöget szerkeszteni: {oldal1}, {oldal2}, {oldal3}")