import requests
import time


class lehivas:

    def __init__(self, api_key):
        self.api_key = api_key
    def motor_aktualis(self,helyseg):



        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={helyseg}&aqi=no"

        adatok = requests.get(url).json()
        statusz = requests.get(url).status_code   #vagy lehetne  = adatok.status_code
        a_szel_iranya_leforditva = adatok['current']['wind_dir']
        if statusz == 200:
            print(f"\nHelység: {adatok['location']['name']}")
            print(f"Ország: {adatok['location']['country']}")
            print(f"Régió: {adatok['location']['region']}")
            print(f"Helyi idő: {adatok['location']['localtime']}\n")
            print(f"Hőmérséklet: {adatok['current']['temp_c']} Celsius.")
            print(f"Hőmérséklet: {adatok['current']['temp_f']} Fahrenheit.")
            print(f"Hőérzet: {adatok['current']['feelslike_c']} Celsius.")
            print(f"Látótávolság: {adatok['current']['vis_km']}KM.")
            print(f"Csapadék: {adatok['current']['condition']['text']} .")
            print(f"Szél: {adatok['current']['wind_kph']} km/h.")
            print(f"Szél-iránya: {adatok['current']['wind_degree']} Fok.")


            # for key, value in Wind_dir_dict.items():
            #     if adatok['current']['wind_dir'] == key:
            #         print(f"A szél irány: {value}")

            #print("Ami ez után jön lesz igen csak érdekes")
            #print(f"A szél irány: {Wind_dir_dict[adatok['current']['wind_dir']]}")
            def get_win_dir(dir): #dir == respound  : "N" vagy "NNE" ilyesmi
                base_dir = {'N': 'Észak',
                            'S': 'Dél',
                            'W': 'Nyugat',
                            'E': 'Kelet', }
                if len(dir) == 1:
                    return print(base_dir[dir].capitalize())
                if len(dir) == 2:
                    return print(base_dir[dir[0]].capitalize() + "-" + base_dir[dir[1]])
                if len(dir) == 3:
                    return print(base_dir[dir[0]].capitalize() + "-" + base_dir[dir[1]] + base_dir[dir[2]].lower())
            get_win_dir(a_szel_iranya_leforditva)


            print(f"Légnyomás: {adatok['current']['pressure_mb']} Pa.")
            print(f"Páratartalom: {adatok['current']['humidity']} %.")
            print(f"Hány % ban felhős?: {adatok['current']['cloud']} %.")
            print("\nEz a státusz kódja", statusz)

        else:
            print("Valami hiba történt nincs adat.....")
            print("\nEz a státusz kódja", statusz)


    def motor_elorejelzes(self,helyseg):
        url = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={helyseg}&days=3&aqi=no&alerts=no"
        adatok = requests.get(url).json()
        statusz = requests.get(url).status_code
        if statusz == 200:
            # első nap
            print(f'\nDátum:{adatok["forecast"]["forecastday"][0]["date"]} - MA')
            print(f'Napkelte:{adatok["forecast"]["forecastday"][0]["astro"]["sunrise"]}')
            print(f'Napnyugta:{adatok["forecast"]["forecastday"][0]["astro"]["sunset"]}')
            print(f'Holdfázis:{adatok["forecast"]["forecastday"][0]["astro"]["moon_illumination"]} %')
            print(f'Napi Min. hőmérsélet:{adatok["forecast"]["forecastday"][0]["day"]["mintemp_c"]}')
            print(f'Napi Átlag. hőmérsélet:{adatok["forecast"]["forecastday"][0]["day"]["mintemp_c"]}')
            print(f'Napi Min. hőmérsélet:{adatok["forecast"]["forecastday"][0]["day"]["avgtemp_c"]}')
            print(f'Csapadék valószínűsége:{adatok["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]} %')
            print(f'Hó valószínűsége:{adatok["forecast"]["forecastday"][0]["day"]["daily_chance_of_snow"]} %')
            print(f'Látótávolság:{adatok["forecast"]["forecastday"][0]["day"]["avgvis_km"]} km')
            print(f'Páratartalom:{adatok["forecast"]["forecastday"][0]["day"]["avghumidity"]} %\n')
            # második nap
            print(f'Dátum:{adatok["forecast"]["forecastday"][1]["date"]} - Holnap')
            print(f'Napkelte:{adatok["forecast"]["forecastday"][1]["astro"]["sunrise"]}')
            print(f'Napnyugta:{adatok["forecast"]["forecastday"][1]["astro"]["sunset"]}')
            print(f'Holdfázis:{adatok["forecast"]["forecastday"][1]["astro"]["moon_illumination"]} %')
            print(f'Napi Min. hőmérsélet:{adatok["forecast"]["forecastday"][1]["day"]["mintemp_c"]}')
            print(f'Napi Átlag. hőmérsélet:{adatok["forecast"]["forecastday"][1]["day"]["mintemp_c"]}')
            print(f'Napi Min. hőmérsélet:{adatok["forecast"]["forecastday"][1]["day"]["avgtemp_c"]}')
            print(f'Csapadék valószínűsége:{adatok["forecast"]["forecastday"][1]["day"]["daily_chance_of_rain"]} %')
            print(f'Hó valószínűsége:{adatok["forecast"]["forecastday"][1]["day"]["daily_chance_of_snow"]} %')
            print(f'Látótávolság:{adatok["forecast"]["forecastday"][1]["day"]["avgvis_km"]} km')
            print(f'Páratartalom:{adatok["forecast"]["forecastday"][1]["day"]["avghumidity"]} %\n')
            # harmadik nap
            print(f'Dátum:{adatok["forecast"]["forecastday"][2]["date"]} - Holnapután')
            print(f'Napkelte:{adatok["forecast"]["forecastday"][2]["astro"]["sunrise"]}')
            print(f'Napnyugta:{adatok["forecast"]["forecastday"][2]["astro"]["sunset"]}')
            print(f'Holdfázis:{adatok["forecast"]["forecastday"][2]["astro"]["moon_illumination"]} %')
            print(f'Napi Min. hőmérsélet:{adatok["forecast"]["forecastday"][2]["day"]["mintemp_c"]}')
            print(f'Napi Átlag. hőmérsélet:{adatok["forecast"]["forecastday"][2]["day"]["mintemp_c"]}')
            print(f'Napi Min. hőmérsélet:{adatok["forecast"]["forecastday"][2]["day"]["avgtemp_c"]}')
            print(f'Csapadék valószínűsége:{adatok["forecast"]["forecastday"][2]["day"]["daily_chance_of_rain"]} %')
            print(f'Hó valószínűsége:{adatok["forecast"]["forecastday"][2]["day"]["daily_chance_of_snow"]} %')
            print(f'Látótávolság:{adatok["forecast"]["forecastday"][2]["day"]["avgvis_km"]} km')
            print(f'Páratartalom:{adatok["forecast"]["forecastday"][2]["day"]["avghumidity"]} %\n')
            print("\nEz a státusz kódja", statusz)
        else:
            print("Valami hiba történt nincs adat.....")
            print("\nEz a státusz kódja", statusz)




