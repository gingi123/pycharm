import math

bevitel = int(input("Kérem adjon megy egy számot: "))
#bevitel =  3
y = math.sqrt(bevitel)
x = isinstance(y, int)
print(y)

#x= math.sqrt(bevitel)
#y = x % 1
def fut_program():
    while True:
    if  x == True or bevitel==1:
        print("Ez négyzetszám ")
    elif x == False:
        print("Ez NEM négyzetszám ")
    #elif bevitel / 4 != 0 and bevitel % 4 != 1:
    #else:
        #print("Ez NEM négyzetszám")
    bevitel = int(input("Kérem adjon megy egy számot: "))
fut_program()

      #and bevitel % 4 == 1