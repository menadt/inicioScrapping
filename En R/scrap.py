from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://resultados.as.com/resultados/futbol/primera/clasificacion/?omnil=mpal"
page = requests.get (url)
soup = BeatifulSoup(page.content, 'html.parser')

#Equipos
eq = soup.find_all('span', class_="nombre-equipo")

print(eq)