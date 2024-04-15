# import requests
# #import import_fajl
# def deezer_kereses(kulcsszo):
#     url = f'https://api.deezer.com/search?q={kulcsszo}'
# #    valasz = requests.get(url)
#     adatok = requests.get(url).json()
#
#     if 'data' in adatok and len(adatok['data']) > 0:
#         print(f"\nKeresési eredmények a '{kulcsszo}' kulcsszóra:")
#         for index, item in enumerate(adatok['data'],start=1):
#             cim = item['title']
#             eloado = item['artist']['name']
#             duration = item['duration']
#             linkeles = item['link']
#             print(f"{index}. {eloado} - {cim} ({duration})\t {linkeles}")
#
#             #import_fajl.kutya()
#     else:
#         print(f"Nincs találat a '{kulcsszo}' kulcsszóra.")
#
# def main():
#     print("Üdvözöllek a Deezer kereső szkriptben!")
#     kulcsszo = input("Kérem, adj meg egy keresési kulcsszót: ")
#     deezer_kereses(kulcsszo)
#
# if __name__ == "__main__":
#     main()
#
from import_fajl import Wind_dir_dict
adatok = 'E'

for key,value in Wind_dir_dict.items():
    if key == adatok:
        print(value)






#tulajdonkpekken ide barmit irhatnek







