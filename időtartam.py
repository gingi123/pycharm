


#oramaradek = masodpercinput % 3600 # ezzel megkapom masodpercek ora fölött részét
#percmaradek = oramaradek % 60 # ezzel megkapom percek fölötti másodperceket
#percmaradek = masodperc

def seconds_mat():
    resthours = secondinput % 3600  # ezzel megkapom masodpercek ora fölött részét
    seconds = resthours % 60
    return seconds
def minutes_mat():
    resthours = secondinput % 3600
    minutes = resthours / 60
    return minutes

def hours_mat():
    hours = secondinput / 3600
    return hours

def inputo_():
    masodpercek = secondinput
    return masodpercek
def printing():
    hours = int(hours_mat())
    minutes = int(minutes_mat())
    seconds = int(seconds_mat())
    comesecounds = int(inputo_())
    print(f"{comesecounds} másodperc a(z) {hours} óra {minutes} perc, és {seconds} másodperc.")

while True:
    secondinput = int(input("Kérem adja meg az időt másodpercben: "))

    printing()

#print(int(hours_mat()))
#print(int(minutes_mat()))
#print(int(seconds_mat()))
# így csináltam és és most lássuk ai hogy csinálta lejjeb

#def idotartam_atalakitas(masodpercek):
#    ora = masodpercek // 3600
#    masodpercek = masodpercek % 3600
#    perc = masodpercek // 60
#    masodperc = masodpercek % 60
#    return ora, perc, masodperc

#masodpercek = int(input("Kérem adja meg az időtartamot másodpercekben: "))
#ora, perc, masodperc = idotartam_atalakitas(masodpercek)

#print(f"{masodpercek} másodperc az {ora} óra, {perc} perc, és {masodperc} másodperc.")