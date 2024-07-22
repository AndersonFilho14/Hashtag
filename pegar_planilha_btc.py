from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.webdriver.common.keys import Keys
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://br.investing.com/crypto/bitcoin/historical-data')
options.add_argument('--ignore-certificate-errors')  # Exemplo de ignorar erros SSL (não recomendado para produção)

email = ''
senha = ''

#Deve descer a tela usnando o javascript
sleep(3)
browser.execute_script("window.scroll(0,500);")
#Clicando em Dowload 
sleep(3)
browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]').click()

#Clicando em sigin in para entrar na conta
sleep(3)
paragrafo = browser.find_element(By.XPATH,'//*[@id=":rb:"]/form/p[2]')
print(paragrafo)
butao = paragrafo.find_element(By.CLASS_NAME,'signup_link__0v8io').click()

# #Colocar o email e senha
browser.find_element(By.CLASS_NAME,'input_input__WivCD').send_keys(email)
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/form/div[5]/input').send_keys(senha)
browser.find_element(By.XPATH,'/html/body/div[3]/div/div/form/button').click()
'''O site não aceita o login, vou tentar'''