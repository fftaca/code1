#Ejercicio 1

#Input a. 0
result_a = 0
print(result_a)  # Output: 0

#Input b. 1.5 * 0
result_b = 1.5 * 0
print(result_b)  # Output: 0.0

#Input c. 11 / 2
result_c = 11 / 2
print(result_c)  # Output: 5.5

#Input d. 11 // 2
result_d = 11 // 2
print(result_d)  # Output: 5

#Input e. 11.0 // 2.0
result_e = 11.0 // 2.0
print(result_e)  # Output: 5.0

#Input f. 2 ** 2
result_f = 2 ** 2
print(result_f)  # Output: 4

#Input g. "a" + "b"
result_g = "a" + "b"
print(result_g)  # Output: "ab"

#Input h. "a" * 0
result_h = "a" * 0
print(repr(result_h))  # Output: ""

#Input g. "a" * 5
result_g = "a" * 5
print(result_g)  # Output: "aaaaa"


#Ejercicio 2

#a. Error en la division por cero
try:
    ejercicio_a = 1 / 0
    print(ejercicio_a)
except ZeroDivisionError:
    print("ERROR DIVISION x CER00000")
#b. 
ejercicio_b = 10 / 2 // 1 ** 5
print(ejercicio_b)
#c.
ejercicio_c = "hola" + ' ' + "mundo" + '!'
print(ejercicio_c)
#d.
ejercicio_d = "hola" + (" " + "mundo")
print(ejercicio_d)
#d1.
ejercicio_d1 = "hola" + (" " + "mundo") * 0
print(ejercicio_d1)
#d2.
ejercicio_d2 = "hola" + (" " + "mundo") * 2
print(ejercicio_d2)

#Ejercicio 3

#Input a. 3
a = 3
print("a. 3 == 3:", a == 3)  # Resultado: True

#Input b. 3.0
b = 3.0
print("b. 3.0 == 3.0:", b == 3.0)  # Resultado: True

#Input c. (0.1 + 0.2) * 10
c = (0.1 + 0.2) * 10
print("c. (0.1 + 0.2) * 10 == 3.0:", c == 3.0)  # Resultado: True

#Input d. 22 / 7
d = 22 / 7
print("d. 22 / 7 == 3.14:", d == 3.14)  # Resultado: False

#Input e. 22 // 7
e = 22 // 7
print("e. 22 // 7 == 3:", e == 3)  # Resultado: True


'''Ejercicio 4
¿Cuáles son las diferencias y similitudes entre las siguientes expresiones?
'''

ejercicio_4a1 = 10 + 5
ejercicio_4a2 = 10 + 5.0
ejercicio_4a3 = 10 + 5.
print("Resultados ejercicios 4a: ", ejercicio_4a1, "-", ejercicio_4a2, "-", ejercicio_4a3)
#todas las expresiones suman dos numeros, pero difieren en los tipos de datos involucrados y en como Python interpreta los numeros en punto flotante. El primer ejercicio suma 2 numeros int, el segundo int + float, el tercero int + float (al encontrarse el punto no importa si hay valor o no, es un float). 

ejercicio_4b1 = 11 / 2
ejercicio_4b2 = 11 // 2
ejercicio_4b3 = 11.0 // 2
print("Resultados ejercicios 4b: ", ejercicio_4b1, "-", ejercicio_4b2, "-", ejercicio_4b3)
#mismo caso que el ejercicio anterior. En el primer ejercicio dividimos 2 int, en el segundo division entera de 2 int, en el tercero division entera de 1 float + 1 int, resultado siempre float aunque sea .0

# EJERCICIO 5

ejercicio_5a = +1
print(ejercicio_5a)

ejercicio_5b = -1
print(ejercicio_5b)

ejercicio_5c = +-1
print(ejercicio_5c)

ejercicio_5d = -+1
print(ejercicio_5d)

# EJERCICIO 6

#6.a 3 * 5 - 7 * 4 / 14 + 3 / 1

ejercicio_6a = (3*5) - (7*4/14) + (3/1)
print("Result: 6.a = ", ejercicio_6a)

#6.b 2 ** 1 + 3 / 5 // 4

