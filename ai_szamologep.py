def osszeadas(szam1, szam2):
    return szam1 + szam2

def kivonas(szam1, szam2):
    return szam1 - szam2

def szorzas(szam1, szam2):
    return szam1 * szam2

def osztas(szam1, szam2):
    if szam2 != 0:
        return szam1 / szam2
    else:
        return "Hibás bemenet: osztás nullával"

while True:
    print("Válasszon műveletet:")
    print("1. Összeadás")
    print("2. Kivonás")
    print("3. Szorzás")
    print("4. Osztás")
    print("5. Kilépés")

    valasztas = input("Kérem válasszon (1/2/3/4/5): ")

    if valasztas == "5":
        print("Kilépés...")
        break

    if valasztas in ("1", "2", "3", "4"):
        szam1 = float(input("Kérem az első számot: "))
        szam2 = float(input("Kérem a második számot: "))

        if valasztas == "1":
            eredmeny = osszeadas(szam1, szam2)
            muvelet = "+"
        elif valasztas == "2":
            eredmeny = kivonas(szam1, szam2)
            muvelet = "-"
        elif valasztas == "3":
            eredmeny = szorzas(szam1, szam2)
            muvelet = "*"
        elif valasztas == "4":
            eredmeny = osztas(szam1, szam2)
            muvelet = "/"

        print(f"Eredmény: {szam1} {muvelet} {szam2} = {eredmeny}")
    else:
        print("Hibás választás. Kérem válasszon újra.")