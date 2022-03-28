from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time

link_detalles = []

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
        link_detalles = []
        url = url + '?pagina=' + str(index)
        driver.get(url)

        autos = driver.find_elements(By.CLASS_NAME, 'random-vehicles__vehicle')
        for auto in autos:
            if(auto_vendido(auto, 'random-vehicles__sold') == False):
                link = auto.find_element(By.CLASS_NAME, 'random-vehicles__vehicle-link').get_attribute("href")
                link_detalles.append(link)

        for link in link_detalles:
            driver.get(link)

            modelo = driver.find_element(By.XPATH, '/html/body/form/div/div/div[1]/div[1]/div[1]/h1')

        url = 'https://veinsausados.com/buscar/'
        index += 1

def auto_vendido(object, classname):
    try:
        object.find_element(By.CLASS_NAME, classname)
    except NoSuchElementException:
        return False
    return True

search()