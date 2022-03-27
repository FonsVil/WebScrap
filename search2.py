from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Search game in Amazon
def search():
    url = 'https://www.amazon.com/s?i=videogames-intl-ship&bbn=16225016011&rh=n%3A20972781011%2Cn%3A20972797011%2Cp_89%3APlaystation&dc&language=es&fst=as%3Aoff&pf_rd_i=16225016011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=e963b29d-d654-4995-bbb2-582c8cfbb5e4&pf_rd_r=0E6CBDMYSY2Z4QW1EYKE&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1619289230&rnid=20972781011&ref=sr_nr_n_3'

    # Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        executable_path="./chromedriver", options=options)
    driver.get(url)

    time.sleep(3)

    searchTextBox = driver.find_element(By.ID, 'twotabsearchtextbox')
    print(searchTextBox.tag_name)

search()