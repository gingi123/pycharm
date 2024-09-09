
def bead(n):

    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    tarolo = []

    for i in range(n):
        bal_r = abc[n - 1:i:-1]    #  c,b
        jobb_h = abc[i:n]          #   a,b,c
        egesz_sor = "-".join(bal_r + jobb_h)
        kotojel = (2 * (n - 1) + 1 + 2 * (n - 1) - len(egesz_sor)) // 2#  az egyik (2 * (n - 1) betük száma  # a másik (2 * (n - 1) "-" száma
        egesz_sor = "-" * kotojel + egesz_sor + "-" * kotojel
        tarolo.append(egesz_sor)

    print("\n")

    for item1 in tarolo[::-1]:
        print(f"{item1}\n")    # javitas

    for item2 in tarolo[1:]:
        print(f"{item2}\n")    #javitas


n = int(input("Méret: ")) #(0 < n <= 26)

while n <= 0 or n >26:
    n = int(input("Méret: "))  # (0 < n <= 26)


bead(n)



#                    0                      1                   2                   3                    4
# tarolo = ['e-d-c-b-a-b-c-d-e', '--e-d-c-b-c-d-e--', '----e-d-c-d-e----', '------e-d-e------', '--------e--------']

# ----c----
# --c-b-c-- #    3        2         1        2        3
# c-b-a-b-c #abc[2] - abc[1] - abc [0] - abc[1] - abc[2]
# --c-b-c--
# ----c----

# n = 5
#
# --------e--------      len (sor ) 1
# ------e-d-e------      len (sor ) 5
# ----e-d-c-d-e----      len (sor )  9
# --e-d-c-b-c-d-e--      len (sor ) 13
# e-d-c-b-a-b-c-d-e      len (sor ) 17
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

