ejercicio_6b = (2**1) + ((3/5) //4)
print("Result: 6.b = ", ejercicio_6b)

#6.c 8 / 4 / 2 ** 2 ** 2

ejercicio_6c = (8/4) / ((2**(2**2)))
print("Result: 6.c = ", ejercicio_6c)

#EJERCICIO 7 - Encontrar el resultado de las siguientes expresiones:

ejercicio_7a = (4 >= 40 and 8 <= 10) or (2 < 20 or 10> 100)
print("7a =", ejercicio_7a)

ejercicio_7b = 4 <= 10 or (2/10) == 1
print("7b =", ejercicio_7b)

ejercicio_7c = (8 >= 10 or 4 <= 8) and (3 != 10 or 10 >= 4)
print("7c =",ejercicio_7c)

ejercicio_7d = (50 > 49 and 7 == 5) or (15 <= 14 or 10 > 100)
print("7d =", ejercicio_7d)

ejercicio_7e = not(not(10 >= 8) and 1 > 3) or (2 != 3 and 2 < 8)
print("7e =", ejercicio_7e)

ejercicio_7f = (4 > 2 or 7 > 6) and not(3 < 6 or 2 > 0)
print("7f =", ejercicio_7f)

ejercicio_7g = not(0)
print("7g =", ejercicio_7g)

ejercicio_7h = not(1)
print("7h =", ejercicio_7h)

ejercicio_7i = not([])
print("7i =", ejercicio_7i)

ejercicio_7j = not('a')
print("7j =", ejercicio_7j)

ejercicio_7k = not('') or not(' ')
print("7k =", ejercicio_7k)

#EJERCICIO 8 - Verificar si son correctos o no los siguientes fragmentos de codigo, en caso de no ser correcto arreglar.

#8a
saludo = 'hola'
destino = 'mundo'
puntuacion = '!'

print(saludo + " " + destino + puntuacion)

#8b
cateto1 = float(input("Ingrese el cateto1: "))
cateto2 = float(input("Ingrese el cateto2: "))
hipotenusa = ((cateto1**2) + (cateto2**2)) ** 0.5
print("La longitud de la hipotenusa es =", hipotenusa)

#8c
tengo_hambre = False
del tengo_hambre
tengo_hambre = True
del tengo_hambre
#este ejercicio es algo confuso y no tiene mucha logica, aunque es tecnicamente correcto crear una variable y eliminarla y volver a crearla con otro estado, para automatizar una tarea como esta podriamos crear una funcion como la siguiente:

def cambiar_estado_hambre (estado_anterior):
    return not estado_anterior #cambiar de T a F y viceversa
'''tambien podriamos definir una funcion de la siguiente manera
if estado_anterior == 'si':
    return 'no'
elif estado_anterior == 'no':
    return 'si'
else:
    return estado_anterior'''
#de esta manera los estados serian nuevo_estado = si / no

tengo_hambre = False
respuesta = input("¿Tienes hambre? (si/no): ").strip().lower()

if respuesta == 'si':
    nuevo_estado = True
elif respuesta == 'no': 
    nuevo_estado = False
else: 
    print("Responda Si o No")
    exit()

tengo_hambre = cambiar_estado_hambre(nuevo_estado)

print("nuevo estado: ", tengo_hambre)


#EJERCICIO 9 - obten datos utiles utilizando SLICING

sitio_web = "https://fceia.unr.edu.ar/noticias-fceia"

protocolo = sitio_web[:5]
print(protocolo)
nombre_de_dominio = sitio_web[8:24]
print(nombre_de_dominio)
ruta = sitio_web[24:]
print(ruta)

#EJERCICIO 10 - obten numeros pares

#numeros = "0123456789"
numeros = list(range(10))
pares = numeros[::2]
print(*pares, sep= ', ') #utilizo el asterisco para eliminar corchetes y STEP para dar la coma de separacion de valores.

#EJERCICIO 11

#traducir de lenguaje natural a expresiones booleanas. Determinar veracidad o falsedad.

#a. La longitud de la cadena "Hola, mundo" es 14
Saludo14 = "Hola, Mundo"
es_longitud_14 = len(Saludo14) == 14
print(es_longitud_14)

Saludo_x = input("Ingrese su saludo:")
longitud_real = len(Saludo_x)
print("Longitud real:", longitud_real)

#b. El area de un cuadrado de lado 5 es igual a la raiz cuadra de 625.

from math import sqrt
lado = 5
area_cuadrado = lado * lado

raiz_cuadrada_625 = sqrt(625)

es_igual = area_cuadrado == raiz_cuadrada_625
print("¿El area del cuadrado de lado 5 es igual a la raiz de 625?:", es_igual)

#c. El diametro de un circulo de radio 3,25 es menor que 7 y mayor a 6.

radio = 3.25
diametro = 2 * radio #el diametro es el doble del radio

esta_entre_7_y_6 = 6<diametro<7
print(esta_entre_7_y_6,", Es:", diametro)

#d. La aproximacion de PI = 22/7 es un numero mayor que 3, y 2 + 2 es igual a 5.

pi = 22 / 7
print(pi)
es_mayor_que_3 = pi > 3 and (2 + 2) == 5
print(es_mayor_que_3)

#e. el numero 10 es mayor a 5 o 0 dividido 0 es igual 0.

resultado = 10 > 5 or (0 / 0) == 0
print(resultado)

#f. La cadena "Python" tiene una longitud de 5 y 1+ "1" es igual a 2.

cadena = "Python"
Longitud = len(cadena) == 5 and (1 + int("1")) == 2 #sino cambiara la variable "1" a INT, ocurriria un fallo al sumar un INT + un STR.
print(Longitud)

#EJERCICIO 12 - Proponer u nalgoritmo (en lenguaje natural) para resolver cada problema

#a. dada la base y altura de un ractangulo, informar el area y su perimetro
'''
init = comienzo algorithm
Input_data  = Solicito ingrese base y altura (FLOAT(input))
Calculo_el_area_del_rectangulo = base * altura
Calculo_el_perimetro = 2 * Calculo_el_area_del_rectangulo
Output = Calculo_el_area_del_rectangulo, Calculo_el_perimetro
print (Calculo_el_area_del_rectangulo)
print (Calculo_el_perimetro)
End
'''

#b. Calcular la nota final de un alumno que se obtiene de promediar las 3 notas de sus parciales.

nota1 = float(input("Ingrese nota 1:"))
nota2 = float(input("Ingrese nota 2:"))
nota3 = float(input("Ingrese nota 3:"))
Promedio = (nota1 + nota2 + nota3) / 3
print("Su promedio es:", Promedio)

#c. Calcular la distancia de 2 puntos en el plano

x1 = float(input("Ingrese coordenadas de X (primer punto):"))
y1 = float(input("Ingrese coordenadas de y (primer punto):"))
x2 = float(input("Ingrese coordenadas de x (segundo punto):"))
y2 = float(input("Ingrese coordenadas de y (segundo punto):"))

distancia_entre_puntos = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) otro modo de calcularlo importando sqrt del modulo MATH
redondear_distancia_entre_puntos = round(distancia_entre_puntos, 3)
print("La distancia entre los puntos es:", redondear_distancia_entre_puntos)

