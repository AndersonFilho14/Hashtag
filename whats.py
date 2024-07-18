import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.webdriver.common.keys import Keys
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://web.whatsapp.com/')
import urllib

contatos_df = pd.read_excel("Whats_desafio.xlsx")
print(contatos_df)

while len(browser.find_elements(By.ID,'side')) < 1:
    sleep(1)

for i, mens in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i,'Pessoa']
    numero = contatos_df.loc[i,'Número']
    texto = urllib.parse.quote(f'Oi {pessoa}! {mens}')
    link = f"https://web.whatsapp.com/send?phone={numero}$text={texto}"
    sleep(3)
    browser.get(link)
    while len(browser.find_elements(By.ID,'side')) < 1:
        sleep(1)
        browser.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
        sleep(10)
        
    browser.find_element(By.XPATH,'')
    
    
