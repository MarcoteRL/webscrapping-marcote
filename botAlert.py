import requests
from webscrapping import precioSuspFinal
from webscrapping import precioDeseado

def telegram_bot_sendtext(bot_message):  
    bot_token = '5604399517:AAE1l4-SjlgyDbWCy8MV3Sg3WosgVApe_qE'
    bot_chatID = '1325259916'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    
if precioSuspFinal <= precioDeseado:
    test = telegram_bot_sendtext(f"¡ATENCION! Hay oferta,bajo el precio! Está en: {str(precioSuspFinal) + '€'}\nEnlace: https://cutt.ly/fXzM2xi")



