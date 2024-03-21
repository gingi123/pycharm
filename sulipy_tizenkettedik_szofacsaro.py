#1. feladat
import random

words = ['alma', 'megyeszékhely', 'mozdonyvezető', 'hűtőszekrény', 'Szeged', 'görög','Anna','kék','csiga',]

random_word = random.choice(words)

#2.feladat
print(random_word)
print("\n2.feladat")
a = 0
for item1 in random_word:
    a = a + 1
if random_word[0].isupper():
    our_random_word = "Tulajdonnév"
else:
    our_random_word = "Köznév"
print(f"A szó '{our_random_word}' és {a} karakterből áll.")

#3. feladat
print("\n3.feladat")
if random_word.lower() == random_word[::-1].lower:
    print("A szó palidrom")
else:
    print("A szó NEM palidrom")

#4. feladat
print("\n4.feladat")
print("Találd ki a választott szó!")
print("Megadhatom a szó maszkját, amelyben a magánhangzók helyén csillag")
print("szerepel, pl: h*z*f*l*d*t")
print("b, Megadhatom a szót alkotó betüket, pl: fldtáiehaza")
helping = input("Milyen formában segítsek? (a/b)")
random_word_for_test = random_word.lower()
maganhangzok = "aáeéiíoóöőuúüű"
if helping == "a":
    for item3 in random_word_for_test:
        if item3 in maganhangzok:
            print("*",end="")
        else:
            print(item3,end="")
if helping == "b":
    mixed_indexes = []
    while len(mixed_indexes) != len(random_word_for_test):
        generated_index = random.randint(0, len(random_word_for_test) - 1)
        if generated_index not in mixed_indexes:
            mixed_indexes.append(generated_index)
    for item4 in mixed_indexes:  #
        print(random_word_for_test[item4],end="")
input_tipp = input("\nAdd meg a tipped!")

if input_tipp == random_word_for_test:
    print("Gratulálok, eltaláltad!")
else:
    print(f"Sajnos nem talált, a keresett szó a(z) '{random_word}' lett volna.")







