

kor = int(input("Ird be a korodat "))

while kor <= 0:
    print("nem lehetsz nulla éves")
    kor = int(input("Ird be a korodat"))
while not kor > 18:
        print("túl fiatal vagy lepj le")
        kor = int(input("Ird be a korodat "))

print("köszi viszlat")