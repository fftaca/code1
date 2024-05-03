import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

# Func para obtener los datos de la pag y mostrarlos en la ventana
def obtener_datos():
    global contador  # Declaramos contador como global
    contador += 1  # Incrementamos el contador
    txt_contador.delete(0, tk.END)  # Borramos el contenido actual del Entry
    txt_contador.insert(0, contador)  # Insertamos el nuevo valor del contador
    
    # codigo para obtener los datos de la pagina y mostrarlos
    url = "https://www.infodolar.com/cotizacion-dolar-blue.aspx"

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        fecha_element = soup.find("abbr", class_="timeago date")
        fecha = fecha_element["title"]

        valores_element = soup.find_all("td", class_="colCompraVenta")
        compra = valores_element[0].text.strip()
        venta = valores_element[1].text.strip()

        lbl_fecha.config(text=fecha)
        lbl_compra.config(text=compra)
        lbl_venta.config(text=venta)

    else:
        lbl_fecha.config(text="Error al obtener los datos")
        lbl_compra.config(text="")
        lbl_venta.config(text="")

# Crear ventana de Tkinter
root = tk.Tk()
root.title("Cotización del Dólar Blue Actual")


ancho_ventana = 345
alto_ventana = 320
root.geometry(f"{ancho_ventana}x{alto_ventana}")


style = ttk.Style()
style.configure("Boton.TButton", background="red", foreground="black")


lbl_fecha = ttk.Label(root, text="", font=("Arial", 12, "bold"), justify="center")
lbl_compra = ttk.Label(root, text="", font=("Arial", 12))
lbl_venta = ttk.Label(root, text="", font=("Arial", 12))


lbl_fecha.pack(pady=10)
lbl_compra.pack(pady=10)
lbl_venta.pack(pady=10)


# Agreg un Entry para mostrar el contador
contador = 0
txt_contador = ttk.Entry(root, font=("Arial", 10, "bold"), width=1)
txt_contador.pack(pady=5)
txt_contador.insert(0, contador)  # Insertamos el valor inicial del contador

# Config de estilo para el Entry
style.configure("Custom.TEntry", background="lightgray", foreground="black", padding=5)

# Aplica el estilo al Entry
txt_contador.config(style="Custom.TEntry")

btn_cerrar = ttk.Button(root, text="Cerrar", style="Boton.TButton", command=root.destroy)
btn_cerrar.pack(side=tk.BOTTOM, padx=5, pady=10)

btn_actualizar = ttk.Button(root, text="Actualizar", style="Boton.TButton", command=obtener_datos)
btn_actualizar.pack(side=tk.BOTTOM, padx=5, pady=10)

obtener_datos()

root.mainloop()
