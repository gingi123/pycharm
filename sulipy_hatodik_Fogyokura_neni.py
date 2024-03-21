
weeks = []
insect_weigh = float(input("Elérni kívánt testtömeg?: "))
insect_weeks = int(input("Hány héten át tartott a fogyókúra?: "))
print(f"Hetek száma: {insect_weeks}")
print(f"Elérni Kívánt testtömeg(kg) = {insect_weigh}")
insect_weeks1 = insect_weeks+1
x = 1
for i in range(insect_weeks1):
    if x == i:
        x=x+1
        week = float(input(f"Tömege a {i} héten mennyi volt?"))
        weeks.append(week)
#weeks = [95.5,94.3,94.4,93.3,93.8,92.9]   #95.5,94.3,94.4,93.3,93.8,92.9
y = 0
z = 10000
a = 0

for item in range(len(weeks)):
    if weeks[item] <= insect_weigh:
        y=y+1
        break
for item in range(len(weeks)):
    if weeks[item] > z:
        a = a+1
    z = weeks[item]
if y != 0:
    print(f"Mari néni a {item+1}. héten elérte a célt.")
if y == 0:
    print("Mari néni nem érte el a célját!")

if a != 0:
    print(f"A tömege {a} esetben nőtt egyik hétről a másikra.")
else:
    print("A tömege nem nőtt egyik hétről a másikra.")
#print(weeks)