#EJERCICIO 13

#Escribir un algoritmo en el cual se pida al usuario que responda la pregunta: "¿Como esta el dia de hoy? (soleado, nublado, lloviendo)". A continuacion, mostrar por pantalla un mensaje que indique "El dia de hoy esta...", completando con el dato ingresado.

palabras_validas = ["soleado", "nublado", "lloviendo"] #creo una lista con las palabras validas
intentos = 0 #les doy un contador para luego poder dar un limite de intentos

while intentos < 3: #permito este bucle continuo por un maximo de 3 veces, tipo cajero automatico
    respuesta = input("¿Como esta el dia de hoy? (soleado, nublado, lloviendo): ") #solicito al usuario escriba el dia
    
    #verifico la respuesta, con lower cambio a minuscula independientemente de lo que haya escrito y siempre y cuando se encuentre en la lista creada, con BREAK rompo el bucle si la respuesta es correcta.
    if respuesta.lower() in palabras_validas:
        print("El dia de hoy esta:", respuesta)
        break
    
    #Respuestas invalidas, muestro mensaje de error y tengo el contador de intentos
    else:
        print("Ingrese solo las respuestas que se le mencionan")
        intentos +=1

#Si el bucle llega a 3 intentos y el usuario no coloco correctamente le muestro por pantalla que se le agotaron los intentos        
if intentos == 3:
    print("Intentos agotados")
    
