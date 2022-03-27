from asyncio.windows_events import NULL
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

        autos = driver.find_elements(By.CLASS_NAME, 'random-vehicles__vehicle')
        for auto in autos:
            # Botón para ver detalles específicos por auto
            button = auto.find_element(By.CLASS_NAME, 'button')
            button.click()
            # Búsqueda detalles
            modelo = driver.find_element(By.XPATH, '/html/body/form/div/div/div[1]/div[1]/div[1]/h1')
            print(modelo.text)




            driver.get(url)
            print(driver.current_url)

        url = 'https://veinsausados.com/buscar/'
        index += 1

search()