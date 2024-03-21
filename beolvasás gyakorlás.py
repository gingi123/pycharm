#file = open('txtbeolvasni.txt','r  ',encoding='utf=8')

#for sor in file:
#    print(sor.strip())

# vagy igy is be lehet olvasni

#sor = file.readline()
#while sor:
#    print(sor.strip())
#    sor = file.readline()

#file.close()          #mindíg le kell zárni

#with open('txtbeolvasni.txt','r',encoding='utf=8') as file:

#    sor = file.readlines()   #readlines listának olvassa be
#    sor = file.read()         #beolvassa az egészet
#    print(sor)

#while sor:
#    print(sor.strip())
#    sor = file.readline()

#    for sor in file:
#        print(sor.strip())

with open('movies.txt', 'r', encoding='utf=8') as file:
    file_tartalma_szoveg = file.read()

soronkent_a_szoveg= file_tartalma_szoveg[:-1].split("\n")
lines = soronkent_a_szoveg[1:]
for line in lines:
    splitted_line = line.split(";")


    print(splitted_line)
#print(soronkent_a_szoveg1)
#print(soronkent_a_szoveg2)




