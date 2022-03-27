from tarfile import LENGTH_NAME
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Search game in Amazon
def search():
    url = 'https://veinsausados.com/buscar/'

    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        executable_path="./chromedriver", options=options)
    driver.get(url)

    time.sleep(3)

    # Cantidad de páginas
    paginacion = driver.find_elements(By.CLASS_NAME, 'search-box__page-number')
    
    # Navegar entre páginas
    index = 1
    while index <= len(paginacion):
        url = url + '?pagina=' + str(index)
        driver.get(url)

        prueba = driver.find_element(By.CLASS_NAME, 'random-vehicles__vehicle')
        print(prueba)

        index += 1

search()