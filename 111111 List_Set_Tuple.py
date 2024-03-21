# collection = single  "variable used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set  = {} unordered and immutable , but add/remove OK. No duplicates
#  Tuple = () ordered and uncahngeable. Duplicates OK. faster

# List = rendezett és változtatható. A másolatok rendben vannak
# Set  = rendezetlen és változtathatatlan,
#        de a hozzáadás/eltávolítás OK. Nincsenek ismétlődések
#Tuple = rendezett és megváltoztathatatlan. A másolatok rendben vannak. gyorsabban

fruits = {"apple", "orange", "banana", "coconat"}


#fruits[1] = "pinneaple"  ezzel le lehet cserélni egy elemet benne
#fruits.append("pineapple")       #append:mellékel
#fruits.remove("apple")
#fruits.insert(2,"pineapple")
#fruits.reverse()
#for x in fruits:
#print(fruits.index("pinneaple"))
#print(fruits.count("pineapple"))
#print(len(fruits))


#for fruit in fruits:
    #print(fruit)
#print(dir(fruits))
#print(help(fruits))
#print(fruits[::-1])

#print(len(fruits))
#print("apple" in fruits)


def udvozles(nev):
    """Ez a funkció üdvözli a megadott nevet."""
    print(f"Üdvözöllek, {nev}!")
# Funkció meghívása
nev = input("Irja be a nevét ")
udvozles(nev)


