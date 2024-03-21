menu_szovege = "Kilépéshez nyomjon 'q'-t \nFilm hozzáadáshoz nyomjon 'h'\nKereseshez nyomjon 'k'\nListázáshoz nyomjon 'l'\n"

filmek = []


with open('movies.txt','r',encoding='utf=8') as file:
    nyers_adat = file.readlines() #össze sor beolvasás egy listába, minden sor egy lista elem
    lines = nyers_adat[1:] # fejléc kihagyása
    for line in lines:
        hasitott_sorok = line.split(";") # split operátor felszabdalja a Stingedet listává egy karakter vagy szó alapján
        filmek.append({
            "cime": hasitott_sorok[0],
            "rendezo": hasitott_sorok[1],
            "evjarat": hasitott_sorok[2],
        }) # itt txt alapján tudod, hogy melyik oszlopban mi van
def hozzaad():
    cime = input("Kérem adja meg a film nevét: ")
    rendezo = input("Kérem adja meg a film rendezőjét: ")
    evjarat = input("Kérem adja meg a film megjelenési évét: ")

    filmek.append({

        "cime":cime,
        "rendezo":rendezo,
        "evjarat":evjarat


})


def kereses():
    kereses_cimre = input("Kérem adja meg a film Címét: ")

    for film in filmek:
        if film["cime"] == kereses_cimre:
            mutat(film)




def listazas():                # na ez kurva fontos és minden másik funkciónk alapja
    for film in filmek:
        mutat(film)

def mutat(film):
    print(f"Címe: {film['cime']}")
    print(f"Rendező: {film['rendezo']}")
    print(f"Évjárat: {film['evjarat']}")


def menu_1():
    valasztas = input(menu_szovege)
    while valasztas != "q":
        if valasztas == "h":
            hozzaad()
        elif valasztas == "k":
            kereses()
        elif valasztas == "l":
            listazas()
        else:
            print("Nem megfelelő menüt választott")
        valasztas = input(menu_szovege)

menu_1()

with open('movies.txt', 'w', encoding='utf=8') as file:
    file.write("cím;rendező;evjarat\n")
    for film in filmek:
        file.write(film["cime"] + ";" + film["rendezo"] + ";" + film["evjarat"] + "\n")