#EJERCICIO 14

'''conocido el numero en matematica PI, pedir al usuario que ingrese el valor del radio de una circunferencia y calcular y mostrar por pantalla el area y perimetro. Recuerde que para calcular el area y el perimetro se utilizan las siguientes formulas
area = pi * radio**2
perimetro = 2 * pi * radio
'''
pi = 3.1416
radio_de_circunferencia_x = float(input("Ingrese el radio de una circunferencia X:"))

calcular_area = round(pi * radio_de_circunferencia_x ** 2, 5)
calcular_perimetro = round(2 * pi * radio_de_circunferencia_x, 5)

print("El valor de la Area es:", calcular_area, ", y el valor del Perimetro es:", calcular_perimetro)

#EJERCICIO 15

#Escribir un programa que calcule el precio promedio de un producto. El precio promedio se debe calcular a partir del precio del mismo producto en tres establecimientos distintos.

semillitas_carrefour = 1080
semillitas_micropack = 1200
semillitas_coto = 1100

promedio = (semillitas_carrefour +  semillitas_coto + semillitas_micropack) / 3
print("El precio promedio de las semillitas es:", promedio)

#EJERCICIO 16

#A partir de una conocida cantidad de metros que el usuario ingresa a través del teclado se debe obtener su equivalente en centı́metros, en milı́metros y en pulgadas.
#Ayuda: 1 pulgada equivale a 2.54 centı́metros

metros = float(input("Ingrese cantidad de metros:"))
metros_a_centimetros = round(metros * 100, 3)
metros_a_milimetros = round(metros * 1000, 3)
metros_a_pulgadas = round(metros *100 / 2.54, 3)

print(f"Medida en cm: {metros_a_centimetros}\n"
      f"Medida en mm: {metros_a_milimetros}\n"
      f"Medida en pg: {metros_a_pulgadas}\n")

'''Ejercicio realizado con tkinter para visualizarlo

#importa tkinter para la visualizacion y win32api para centrar la ventana segun dimensiones de la pantalla
import tkinter as tk
import win32api

# Funcion donde agrego event=none para clickear enter y que funcion al igual que el boton de convertir, agrego la variable metros_str para que sea indiferente el ingreso de punto o coma para la conversion
def convertir_unidades(event=None):
    metros_str = entrada_metros.get().replace(',','.')
    metros = float(metros_str)
    metros_a_centimetros = round(metros * 100, 3)
    metros_a_milimetros = round(metros * 1000, 3)
    metros_a_pulgadas = round(metros * 100 / 2.54, 3)
    
    # Utilizo resultado.config(text= ya que en el contexto de una GUI (interfaz de usuario), este es un objeto label, en cambio el PRINT, mostraria el texto por consola.
    resultado.config(text=f"Medida en cm: {metros_a_centimetros}\n"
                          f"Medida en mm: {metros_a_milimetros}\n"
                          f"Medida en pg: {metros_a_pulgadas}\n")


# Creo la funcion limpiar para aplicar a un boton
def limpiar_entry():
    entrada_metros.delete(0,tk.END)
    resultado.config(text="")
   
# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Unidades!")

# De esta manera obtenengo las dimensiones de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Calculo las coordenadas para centrar la ventana
x = (ancho_pantalla - 300) // 2
y = (alto_pantalla - 200) // 2

# Establezco la geometría de la ventana
root.geometry(f"+{x}+{y}") #recordar que la f, sola se utiliza para obtener sintaxis mas clara y legible, es lo mismo que colocar comas ,,,.

# Creo un widget dentro de la ventana principal que indica sobre el ENTRY que debe realizar "el usuario"
etiqueta_metros = tk.Label(root, text="Ingrese la cantidad en metros:")
etiqueta_metros.pack(pady=1)

#Entry se utiliza en tkinter para crear un cuadro para ingresar datos por teclado "el usuario"
entrada_metros = tk.Entry(root, width=5)
entrada_metros.pack(pady=1)

boton_convertir = tk.Button(root, text="Convertir", command=convertir_unidades)
boton_convertir.pack(pady=1)

#Agrego un boton para limpiar todo el contenido
boton_limpiar = tk.Button(root, text="Limpiar", command=limpiar_entry)
boton_limpiar.pack(pady=1)

resultado = tk.Label(root, text="")
resultado.pack(pady=1)

# Vinculo el evento Enter al boton convertir
entrada_metros.bind("<Return>", convertir_unidades)

# Ejecuto el bucle de eventos
root.mainloop()

# Para compilar mi app y crear un ejecutable, ademas agrego el comando noconsole para evitar se habra el command prompt de fondo

#pyinstaller --onefile --noconsole tu_script.py
'''

