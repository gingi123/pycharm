#print("i hate gay people")

elso = float(input("Kérem adja meg az első számot "))
muvelet1 = input("Kérem adja meg a müveletet ")
masodik = float(input("Kérem adja meg a második számot "))

if muvelet1 == "*":
    print(f"Az eredmény: {elso}*{masodik}={elso * masodik}")
elif muvelet1 == "/":
    print(f"Az eredmény: {elso}/{masodik}={elso / masodik}")
elif muvelet1 == "-":
    print(f"Az eredmény: {elso}-{masodik}={elso - masodik}")
elif muvelet1 == "+":
    print((f"Az eredmény: {elso}+{masodik}={elso + masodik}"))
else:
    print("Hibás adatot adott meg")
