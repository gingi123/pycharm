def idotartam_atalakitas(masodpercek):
    ora = masodpercek // 3600
    masodpercek = masodpercek % 3600
    perc = masodpercek // 60
    masodperc = masodpercek % 60
    return ora, perc, masodperc

masodpercek = int(input("Kérem adja meg az időtartamot másodpercekben: "))
ora, perc, masodperc = idotartam_atalakitas(masodpercek)

print(f"{masodpercek} másodperc az {ora} óra, {perc} perc, és {masodperc} másodperc.")