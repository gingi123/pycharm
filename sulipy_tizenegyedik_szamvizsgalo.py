

# 1. feladat
print("1. feladat")
pleasegivemefive = ""
while len(pleasegivemefive) < 5:
    pleasegivemefive = input("Adj meg egy legalább 5 számjegyű számot.")

itspleasegivemefive = int(pleasegivemefive)

# 2. feladat
print("\n2. feladat")
if itspleasegivemefive % 5 == 0 and itspleasegivemefive % 10 == 0:
    print("Ez a szám osztható öttel és tízzel.")
else:
    print("Ez a szám NEM osztható öttel és tízzel.")

#3. feladat
print("\n3.feladat")
mother_of_earth = []
bucket = []
i_know_this_gonna_happen = []
for item in pleasegivemefive:
    mother_of_earth.append(item)
    bucket.append(item)
    i_know_this_gonna_happen.append(item)
#bucket.sort(reverse=True)     # ez volt az ahogy én oldottam meg és most utána jön ami szebb sokkal
#print(f"A szám visszafelé olvasva: {bucket}")
print(f"A szám visszafele olvasva: {pleasegivemefive[::-1]}")

print("\n4. feladat")
i_know_this_gonna_happen = [item for item in i_know_this_gonna_happen if int(item) % 2 == 0 and int(item) != 0]
i_know_this_gonna_happen.sort()

print(f"A páros számjegyek növekvő sorrendben: {i_know_this_gonna_happen}")

print("\n5. feladat")
stacked_numbers = []
for item123 in mother_of_earth:
    if mother_of_earth.count(item123) > 1 and item123 not in stacked_numbers:
        stacked_numbers.append(item123)

if stacked_numbers:
    print("Az ismétlődő számjegyek: ", ", ".join(stacked_numbers))
else:
    print("Nincsenek ismétlődő számjegyek.")


# 6. feladat

print("\n6. feladat")

for index, item in enumerate(pleasegivemefive, start=1):  # index alapból 0 val kezdődik de "start"al változtatható
    print("x",end="")
    if (len(pleasegivemefive) - index) % 3 == 0 and len(pleasegivemefive) != index:
        print(".",end="")






