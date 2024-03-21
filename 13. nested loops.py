#nested loops "inner loops


sorok = int(input("Hány sorba?: "))
oszlopok = int(input("Hány oszlopba?: "))
szimbolum = input("ird be a szimbolumot: ")

for i in range(sorok):
    print()
    for j in range(oszlopok):
        print(szimbolum, end="")