from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)


'''seleção de elementos
browser.find_element Retorna um elemento
browser.find_elements Retorna uma lista

'''
url = 'https://www.detran.pe.gov.br/'
browser.get(url)

'''Buscando pelo id é 
browser.find_element(By.ID,'o nome do id em sem colocar espaço entre eles') 
No exemplo em baixo eu entrei no site do dentran e cliclei no buton   
browser.find_element(By.ID,'btn-two').click()     '''

'''Buscando pela classname
browser.find_element(By.CLASS_NAME,'Nome da classe. lembrando, apagar o espaço dela ')
browser.find_element(By.CLASS_NAME,'nav-link').click()      '''

'''Buscando pelo xpath
sendo mais facil de ser mudado que as buscas acima respectivamente
browser.find_element(By.XPATH,'//*[@id="btn-two"]').click()'''

'''----------------- Metodo de busca menos recomendados ----------------------

Buscandp pela tag para pegar oque esta no site
print(browser.find_element(By.TAG_NAME,'h2').text)
'''

'''Se eu quiser puxar pelo link do site, pode utlizar o link texto. 
Ou se eu ti tiver apenas um link que não conhce, se pega pelo PARTIAL_LINK
browser.find_element(By.PARTIAL_LINK_TEXT,'Pernanbuco').text'''