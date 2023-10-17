import requests
from bs4 import BeautifulSoup
from termcolor import colored

# URL de la página
url = "https://www.infodolar.com/cotizacion-dolar-blue.aspx"

# Realizar la solicitud GET a la página
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la respuesta
    html_content = response.text
    
    # Crear un objeto BeautifulSoup para procesar el contenido HTML
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Encontrar el elemento que contiene la fecha y hora
    fecha_element = soup.find("abbr", class_="timeago date")
    
    # Extraer la fecha y hora
    fecha = fecha_element["title"]
    
    # Encontrar los elementos que contienen los valores de compra y venta
    valores_element = soup.find_all("td", class_="colCompraVenta")
    
    # Extraer los valores de compra y venta
    compra = valores_element[0].text.strip()
    venta = valores_element[1].text.strip()
    
    # Agregar espacio entre los renglones
    print("\n")
    
    # Mostrar los datos centrados con más espacio
    print(colored("Fecha y hora:", "yellow").center(40))
    print(fecha.center(40))
    
    print("\n")
    
    print(colored("Valor de compra:", "green").center(40))
    print(compra.center(40))
    
    print("\n")
    
    print(colored("Valor de venta:", "green").center(40))
    print(venta.center(40))
    
    print("\n")
    
else:
    # Mostrar un mensaje de error si la solicitud no fue exitosa
    print("Error al obtener los datos de la página")
