#!/usr/bin/env python3.9
from bs4 import BeautifulSoup
import telebot
import requests

url = requests.get("https://www.oscaro.es/juego-de-4-amortiguadores-muelles-koni-1120-3172-4990571-190-p?utm_source=google&utm_medium=cpc&utm_campaign=ES-Shopping-Zombie-PMax&utm_content=ES-Smart-Shopping-Zombie&utm_term=shopping-4990571&gclid=CjwKCAjwo_KXBhAaEiwA2RZ8hExKQ0RcDK-h7dHZ-bTO4pFOvx9j3pr03Yj-q5MHR4PVcf8YU4MgvBoC75oQAvD_BwE#/?vid=19911&vident=bSmUgc3VpcyBEaW9ueXNvc-NnkGH7nIvQKUeSIOTfyxrTwh3hy33oXffsiefYVP8C")

soup = BeautifulSoup(url.content, 'html.parser')
result = soup.find("p", {"class": "price"})
if result is not None:
    precioSuspEuros = result.text
precioSusp = precioSuspEuros.replace("€", "")
precioSusp2 = precioSusp.replace(",", ".")
precioSuspFinal = float(precioSusp2)
print(result.text)
precioDeseado = 385.00


bot = telebot.TeleBot('5604399517:AAE1l4-SjlgyDbWCy8MV3Sg3WosgVApe_qE', parse_mode = "None")

@bot.message_handler(commands=['help', 'start'])

def enviar(message):
    bot.reply_to(message, "Hola, soy un bot que1 te avisa cuando el precio de un producto cambia.\nPara usarme escribe /precio")

@bot.message_handler(func=lambda message: "/precio" in message.text)

def enviar_precio(message):
    bot.reply_to(message, "El precio actual es de " + str(precioSuspFinal) + "€")
    if precioSuspFinal <= precioDeseado:
        bot.reply_to(message, f"¡ATENCION! Hay oferta,bajó el precio! Está en: {str(precioSuspFinal) + '€'}\nEnlace: https://cutt.ly/fXzM2xi")
    else:
        bot.reply_to(message, f"Está muy caro aún 😢😢")

if precioSuspFinal <= precioDeseado:
    bot.send_message(1325259916, f"¡ATENCION! Hay oferta,bajó el precio! Está en: {str(precioSuspFinal) + '€'}\nEnlace: https://cutt.ly/fXzM2xi")

bot.polling()