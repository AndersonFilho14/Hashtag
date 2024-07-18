from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud')

email = '---'
senha = '--'

#clicar em dowload
browser.find_elements(By.CLASS_NAME,'sc-jMbVJB')[3].click()

#clicando em email
browser.find_element(By.XPATH,'//*[@id="site-content"]/div[2]/div/div/div[1]/form/div/div/div[1]/button[2]').click()

#Colocando o email
browser.find_elements(By.CLASS_NAME,'mdc-text-field__input')[0].send_keys(email)
#Colocando Senha
browser.find_elements(By.CLASS_NAME,'mdc-text-field__input')[1].send_keys(senha,Keys.ENTER)
#clicar em dowload
browser.find_elements(By.CLASS_NAME,'sc-jMbVJB')[2].click()


#Tirando do zip um arquivo baixado
import zipfile
with zipfile.ZipFile(r'C:\Users\anderson.filho\Downloads\archive.zip','r') as zip_ref:
    zip_ref.extractall(r'C:\Users\anderson.filho\Downloads')

#Vendo quantas das informações 
df = pd.read_csv(r'C:\Users\anderson.filho\Downloads\creditcard.csv')

# Escolha a coluna de interesse, substitua 'sua_coluna' pelo nome da coluna desejada
coluna_interesse = 'sua_coluna'

# Contar valores acima de zero e abaixo ou iguais a zero
acima_zero = (df['V7'] > 0).sum()
nao_acima_zero = (df['V7'] <= 0).sum()

print(f'Valores acima de zero: {acima_zero}')
print(f'Valores não acima de zero: {nao_acima_zero}')
