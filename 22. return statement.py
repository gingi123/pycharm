#return statements = functions send python values/objects back to the caller.
#                    these values/objects are know as the functions' return value
#                 def = define  (meghatároz)
#def szorzás(number1,number2):
    #eredmény = number1 * number2
    #return eredmény

#print(szorzás(6,8))

#def szorzás(number1,number2):
    #return number1 * number2

#x = szorzás(6,8)


elso_szam = int(input("Adjon megy egy számot "))
masodik_szam = int(input("adjon meg még egy számot "))

def szorzata(elso_szam,masodik_szam):
    eredmény = elso_szam * masodik_szam
    return eredmény

a = szorzata(elso_szam,masodik_szam)

print(f"{a} Ez a kettőnek az szorzata")
