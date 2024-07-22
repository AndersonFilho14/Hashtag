from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from selenium.webdriver.common.keys import Keys
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)
browser.get('https://br.financas.yahoo.com/quote/BTC-USD/history/')

#Clicar o button de alterar para grafico
sleep(6)
browser.find_element(By.XPATH,'//*[@id="quote-nav"]/ul/li[2]/a').click()
#na distancia certa
sleep(2)
browser.execute_script('window.scroll(0,460);')
#determinar o intervalo
browser.find_element(By.XPATH,'//*[@id="chart-toolbar"]/div[1]/div[2]/ul/li[7]/button').click()
#Colocar o tipo de vela 
browser.find_element(By.XPATH,'//*[@id="chart-toolbar"]/div[1]/div[5]/div/span').click()
browser.find_element(By.XPATH,'//*[@id="dropdown-menu"]/div[3]/ul/li[3]/button').click()
#tirar print
sleep(3)
browser.save_screenshot('print_usando_selenium.png')

#Criar um pdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("output.pdf", pagesize=letter)

# Colocar a imagem num pdf 
from reportlab.lib.utils import ImageReader
from PIL import Image
img_path = 'print_usando_selenium.png'  
img = Image.open(img_path)
c.drawImage(ImageReader(img), 100, 500, width=img.width, height=img.height)

# e depois mandar um email

