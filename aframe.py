from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://pbdatatrader.com.br/jogosdodia')


sleep(7)

#fazendo o selenium ir para a tela do aframe, se usa
a = browser.find_element(By.TAG_NAME,'iframe')
browser.switch_to.frame(a)
# E para sair do aframe, basta fazer 
browser.switch_to.default_content()