class foprogram:

    @staticmethod
    def main():

        api_key = "4c4de573ae45424aab3182243240703"
        #weather_api = lehivas(api_key)  #ez egy class hivas

        lezaras = ["A","program","ezzel","bezárul","viszlát"]
        while True:
            print("Üdvözöllek a készülő API- programomban jelenleg fejlesztés alatt áll...")

            print("Válasszon menüpontot! ")
            print("Válassza 1. -est ha jelenlegi időjárást szeretné látni")
            print("Válassza 2. -est ha előrejelzést szeretné látni")
            print("Kilépéshez válassza 0. át")

            valasztas = input("-")
            if valasztas == "0":
                for item in lezaras:
                    print(item,end=" ")
                    time.sleep(0.75)
                break
            if valasztas == "1":
                helyseg = input("Időjárás API töltése folyamatban kérem adja meg a helyet (ékezetek nélkül): ")
                lehivas(api_key).motor_aktualis(helyseg)
                for item in lezaras:
                    print(item,end=" ")
                    time.sleep(0.75)
                break
            if valasztas == "2":
                helyseg = input("Időjárás API töltése folyamatban kérem adja meg a helyet (ékezetek nélkül): ")
                lehivas(api_key).motor_elorejelzes(helyseg)
                for item in lezaras:
                    print(item,end=" ")
                    time.sleep(0.75)
                break
if __name__ == '__main__':
    foprogram.main()














