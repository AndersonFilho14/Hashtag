from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://www.hashtagtreinamentos.com/cursos-hashtag-treinamentos')

#Percorrendo diferentes abas e indo de uma para outra

#Clicando no link para acessar outra aba
browser.find_element(By.XPATH,'/html/body/section[2]/div/div[6]/figure/a/img').click()

#Por padrão, o selenium permanece na mesma aba,
#para ir para uma nova pode se usar browser.switch_to.new_window, mas se for nescessario usar varias abas
#Pra saber quantas abas tem, se usa 'lista-abas = browser.window_handles' recebendo uma lista dessa variavel
print(browser.window_handles)
# Esquema para saber a posição que cada está e o nome dela 
for i in lista_abas:
    browser.switch_to.window(i)
    print(browser.title)

#E par percorrer entre elas, pode se usar 
aba_original = browser.window_handles[0]
aba_nova = browser.window_handles[1]
browser.switch_to.window(aba_nova)
browser.switch_to.window(aba_nova)

# Se já terminou oque tinha que fazer na aba e quer fechar ela, bastar dar 
browser.close()
