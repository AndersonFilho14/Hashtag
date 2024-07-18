from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.webdriver.common.keys import Keys
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://www.investing.com/crypto/bitcoin/btc-usdt-historical-data')
 
'''sleep(2)
#alterar a data para dia 01/01/2020
browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]').click()
janela = browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]/input').send_keys('012345678')
'''
#Clicando em Dowload
# browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]').click()
#Clicando em sigin in para entrar na conta
browser.find_element(By.XPATH,'//*[@id="__next"]/header/div[1]/section/div[3]/ul/li[1]/button').click()
#Clicando no button de sig in email, para colocar os dados
browser.find_element(By.CLASS_NAME,'signup_link__0v8io').click()
# #Colocar o email e senha
browser.find_element(By.XPATH,'//*[@id=":r7:"]/form/div[3]/input').send_keys(email)
browser.find_element(By.XPATH,'/html/body/div[2]/div/div/form/div[5]/input').send_keys(senha)
browser.find_element(By.XPATH,'/html/body/div[2]/div/div/form/button').click()

browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]').click()


lista_abas = browser.window_handles
for i in lista_abas:
    browser.switch_to.window(i)
    print(browser.title, i)

browser.window_handles[0]
