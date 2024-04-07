import requests
import json

ico = input(f"Zadej IČO hledaného subjektu: ")

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data = response.json()
#print(data)

firma = data["obchodniJmeno"]
print(firma)
adresa = data["sidlo"]["textovaAdresa"]
print(f"{adresa}")
