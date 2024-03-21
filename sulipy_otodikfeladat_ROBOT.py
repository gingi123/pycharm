

input1 = input("Kérem a Robot parancsait: ")
E = 0
D = 0
N = 0
K = 0

for i in input1:
    if i == "E":
        E = E +1

    if i == "D":
        D = D + 1

    if i == "N":
        N = N + 1

    if i == "K":
        K = K + 1

print(f" E betűk száma: {E}")
print(f" D betűk száma: {D}")
print(f" K betűk száma: {K}")
print(f" N betűk száma: {N}")

e = 0
d = 0
k = 0
n = 0



for item in input1:
    if item == "E":
        e += 1

    if item == "D":
        d += 1

    if item == "N":
        n += 1

    if item == "K":
        k += 1

if e > d:
    direction_EK = e - d
    valtozo1 = "E"
if d > e :
    direction_EK = d - e
    valtozo1 = "D"
if k > n:
    direction_KN = k - n
    valtozo2 = "K"
if n > k:
    direction_KN = n - k
    valtozo2 = "N"


#valtozo1 = ""
#valtozo2 = ""




print(f"Egy legrövidebb út parancsa: {valtozo1*direction_EK}{valtozo2*direction_KN}")



#print(input1)
#print(3*" PINA ")
























