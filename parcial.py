import datetime
import random
import re
# 1. Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
# cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
# un personaje puede tener más de una raza y más de una habilidad.

def mostrar_datos_del_archivo(path:str): #declaro la funcion "mostrar_datos_del_archivo" y le paso por parametros un string "path"
    with open(path, "r",encoding = "utf-8") as archivo:  #abro el archivo, lo recorro usando path", y le agrego los caractere especiales("encoding = "utf-8"")"
        lista_personajes = []
        if not path: #si no esta en la ruta("path")
            print("ERROR. lista vacia")
            return -1
        else:
            for personaje in archivo: #declaro variable("personaje") para qu recorra("archivo") 
                lectura = re.split(",| \n", personaje) #le saca las(",") a la variable creada
                diccionario = {} #declaro un diccionario
                diccionario["Id"] = int(lectura[0])
                diccionario["Nombre"] = lectura[1]
                diccionario["Raza"] = lectura[2].strip() #le saco los espacios
                diccionario["Poder de pelea"] = int(lectura[3])
                diccionario["Poder de ataque"] = int(lectura[4])
                diccionario["Habilidades"] = lectura[5].replace("$%","") #remplazo los caracteres especiales "$%" por un espacio
                lista_personajes.append(diccionario) #le paso la variable con claves definidas "diccionario",  y las agrupo en la lista definda anteriormente "lista_personajes"
            return lista_personajes #retorno la lista

for personajes in mostrar_datos_del_archivo("DBZ.csv"): #declaro variable "personajes", que recorre mi funcion, la cual tiene el archivo "DBZ.csv" 
    print("Id: {} \n Nombre: {} \n Raza:{} \n Poder de pelea:{} \n Poder de ataque:{} \n Habilidades:{}\n".format(  #
        personajes["Id"],
        personajes["Nombre"],
        personajes["Raza"],
        personajes["Poder de pelea"],
        personajes["Poder de ataque"],
        personajes["Habilidades"],
        ))
    
# 2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
# corresponden a esa raza.

"""def listar_razas(lista: list): #declaro la funcion "listar_razas" y le paso por paremetros una lista "lista"
    lista_de_raza = {} #declaro que es un diccionrio
    for personaje in lista: 
        key = personaje["Raza"]
        if key in lista_de_raza:
                lista_de_raza[key] += 1 #si la raza ingersada esta en la lista se suma 
        else:
                lista_de_raza[key] = 1 #si no esta en lista se agrega 
    return lista_de_raza #retorna la "lista_de_raza"

raza = listar_razas(mostrar_datos_del_archivo("DBZ.csv"))
print(raza)"""

# 3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
# personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
# repetirse en los distintos listados.

"""def listar_razas(lista: list): #declaro la funcion "lista_agrupados" y le paso por paremetros una lista
    lista_de_personajes = [] #declaro una lista
    for personaje in lista: 
        datos_raza = (personaje["Raza"])
        if datos_raza not in lista_de_personajes: #si los datos de la "key" no estan en "lista_de_personajes"
            lista_de_personajes.append(datos_raza) #junto los datos obtenidos de la "key" en la  "lista_de_personajes"
    return lista_de_personajes

def mostrar(lista:list):
    lista_de_personajes = listar_razas(lista)
    for datos_raza in lista_de_personajes:
        print(datos_raza)
        for personaje in lista:
            if personaje["Raza"] == datos_raza:
                print("\t",personaje["Nombre"],personaje["Poder de ataque"])
    return lista_de_personajes 
mostrar(mostrar_datos_del_archivo("DBZ.csv"))"""

# 4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
# deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.

#declaro la funcion "listar_personajes_por_habilidad", le paso por parametros un string "habilidad" y una lista "lista"
"""def listar_personajes_por_habilidad(habilidad: str,lista: list): 
    lista_personajes = [] #declaro lista
    for personajes in lista:
        key = personajes["Habilidades"].replace("|","") #remplazo los pay "|" por espacios en la clave "["Habilidades"]" y la guardo en la variable "key"
        if habilidad in key:
            lista_personajes.append(personajes) #junto los datos que tengo en mi clave "key" en mi "lista_personajes"
    
    if lista_personajes: 
        print("Personajes que tienen la habilidad",habilidad)
        for personajes in lista_personajes:
            promedio = int(personajes["Poder de ataque"]) + int(personajes["Poder de pelea"])/2 #los parseo, los sumo y los divido por la cantidad que se haya sumado
            print((personajes["Nombre"], personajes["Raza"],"el promedio de pelea y ataque es de: ",promedio))
    else:
        print("Error... No se escontraron habilidades con ese nombre")

habilidad_buscada = input("Ingrese la habilidad que desea buscar: ") #
listar_personajes_por_habilidad(habilidad_buscada,mostrar_datos_del_archivo("DBZ.csv"))"""

# 5. Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. Gana la
# batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla se deberá
# guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del personaje que ganó y
# el nombre del perdedor. Este archivo anexará cada dato.

def seleccion_personaje(lista: list): 
    
    seleccion_personaje = input("Ingrese su personaje.. :")
    if not seleccion_personaje:
        print("Error personaje no elegido..")
        return -1
    for personajes in lista:
        if personajes["Nombre"] == seleccion_personaje:
            return seleccion_personaje

def generar_numero_aleatorio(minimo, maximo):
    numero_aleatorio = random.randint(minimo,maximo)
    return numero_aleatorio

def seleccio_enemigo(lista:list):
    numero_aleatorio = generar_numero_aleatorio(lista)
    for personaje in lista:
        if personaje["Id"] == numero_aleatorio:
        
"""print("Elegiste este personaje:", eleccion_personaje["Nombre"])
    enemigo = random.choice(lista) #elije personaje random de la lista
    print("Tu enemigo es:", enemigo["Nombre"],enemigo["Poder de ataque"])
    if eleccion_personaje["Poder de ataque"] > enemigo["Poder de ataque"]: #si el personaje elegido es mayor que el enemigo
        print("Winnn:", eleccion_personaje["Nombre"])
    elif eleccion_personaje["Poder de ataque"] < enemigo["Poder de ataque"]: #si el enemigo es mayor que el enemigo
        print("Winnn:",enemigo["Nombre"])
    else:
        print("Empate")

    return  """


"""def archivo ():
    fecha_actual = datetime.datetime.now()
    with open("datos_de_pelea.txt", "a",encoding = "utf-8") as archivo:
        archivo.write(f"{batalla}")"""

# 6. Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
# cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
# guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
# búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
# Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
# Nombre del archivo:
# Saiyan_Genki_Dama.Json
# Datos :
# Goten - 3000 - Kamehameha + Tambor del trueno
# Goku - 5000000 - Kamehameha + Super Saiyan 2

# 7. Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json de la opción

# 6.Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
# cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
# guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
# búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
# Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
# Nombre del archivo:
# Saiyan_Genki_Dama.Json
# Datos :
# Goten - 3000 - Kamehameha + Tambor del trueno
# Goku - 5000000 - Kamehameha + Super Saiyan 2

# 8. Salir del programa.