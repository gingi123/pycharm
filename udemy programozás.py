


#szoveg1 = 13//5
#print(szoveg1)
#szoveg2 = 13/5
#print(szoveg2)
#szoveg3 = 12%5
#print(szoveg3)

#name = "Rolf Smith"
#street = "123 No Name Road"
#postcode = "PY10 1CP"

#address = f"""Name: {name}
#Street: {street}
#Postcode: {postcode}
#Country: United Kingdom"""

#print(address)


#description = "{} is {} years old."
#print(description.format("Bob",30))

#description = "{} is {age} years old."
#print(description.format("Bob", age=30))
#name = "jose"
#name1 = f"Hello, {name}"
#print(name1)

#bekeres = int(input("Give me your age: "))
#print(f"Your are {bekeres*12} mounth old.")

#friends = ["rolf","bob","anne"]
#friends.append("Jen")

#print(friends)

#friends = {"rolf","bob","anne"}
#friends.add("Jen")
#print(friendsnevkere)

#nearby_people = {'Rolf', 'Jen', 'Anna'}
#user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend

# Add the name to the empty set

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.

#nevkeres = input("Please give me your friend name: ")

#user_friends.add(nevkeres)

#kozosek = nearby_people.intersection(user_friends)

#print(kozosek)


#lista = [33,44,12,120,70]

#osszes = sum(lista)
#darab = len(lista)
#print(osszes/darab)

#lottery_numbers = {13, 21, 22, 5, 8}
#faszomat = len(lottery_numbers)
#players =[
    #{"name" : "john",
     #"numbers":{13,44,22,5,9}},
    #{"name" : "Amber",
     #"numbers" : {22,5,8,14,15}}
#]
#jatekos1neve = players[0]["name"]
#jatekor1szamai = players[0]["numbers"]
#jatekos2neve = players[1]["name"]
#jatekos2szamai = players[1]["numbers"]
#osszesitettszamokjatekos1 = players[0]["numbers"].intersection(lottery_numbers)
#osszesitettszamokjatekos2 = players[1]["numbers"].intersection(lottery_numbers)
#print(f"{jatekos1neve} got {len(osszesitettszamokjatekos1)} number right and these are: {osszesitettszamokjatekos1}")
#print(f"{jatekos2neve} got {len(osszesitettszamokjatekos2)} number right and these are: {osszesitettszamokjatekos2}")


#friends = ["rolf","anna","charlie"]
#szepnyomtatas =", ".join(friends)
#print(friends)
#print(szepnyomtatas)
#print(f"Az én barátaim: {szepnyomtatas}")


#if user_name != friends:
    #print("hello friend")



#user_input = input("Please choose (p : q)? ")

#while user_input != "q":
    #print("Hello")
    #user_input = input("Please choose (p : q)? ")  # ez eddig szar ez a nagy nulla
    #if user_input == "p":
        #print("Hello2")
    #user_input = input("Please choose (p : q)? ")  #<-----------

#user_input = input("Enter q or p: ")

#while user_input != "q":

    #if user_input == "p":
        #print("Hello")
    #user_input = input("Enter q or p: ")


#user_input = input("Adjon meg egy betüt p vagy q vagy más nyilván")
#print("Ez egyszer fut le program indulásonként, soha többé nem fog ez kiírodni")
#while user_input != "q":  # ha alapból q-t adtunk meg a while ba bele se lép
#    print("A user_input nem q volt ezért ez lefut")
#    if user_input == "p":
#        print("A user input p volt ezért kiirjuk hogy ez pé")
#   if user_input == "z":
#        print("egyébként ezt is megnézhetjük ez sem befolyásolja hogy kilép e a while ból mert while on belül vagyunk")
#   print(
#       "Ez fut le azután hogy megvizsgáltuk hogy p e az input, ha p akkor ez elött ki van irva hogy ez p ha nem p akkor nem irtuk ki hogy p")
#
#   user_input = input("Itt bekérünk megint egy betüt hogy hátha most végre q vagy p lesz")
#   print("Ettől függetlenül ez tovább fog menni és ez is itt le fog futni, mert a whileon belül vagyunk még mindig")
#print(
#    "Itt kint vagyunk már a while ból mert kijebb vagyunk, ez a szöveg akkor és csak akkor fog kiírodni ha a user input q. mivel addig nem tudunk kilépni a while ciklusból")