#EJERCICIO 17

#Escribir un programa que calcule cuántos litros de combustible consumió un automóvil. El usuario debe ingresar una cantidad de litros de combustible cargados en la estación y una cantidad de kilómetros recorridos. Después, el programa calculará el consumo (km/lt) y se lo mostrará al usuario.

#Definir un consumo promedio en una variable fija
consumo_promedio = 10  # km/lt

#Ingresar cantidad de litros_cargados y km recorridos
litros_cargados = float(input("Cantidad de litros cargados: "))
km_recorridos = float(input("Cantidad de kilómetros recorridos: "))

#Calcular el consumo real
consumo_real = km_recorridos / litros_cargados

print("El consumo promedio es de", consumo_promedio, "km/lt")
print("El consumo real es de", consumo_real, "km/lt")

#Calcular la cantidad de litros_consumidos
litros_consumidos = km_recorridos / consumo_promedio

print("Cantidad de litros consumidos =", litros_consumidos)

#EJERCICIO 18

#Escriba un programa que permita al usuario ingresar el valor de dos variables numéricas de tipo entero. Posteriormente, el programa debe intercambiar los valores de ambas variables y mostrar el resultado final por pantalla. Por ejemplo, si el usuario ingresa los valores num1 = 9 y num2 = 3, la salida del programa deberá mostrar: num1 = 3 y num2 = 9.
#####Ayuda: Para intercambiar los valores de dos variables se debe utilizar una variable auxiliar.

valor1 = int(input("Ingrese el primer numero: "))
valor2 = int(input("Ingrese el segundo numero: "))

#ahora creo la variable auxiliar para guardar el estado de valor1
variable_auxiliar = valor1
valor1 = valor2
valor2 = variable_auxiliar

#Mostrar resultado final implementar f-string para mejorar sintaxis
print(f"Intercambiando los datos obtenemos que: "
      f"el primer numero es {valor1}, "
      f"y el segundo numero es {valor2}")

'''Tambien podemos simplemente mentirle al programa cambiando el print de valor2 y valor1

valor1 = int(input("Ingrese el primer numero:"))
valor2 = int(input("Ingrese el segundo numero:"))

#Mostrar resultado final
print(f"Intercambiando los datos obtenemos que: "
      f"el primer numero es {valor2}, "
      f"y el segundo numero es {valor1}")
'''

#EJERCICIO 19

'''Escriba un programa que permita al usuario ingresar el valor de tres variables numéricas de tipo entero. Posteriormente, el programa debe intercambiar los valores de las tres variables y mostrar el resultado final por pantalla. Por ejemplo, si el usuario ingresa los valores num1 = 9, num2 = 3 y num3 = 5 la salida del programa deberá mostrar: num1 = 5, num2 = 9 y num3 = 3.

Ayuda: Para intercambiar los valores de tres variables se debe utilizar una variable auxiliar.'''

valor1 = int(input("Ingrese el primer numero: "))
valor2 = int(input("Ingrese el segundo numero: "))
valor3 = int(input("Ingrese el tercer numero: "))

#ahora creo la variable auxiliar para guardar el estado de valor1
variable_auxiliar = valor1
valor1 = valor3
valor3 = valor2
valor2 = variable_auxiliar

#Mostrar resultado final implementar f-string para mejorar sintaxis
print(f"Intercambiando los datos obtenemos que: "
      f"el primer numero es {valor1}, "
      f"el segundo numero es {valor2}, "
      f"y el tercer numero es {valor3}")

