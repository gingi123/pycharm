carakters = []
print("1. feladat")
its_the_text = input("Add meg a mondatot! ") #Melyik a leghosszabb szo?

print("\n 2. feladat")
b = 0
for i in its_the_text:
    if b == 0:
        carakters.append(i)
for item in carakters:
    if item == " " or item == "!" or item == "?" or item == "." or item== ";" or item== ",":
        carakters.remove(item)


len_sentence = len(carakters)
print(f"A Mondatban előforduló betűk száma: {len_sentence} ")

formating = its_the_text.lower().split(' ')
formating2 = its_the_text.lower()[:-1]
format_len = len(formating)
print("\n 3. feladat")
print(f"A szavak száma: {format_len}")

print("\n 4. feladat")
maganhangzok = []

for item2 in carakters:
    if item2 == "a" or item2 == "e" or item2 == "i" or item2 == "o" or item2 == "u":
        maganhangzok.append(item2)

maganhangzok_len = len(maganhangzok)
print(f"A mondatban előforduló magánhangzók száma: {maganhangzok_len}")

print("\n 5. feladat")
it_is_formated = its_the_text[:-1].split(" ")
max_leng = ""
x = 0
for item3 in it_is_formated:
    if x < len(item3):
        x = len(item3)
        max_leng = item3
print(f'A leghosszab szó a(z) "{max_leng}" {x} betűből áll.')

#print(formating)
print("\n 6. feladat")
search_and_destroy = input("Add meg a keresett szó. ")
search_and_destroy1 = search_and_destroy.lower()
if search_and_destroy1 in formating2:
    print("A keresett szó előfordul a mondatban.")
else:
    print("A keresett szó nem fordul elő a mondatban.")


print("\n \n \n Leszophat a feladat BTW csak úgy mondom.......")


print(formating2)
print(carakters)









