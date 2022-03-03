import requests
import json
import os



cot = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cot = cot.json()

def Limpar():
    try:
        os.system('cls')
    except:
        os.system('clear')
        
def CotEuro():
    Limpar()
    cot_euro=cot['EURBRL'] #Euro
    print("--------------------------------")
    print("Cotação: {}\nEUR 1,00 equivalem a R$ {}\n\nData e Hora da Requisição (YYYY-MM-DD) (HH:MM:SS): {} ".format(cot_euro['name'],cot_euro['bid'],cot_euro['create_date'] ))

def CotDolar():
    Limpar()
    cot_dolar=cot['USDBRL'] #Dolar
    print("--------------------------------")
    print("Cotação: {}\nUS$ 1,00  equivalem a R$ {}\n\nData e Hora da Requisição (YYYY-MM-DD) (HH:MM:SS): {} ".format(cot_dolar['name'],cot_dolar['bid'],cot_dolar['create_date'] ))

def CotBit():
    Limpar()
    cot_btc=cot['BTCBRL'] #Bitcoin
    print("--------------------------------")
    print("Cotação: {}\nBTC 1,00  equivalem a R$ {}\n\nData e Hora da Requisição (YYYY-MM-DD) (HH:MM:SS): {} ".format(cot_btc['name'],cot_btc['bid'],cot_btc['create_date'] ))

def Menu():
    print("------------Cotações Monetárias------------")
    choice = int(input("Escolha uma opção\n1 - Cotação do Euro\n2 - Cotação do Dolar\n3 - Cotação do Bitcoin\nR <- "))
    if choice==1:
        CotEuro()
    elif choice==2:
        CotDolar()
    elif choice==3:
        CotBit()