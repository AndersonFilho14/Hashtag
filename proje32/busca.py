from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
browser = webdriver.Chrome()

tabela = pd.read_excel(r'C:\Users\anderson.filho\Desktop\Curso python\Hashtag\proje32\buscas.xlsx') 
print(tabela)
produto=  'iphone 12 64gb'
browser.get(f'https://www.google.com.br/search?q={produto}')
 
for i in a:
    if 'Todas' == i.text:
        print('Foi')
        break
print('--')