#EJERCICIO 20

#Escriba un programa que lea dos números enteros y realice el cálculo de la suma, resta, multiplicación y división entre ambos valores. Los resultados deben mostrarse por pantalla.

x = int(input("Ingrese el primer valor para el calculo: "))
y = int(input("Ingrese el segundo valor para el calculo: "))

suma = x + y
resta = x - y
multi = x * y
div = x / y

print(f"Resuldos:\n"
      f"Suma = {suma}\n"
      f"Resta = {resta}\n"
      f"Producto = {multi}\n"
      f"Division = {div}")

#EJERCICIO 21

'''Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso actual. Diseñar un algoritmo para este propósito. Recuerde que para calcular el porcentaje puede hacer una regla de 3 simple. El programa debe solicitar al usuario que ingrese la cantidad total de niños, y la cantidad total de niñas que hay en el curso.'''

cant_ninos = int(input("Ingrese la cantidad total de niños: "))
cant_ninas = int(input("Ingrese la cantidad total de niñas: "))

total_estudiantes = cant_ninos + cant_ninas

porcentaje_ninos = round((cant_ninos/total_estudiantes) * 100, 2)
porcentaje_ninas = round((cant_ninas/total_estudiantes) * 100, 2)

print(f"El porcentaje de niños es = {porcentaje_ninos} "
      f"y el porcentaje de niñas es = {porcentaje_ninas}")

#EJERCICIO 22

'''A partir de una conocida cantidad de dias que el usuario ingresa a través del teclado, escriba un programa para convertir los dias en horas, en minutos y en segundos. Por ejemplo: 1 dia = 24 horas = 1440 minutos = 86400 segundos.'''
#si solo voy a usar los valores una sola vez esta es la manera mas breve y sencilla.
cant_dias = int(input("Ingresar cantidad de dias: "))
dias_a_horas = round(cant_dias * 24, 3)
dias_a_minutos = round(cant_dias * 1440, 3)
dias_a_segundos = round(cant_dias * 86400, 3)

print(f"{cant_dias} día(s) equivale(n) a:")
print(f"{dias_a_horas} horas")
print(f"{dias_a_minutos} minutos")
print(f"{dias_a_segundos} segundos")

#esta manera de resolver el ejercicio me permite reutilizar la funcion mas adelante.
def conversor_de_dias(cant_dias):
    dias_a_hs = round(cant_dias * 24, 3)
    dias_a_min = round(cant_dias * 1440, 3)
    dias_a_seg = round(cant_dias * 86400, 3)
#estaba colocando el print a la altura de la funcion DEF y entraba en fallo y no detectaba porque.
    print(f"{cant_dias} dia(s) equivale(n) a: \n"
      f"{dias_a_hs} horas \n"
      f"{dias_a_min} minutos \n"
      f"{dias_a_seg} segundos")

cant_dias = int(input("Ingresar cantidad de dias: "))
conversor_de_dias(cant_dias)

#EJERCICIO 23

#Modelar los siguientes problemas, nombrando los datos relevantes y el resultado, junto con la forma que tendrán sus representaciones internas en Python. Luego programar la solución.

'''a. Se tienen dos habitaciones dentro de un hogar, cada una con una temperatura ambiente. Se quiere saber a qué temperatura estarán las habitaciones, dado suficiente tiempo para que se transmita el calor de una a la otra. Se conoce que en este caso es válido promediar temperaturas.'''

def temperatura_final(temp_hab1, temp_hab2):
    #calcular promedios
    temp_final = (temp_hab1 + temp_hab2) / 2 #es el calculo del promedio de ambas habitaciones
    return temp_final
#Inicial
temp_hab1 = float(input("Ingrese la temperatura ambiente inicial de la habitacion 1: "))
temp_hab2 = float(input("Ingrese la temperatura ambiente inicial de la habitacion 2: "))
#calcular temperatura final
temp_final = temperatura_final(temp_hab1, temp_hab2)

print(f"Dado un tiempo suficiente, la temperatura de las habitaciones se encuentra en: {temp_final} °C")

