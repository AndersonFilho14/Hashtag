from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://the-internet.herokuapp.com/context_menu')

''' Quando aparecer um alerta,'pop up'. mandara esse codigo que fara o navegador acessar o alerta 
alerta = browser.switch_to.alert
coloando o alerta.accept, para aceitar ou o alerta.dismiss para recusar '''

'''Para pegar a informação de um elemento usasse essse três parametros
.text 
.get_attribute("value") -- Serve para saber qual valor e preenchido, Ele é usado para localizar a lista de WebElements filhos correspondentes dentro do contexto do elemento pai
.is_selected -- usado pra saber se o  button está selecionado 
'''



