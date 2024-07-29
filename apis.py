import requests
import json
#Pegando a biblioteca geral da cotações das moedas
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()
print(cotacoes_dic['USD'])

# Fazendo uma lista
dias = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dias = dias.json()
print(cotacoes_dias[2]['bid'])
lista_cotaçoes_dolar = [i['bid'] for i in cotacoes_dias]
print(lista_cotaçoes_dolar)

#Api para mandar SMS, mas com credencial, usando o twilio



