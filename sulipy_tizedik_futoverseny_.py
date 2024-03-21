# 2. feladat

database = ["F5.3","NF1","F3.2","NF0.6","NF0","F2.1","NF2"]
#database = ["F5.3","NF1","F3.2","NF0.6","NF0","F2.1","NF2","F3.2","NF0.1","NF0","F6.2","NF0","NF0.2","F3.0"]
#print(database)
triplong = 0
for item1 in database:
    if item1[0] == "F":
        triplong += float(item1[1:])
    if item1[0] == "N":
        triplong += float(item1[2:])
print("2. feladat")
print(f"A verseny távja {triplong} km volt.")

#3. feladat
last_in_the_list = database[len(database)-1]

print("\n3. feladat")
if last_in_the_list[0] == "N":
    print("Gyalogolva ért célba")
else:
    print("Futva ért célba")

#4. feladat
counter = 0
print("\n4.feladat")
for item3 in database:
    if item3[0] == "N" and float(item3[2:]) == 0:
        counter += 1
print(f"A verseny során {counter} alkalommal ált meg.")

#5. feladat
print("\n5. feladat")
a = 0
h = 0
for item500 in database:              # ["F5.3","NF1","F3.2","NF0.6","NF0","F2.1","NF2"]
    if item500[0:2] == "NF":
        a = a + 1
    if item500[0:1] == "F" and a > 0:
        h = h + 1
        a = 0


print(F"A futást {h} alkalommal szakították meg.")


#6. feladat
print(F"\n6.feladat")
y = 0  # sétált
k = 0  # sétálás után nem futott
for item313 in database:
    if item313[0:2] == "NF":
        parameters = float(item313[2:])
    elif item313[0:1] == "F":
        parameters = float(item313[1:])
    if item313[0:2] == "NF" and parameters > 0:
        y=y+1
    if item313[0] == "F":
        y = 0

    if y > 0 and parameters == 0:
        k = k + 1
        y = 0

if k > 0:
    print(f"Volt olyan alkalom , hogy gyaloglás után közvetlenül megállt. {k}db ")
if k <= 0:
    print("Nem volt olyan alkalom ,hogy gyaloglás után közvetlenül megállt.")








