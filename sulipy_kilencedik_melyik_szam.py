import random



print("Egy számot kell kitalálnod 1 - és az általad megadott felső határérték között.")
insert_number = int(input("Add meg a határértéket: "))

random_number = random.randint(1,insert_number)
print(random_number)


x = 0
y = 1
while True:

    figure_it_out = int(input("\nMelyik számra gondoltam? ( kilépés -1 ) "))
    x = x+1
    if  figure_it_out == -1:
        print(f"Sajnálom A kitalálandó szám a {random_number} volt.")
        break
    elif figure_it_out != random_number:
        print("Sajnos nem talált")
        if figure_it_out < random_number:
            print("Nagyobb számra gondoltam!")
        if figure_it_out > random_number:
            print("Kisebb számra gondoltam!")
    elif figure_it_out == random_number:
        print(f"Eltaláltad {x} próbálkozásból")
        break


#szam = random.randint(1, felso_hatar)
# print(f'{szam=}')


# itt egy alternatív Rozmárral vagy Warussal megírva
#szamlalo = 1
# walrus (rozmár) operátor :=
# lehetővé teszi az értékadást és kiértékelést egy utasításon belül
#while tipp := int(input('\nMelyik számra gondoltam? (kilépés: -1) ')) != szam:
#    if tipp == -1:
#        break
#    elif tipp < szam:
#        print('Sajnos nem talált!')
#        print('Nagyobb számra gondoltam!')
#    else:
#        print('Sajnos nem talált!')
#        print('Kisebb számra gondoltam!')
#    szamlalo += 1

#if tipp == -1:
#    print(f'Sajnálom! A kitalálandó szám a {szam} volt.')
#else:
#    print(f'Eltaláltad {szamlalo} próbálkozásból!')










