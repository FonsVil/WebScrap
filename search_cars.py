from bs4 import BeautifulSoup
import requests

def search():
    url_page = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'

    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, "lxml")
	
    # Obtenemos la tabla por un ID específico
    tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})
    print(tabla)


search()