#students = [
#    {"name" : "Rolf" , "grade" : 90},
#    {"name" : "bob" , "grade" : 78},
#    {"name" : "jen" , "grade" : 100},
#    {"name" : "anna" , "grade" : 80},
#]

#for i in students:
#    name = i["name"]
#    grade =i["grade"]
#    print(f"{name} {grade}")

#currencies = 0.8, 1.2  #distructuring
#usd, eur = currencies

#friends_tubles = [("rolf",25),("anne",37),("charlie",32),("bob",21)]
#friends_dictionaries = {"rolf" : 25,"anne" : 37, "charlie" :32 ,"bob" : 21}

#for name,age in friends:
#    print(name,age)
#for name, age in friends:
#    print(f"{name} is {age} years old")

#for name,age in friends_dictionaries.items():
#    print(name,age)
#for name in friends_dictionaries.values():
#    print(name)

#cars = ["ok1","ok2","ok3","ok4","faulty","ok5","ok6"]

#for i in cars:
#    if i == "faulty":
#        print("Found faulty car, skipping .....")
#        break                                      #break megállitja continue folytatja
#    print(f"This car is {i}")
#    print("Shipping new car to customer!")
#else:
#    print("All cars was built successfully. no faulty cars")




#for i in range(1,100):
#    osztva1 = i % 3
#    osztva2 = i % 5
#    osztva3 = (osztva1,osztva2)
#    if osztva1 == 0 and osztva2 == 0:
#        print("Fizzbuzz")
#    elif osztva1 == 0:
#        print("fizz")
#    elif osztva2 == 0:
#       print("buzz")
#    else:
#        print(i)

#for i in range(2,10):
#    for x in range(2,i):
#        if i % x ==0:
#            print(f"{i} egyenlo {x} * {i//x}")
#           break
#   else:
#       print(f"{i} ez egy prím szám")

#számok = [1,2,3,4,5,6,7,8,9,10]
#double_numbers = []

#for i in numbers:
    #double_numbers.append(i*2)

# ami ez után jön ugyan az csak lerövidítve
#double_numbers = [5 for i in számok]
#double_numbers = [i * 2 for i in range(1,10)]

#print(double_numbers)


#friends_ages = [22,31,35,37]
#age_strings = [f"my friends is {age}years old."for age in friends_ages]
#age_strings = [f"my friends is {age}years old."]
#for age in friends_ages:
#print(age_strings)


#name = ["rolf","bob","anna"]
#lower = [i.lower() for i in name]

#print(lower)

#friend = input("Enter your name: ")
#friends = ["Rolf","bob","jen","charlie","anne"]
#frends_lower = [name.lower()for name in friends]

#if friend.lower()  in friends_lower:
    #print(f"{friend.title()} is on of your friends")

#ages = [22,35,27,21,20]
#odds = [i for i in ages if i % 2 == 1]

# vagy lehet úgy is hogy

#ages = [22, 35, 27, 21, 20]

#odds = []
#for i in ages:
    #if i % 2 == 1:
        #odds.append(i)


#print(odds)

#friends = ["Rolf","ruth","charlie","Jen"]
#guests = ["jose","Bob","Rolf","Charlie","michael"]

#friends_lower = [f.lower() for f in friends]

##    name.title() for name in guests if name.lower()in friends_lower
#]

#print(present_friends)

#friends = ["Rolf","Bob","Jen","Anne"]
#time_since_seen = [3,7,15,11]

#long_timers = dict(zip(friends, time_since_seen))
#print(long_timers)



#friends = ["Rolf","John","Anna"]

#index = 0

#for i in friends:
    #print(index)
    #print(i)
    #index = index + 1

#for index,i in enumerate(friends):

    #print(index)
    #print(i)

#print(list(enumerate(friends)))

#numbers = list(range(10))
#doubled = [n*2 for n in numbers]
##import random

#lottery_numbers = set(random.sample(list(range(22)),6))
#winnings = 100 ** len(numbers_matched)
#players = [
#    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
#    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
#    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
#    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}}
#]

#for i in players:
 #   print(i["name"])
#    print(i["numbers"])

#print(f"Ezek a nyerőszámok: {lottery_numbers}")


#top_player = players[0]
#print(top_player)
#for i in players:
#    matched_numbers = len(i["numbers"].intersection(lottery_numbers))

#if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):
 #       top_player = i

#    winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))

#    print(f"{top_player['name']} won {winnings}.")


#garazs = [
#    {"name": "audi","csomagtarto": "drogok", "kesztyütarto":"kulcsok"},
 #   {"name": "vw", "csomagtarto": "kurvák", "kesztyütarto":"hdd"},
