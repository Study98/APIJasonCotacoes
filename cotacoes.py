import requests
import json

cot = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cot = cot.json()
cot_euro=cot['EURBRL']


print("--------------------------------")
print("Cotação: {}\n1 EUR equivalem a R$ {}\n\nData e Hora da Requisição (YYYY-MM-DD) (HH:MM:SS): {} ".format(cot_euro['name'],cot_euro['bid'],cot_euro['create_date'] ))