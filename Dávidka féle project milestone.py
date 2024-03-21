def hozzaad(filmek):
    cime = input("Kérem adja meg a film nevét: ")
    rendezo = input("Kérem adja meg a film rendezőjét: ")
    evjarat = input("Kérem adja meg a film megjelenési évét: ")

    filmek.append({
        "cime": cime,
        "rendezo": rendezo,
        "evjarat": evjarat
    })


def kereses(filmek):
    kereses_cimre = input("Kérem adja meg a film Címét: ")

    for film in filmek:
        if film["cime"] == kereses_cimre:
            mutat(film)


def listazas(filmek):  # na ez kurva fontos és minden másik funkciónk alapja
    for film in filmek:
        mutat(film)


def mutat(film):
    print(f"Címe: {film['cime']}")
    print(f"Rendező: {film['rendezo']}")
    print(f"Évjárat: {film['evjarat']}")


def menu_1(filmek):
    valasztas = input(menu_szovege)
    while valasztas != "q":
        if valasztas == "h":
            hozzaad(filmek)
        elif valasztas == "k":
            kereses(filmek)
        elif valasztas == "l":
            listazas(filmek)
        else:
            print("Nem megfelelő menüt választott")
        valasztas = input(menu_szovege)


menu_szovege = "Kilépéshez nyomjon 'q'-t\nFilm hozzáadáshoz nyomjon 'h'\n kereseshez nyomjon 'k'\n listázáshoz nyomjon 'l'-t."

filmek = []
file_tartalma_szoveg = ""

with open('movies.txt', 'r', encoding='utf=8') as file:
    file_tartalma_szoveg = file.read()  # mindent beolvasunk
# itt már be van zárva a file

soronkent_a_szoveg= file_tartalma_szoveg[:-1].split("\n") #[:-1] azért van ott mert amikor kiírjuk az adatot van egy felesleges enter a végén
lines = soronkent_a_szoveg[1:]  # fejléc kihagyása
for line in lines:
    splitted_line = line.split(";")  # split operátor felszabdalja a Stingedet listává egy karakter vagy szó alapján
    filmek.append({
        "cime": splitted_line[0],
        "rendezo": splitted_line[1],
        "evjarat": splitted_line[2],
    })  # itt txt alapján tudod, hogy melyik oszlopban mi van



menu_1(filmek)

with open('movies.txt', 'w', encoding='utf=8') as file:
    file.write("cím;rendező;evjarat\n")
    for film in filmek:
        file.write(film["cime"] + ";" + film["rendezo"] + ";" + film["evjarat"] + "\n")