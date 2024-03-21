def input_and_countgools_plus_giveit_to_list(insert_howmany_round):   # Feladat 2 nek a fele
    y = 0
    for item in range(insert_howmany_round):
        y = y + 1
        wooden_legs = int(input(f"Falábuak gólja? A(z) {y}. fordulóban (db):"))
        enemy_balfasz = int(input(f"Ellenfel gólja? A(z) {y}. fordulóban (db):"))
        gool_diff = wooden_legs - enemy_balfasz
        gools.append(gool_diff)

def counting_the_gool_diff_i_think(insert_howmany_round):       # feladat 2 nek a másik fele
    x = 0
    z = 0
    for item in range(insert_howmany_round):
        x = x + 1
        if x <= insert_howmany_round:
            print(f"{x}. Fordulóban a gólkülönbség: {gools[z]}")
        z = z + 1

def Winning_i_think_bich(gools):
    a = 0
    for item in gools:
        if item > 0:
            a = a + 1

    return a

def LOOOSING_MTF(gools):
    a = 0
    for item in gools:
        if item < 0:
            a = a + 1

    return a

def Equal_what_a_bicth(gools):
    a = 0
    for item in gools:
        if item == 0:
            a = a + 1

    return a

def points_Bitch(gools):
    for item in gools:
        if item > 0:
            x = 3
            points.append(x)
        if item == 0:
            x = 1
            points.append(x)



def WIN_LOSE_EQUAL_PRINT(gools):
    win = Winning_i_think_bich(gools)
    lose = LOOOSING_MTF(gools)
    equal = Equal_what_a_bicth(gools)
    print(f"A szezonban a csapatnak {win} győzelme, {lose} versége, {equal} döntetlen volt.")
def summer_(points):
    points_for_win = sum(points)
    print(f"A szezonban a csapatnak összesen {points_for_win} pontja lett.")

def more_lose_or_win(gools):
    for gol in gools:
        a = 1
        if gol > 0:
            wins.append(a)

        if gol < 0:
            lose.append(a)

        if gol == 0:
            equal.append(a)

    if len(wins) > len(lose)+len(equal):
        print("A csapatnak többe győztes mérkőzése volt, mint veresége és dönbtetlen együttvéve")
    else:
        print("A csapatnak nem volt több győztes mérkőzése, mint veresége és döntetlen együttvéve")

def our_big_dream_with_gools(gools):
    z = 1000000000000000000000000000
    dream = 0
    for item in gools:
        if item > z and item > 0:
            dream = dream +1
        if item > 0:
            z = item
    if dream >= 0:
        print(f"A kitűzött célt {dream} alkalommal sikerült elérni.")


gools = []
points = []
wins = []
lose = []
equal = []


insert_howmany_round = int(input("Hány forduló volt a szenzonban?: ")) # Feladat 1.
print(f"Fordulók száma: {insert_howmany_round}")  # Feladat 1.
input_and_countgools_plus_giveit_to_list(insert_howmany_round)
counting_the_gool_diff_i_think(insert_howmany_round)
WIN_LOSE_EQUAL_PRINT(gools)
points_Bitch(gools)
summer_(points)
more_lose_or_win(gools)
our_big_dream_with_gools(gools)


#print(*gools)
#print(*points)
#print(sum(points))






















