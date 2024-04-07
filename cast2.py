import requests
import json

nazev = input(f"Zadej nazev hledaneho subjektu: ")
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = f'{{"obchodniJmeno": "{nazev}"}}'
response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
vysledky = response.json()
celkem_pocet = vysledky["pocetCelkem"]
print(f"Celkem bylo vyhledano {celkem_pocet} subjektů s daným názvem")
subjekty = vysledky["ekonomickeSubjekty"]
for sub in subjekty:
    print(f'{sub["obchodniJmeno"]}, {sub["ico"]}')