'''def temperatura_final(temp_hab1, temp_hab2, tiempo):
    factor = 0.25  # Factor de ajuste para la velocidad de transferencia de calor
    for _ in range(tiempo):
        temp_promedio = (temp_hab1 + temp_hab2) / 2
        temp_hab1 += factor * (temp_promedio - temp_hab1)
        temp_hab2 += factor * (temp_promedio - temp_hab2)
    return temp_hab1, temp_hab2

# Solicitar temperaturas iniciales y tiempo
temp_hab1 = float(input("Ingrese la temperatura ambiente inicial de la habitacion 1: "))
temp_hab2 = float(input("Ingrese la temperatura ambiente inicial de la habitacion 2: "))
tiempo = int(input("Ingrese el tiempo en horas para alcanzar el equilibrio: "))

# Calcular temperatura final
temp_final_hab1, temp_final_hab2 = temperatura_final(temp_hab1, temp_hab2, tiempo)

print(f"Después de {tiempo} horas, la temperatura de la habitación 1 es: {temp_final_hab1} °C")
print(f"Después de {tiempo} horas, la temperatura de la habitación 2 es: {temp_final_hab2} °C")
'''

#23.b
'''b. Se tiene una multitud afuera, cada persona le dirá su nombre a cada otra persona en la multitud. Se quiere saber cuánto tiempo llevará hacer esto, dado que decir una vez tu nombre lleva aproximadamente 4 segundos y medio.'''
'''
#Encontre esta manera pero el resultado era lineal de una a una persona

Cant_multitud = int(input("Ingrese cantidad de personas en la multitud: "))

Tiempo_estimado_de_nombres = Cant_multitud * 4.5

print("El tiempo estimado para saber los nombres de toda la multitud es de: ", Tiempo_estimado_de_nombres, " seg.")
'''
#Despues pense en que todas esas personas tenian que decirse su nombre entre todas juntas, de manera no lineal
#Entonces creamos una funcion para calcular el tiempo total de la cantidad de la multitud X, la cual seria ingresada por teclado.
def calcular_tiempo_total(cant_multitud):
    tiempo_de_nombre = 4.5
    tiempo_total = cant_multitud * (cant_multitud - 1) * tiempo_de_nombre / 2 #utilizamos esta formula n(n-1) / 3 *t, donde n, es el numero de personas en la multitud, y n-1 quiere decir que se presenta a todas las personas excepto a si misma, luego multiplicar por el tiempo que lleva presentarte T. (Ver formula en Mate. COMBINATORIO) 
    # Respuesta a porque se divide por 2
    ''' es necesario porque en la combinación de N elementos tomados de a 2, cada par se cuenta dos veces si no se tiene en cuenta el orden. Por ejemplo, si tenemos los elementos A, B, y C, las combinaciones posibles serían AB, AC, y BC. Sin embargo, estas combinaciones se contarían dos veces si no se dividiera por 2, ya que tanto AB como BA se considerarían como combinaciones diferentes. Por lo tanto, para obtener el número correcto de combinaciones únicas, es necesario dividir por 2 para eliminar los duplicados.'''
    return tiempo_total
#numero aprox de personas
cant_multitud = int(input("Ingrese la cantidad estimada de personas en la multitud: "))
#tiempo estimado
tiempo_estimado = calcular_tiempo_total(cant_multitud)

print("El tiempo estimado para que todos digan su nombre es de:",tiempo_estimado," seg")

#23.c

'''c. Hay dos personas con nombres muy largos, pero similares. Se quiere conocer, por un lado, si tienen el mismo tamaño, y por otro lado si son iguales.

Ayuda para el programa: investigar la función len.'''

persona1 = str(input("Nombre de la primera persona = ")).lower()
persona2 = str(input("Nombre de la segunda persona = ")).lower()

#con LEN obtengo la longitud de los input's
longitud_nombre1 = len(persona1)
longitud_nombre2 = len(persona2)
#igualo longitudes & nombres ingresados ya convertidos a minusculas
mismo_tamaño = longitud_nombre1 == longitud_nombre2
son_iguales = persona1 == persona2

print(f"¿El tamaño(longitud) es igual?: {mismo_tamaño}\n"
      f"¿Los nombres son iguales?: {son_iguales}")