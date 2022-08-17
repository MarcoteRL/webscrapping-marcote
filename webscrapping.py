#!/usr/bin/python3.9
from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://www.oscaro.es/juego-de-4-amortiguadores-muelles-koni-1120-3172-4990571-190-p?utm_source=google&utm_medium=cpc&utm_campaign=ES-Shopping-Zombie-PMax&utm_content=ES-Smart-Shopping-Zombie&utm_term=shopping-4990571&gclid=CjwKCAjwo_KXBhAaEiwA2RZ8hExKQ0RcDK-h7dHZ-bTO4pFOvx9j3pr03Yj-q5MHR4PVcf8YU4MgvBoC75oQAvD_BwE#/?vid=19911&vident=bSmUgc3VpcyBEaW9ueXNvc-NnkGH7nIvQKUeSIOTfyxrTwh3hy33oXffsiefYVP8C")

soup = BeautifulSoup(url.content, 'html.parser')
result = soup.find("p", {"class": "price"})
precioSuspEuros = result.text
precioSusp = precioSuspEuros.replace("€", "")
precioSusp2 = precioSusp.replace(",", ".")
precioSuspFinal = float(precioSusp2)

precioDeseado = 385