#    {"name": "lada","csomagtarto": "műtrágya", "kesztyütarto":"füles"},
#    {"name": "merci", "csomagtarto": "ruhák", "kesztyütarto":"bögre"},
#]

#for auto in garazs:
#    if  auto["name"] == "audi":
#        print("Az audit kihagyjuk")
 #   else:
 #       print(f"A {auto['name']} nevű autónak a csomagtartójában egy: {auto['csomagtarto']}van(nak))!")



#def greet():
#    name = input("Enter your name: ")
#    print(f"Hello,{name}!")

#greet()
#car = {
#    "make": "Ford",
#    "model": "Fiesta",
#    "mileage": 23000,
#    "fuel_consumed": 4600
#}
#cars = [
#    {"make": "Ford","model":"Fiesta","mileage":23000,"fuel_consumed":460},
#    {"make": "Ford","model":"Focus","mileage":17000,"fuel_consumed":350},
#    {"make": "Mazda","model":"MX-5","mileage":49000,"fuel_consumed":900},
#    {"make": "Mini","model":"Cooper","mileage":31000,"fuel_consumed":235},
#]
#def calculate_mpg(car_to_calculate):     #parameter
#    mpg = car_to_calculate["mileage"]/car_to_calculate["fuel_consumed"]
#   name =f"{car_to_calculate['make']} {car_to_calculate['model']}"
#    print(f"{name} does {mpg} miles per gallon")

#calculate_mpg(cars[2])      #argument value
#for item in cars:
    #print("most meghivjuk a szamitast")
#calculate_mpg(cars[0])
    #print(item)

#cars = [
#    {"make": "Ford","model":"Fiesta","mileage":23000,"fuel_consumed":460},
#    {"make": "Ford","model":"Focus","mileage":17000,"fuel_consumed":350},
#    {"make": "Mazda","model":"MX-5","mileage":49000,"fuel_consumed":900},
#    {"make": "Mini","model":"Cooper","mileage":31000,"fuel_consumed":235},
#]
#def calculate_mpg(item):     #parameter
#    mpg = item["mileage"]/item["fuel_consumed"]
#    return mpg

#def car_name(item):
#    name =f"{item['make']} {item['model']}"
#    return name
#def print_car_info(item,intro):
#    print(intro)
#    name = car_name(item)
#    mpg  = calculate_mpg(item)

#    print(f"{name} does {mpg} miles per gallon")

#for item in cars:
#    print_car_info(item,"Ezt mindenhova kiirja a loop miatt?")  #de ha return lenne print_car_infoba akkor mpg = print_car_info(item)



#def atlag(sorrend):
#   return sum(sorrend)/len(sorrend)

#students =[
#    {"name":"Rolf","grade":(67,90,95,10)},
#    {"name":"Bob","grade": (56,78,80,90)},
#    {"name":"Jen","grade": (98,90,95,99)},
#    {"name":"Anne","grade":(100,100,95,100)}
#]

#for item in students:
#    print(atlag(item["grade"]))


#def greet():
    #print("Hello")

#hello = greet

#hello()

def average(seq):
    return sum(seq) / len(seq)

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda  seq: max(seq)

muveletek = {
    "average":avg,
    "total":total,
    "top":top
}

students =[
    {"name":"Rolf","grade":(67,90,95,10)},
    {"name":"Bob","grade": (56,78,80,90)},
    {"name":"Jen","grade": (98,90,95,99)},
    {"name":"Anne","grade":(100,100,95,100)}
]

for item in students:
    name = item["name"]
    grades = item["grade"]

    print(f"Student: {name}")
    bevitel = input("Enter 'average', 'total', or 'top': ")


    muveleti_funkciok = muveletek[bevitel]
    print(muveleti_funkciok(grades))

    if bevitel == "average":
        print(avg(grades))
    elif bevitel == "total":
        print(total(grades))
    elif bevitel == "top":
        print(top(grades))


#my_students = {
#    "name":"Rolf smith",
#    "grades":[70,88,90,99],
#    "average": None
#}


#def avg(student):
#    return  sum(student['grades'])/len(student["grades"])

#class Student:
#    def __init__(self, new_name, new_grades):
#        self.name = new_name
#        self.grades = new_grades

#    def average(self):
#        return sum(self.grades) / len(self.grades)

#student_one = Student("Rolf smith",[70,88,90,99])

#print(student_one.name)











