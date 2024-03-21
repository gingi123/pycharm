#keresztnev = input("Kerem a keresztnevet ")
#vezeteknev = input("Kerem a vezeteknevet ")

#print("Üdvözöllek ",keresztnev,vezeteknev)

#szamot = int(input("Kérek egy számot "))
#print("A megelőző",szamot+1)
#print("A rákövetkező",szamot-1)

szam = int(input("Kérem adjon meg egy számot "))
x = szam % 2 #maradékot vizsgaljuk pl:7 osztva 2 val maradék 1 lesz

if x == 0:
    print(f"{szam} Ez a szám páros ")
else:
    print(f"{szam} Ez a szám páratlan ")
