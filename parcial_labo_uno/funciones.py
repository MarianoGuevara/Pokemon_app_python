from os import system 
system("cls")

from sanitizar_string import *
from funciones_listas_generales import *
from estilos import *

import re
import os
import json

ruta_csv = "pokemones.csv"


def crear_texto_en_base_a_archivo(ruta_archivo:str)->str:
    '''
    Brief: En base a un archivo, crea un string con su contenido
    salteando la primera linea
    Parametros: ruta_archivo: ruta del archivo en cuestion
    Return: Devuelve el contenido del archivo hecho string o 
    un string diciendo que no existe si no lo hace
    '''
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            next(archivo)
            texto = archivo.read()
            return texto
    else:
        return False


def crear_lista_pokemones(ruta:str):
    '''
    Brief: Separa el texto string separando los diferentes pokemones
    Parametros: ruta: Una ruta de archivo
    Return: Devuelve la lista con los diferentes pokemones que hay
    o false si nisiquiera existe
    '''

    texto = crear_texto_en_base_a_archivo(ruta)
    if texto == False:
        return False
    else:

        lista_pokemones_basica = re.split("\n", texto)
        lista_elemento_por_pokemon = []
        for pokemones in lista_pokemones_basica:
            pokemones = pokemones.split(",")
            if len(pokemones) != 1:
                lista_elemento_por_pokemon.append(pokemones)
        return lista_elemento_por_pokemon
# print(crear_lista_pokemones('pokemones.csv'))


def traer_datos_desde_archivos(ruta:str):
    '''
    Brief: Llama a las funciones correspondientes y 
    ordena el contenido del csv en una lista de los 
    diferentes pokemones con sus respectivas 
    keys
    Parametros: Recibe una ruta de archivo
    Return: Devuelve la lista ordenada de pokemones
    si salió bien
    '''
    lista_pokemones_basica = crear_lista_pokemones(ruta)

    if lista_pokemones_basica == False:
        return False
    else:
        lista_pokemones_final = []
        for elemento in lista_pokemones_basica:
            try:
                ataque = int(elemento[3])
                defensa = int(elemento[4])
                linea = estilar_diccionario_pokemon_basico(ataque, 
                                                defensa, elemento)
                lista_pokemones_final.append(linea)
            except:
                return -2
        if len(lista_pokemones_final) != 0:
            return lista_pokemones_final
        else:
            return -1
# print(traer_datos_desde_archivos("pokemones.csv"))

def listar_cantidad_por_tipo(lista:list, key:str):
    '''
    Brief: Se fija los tipos de pokemon que hay y cuantos hay
    de cada uno
    Parametros: Lista: Representa la lista de pokemones
                Key: Representa el key tipo de lista pokemones
    Return: Devuelve un string con los tipos y sus cants si salió 
    bien, o un false o n° positivo si no lo hizo
    '''
    lista_tipo_sin_repe = listar_tipos_sin_repetido(lista, key)
    if lista_tipo_sin_repe == False:
        return False
    elif lista_tipo_sin_repe == -3:
        return -3
    else:
        if key == "tipo":
            lista_cant_tipos = []
            for tipo in lista_tipo_sin_repe:
                tipo = sanitizar_string(tipo)
                contador = 0
                for pokemon in lista:
                    lista_tipos = sanitizar_lista(pokemon[key])
                    if tipo in lista_tipos:
                        contador += 1
                estilo = estilar_especifico_uno(lista_cant_tipos, tipo, contador)
            return estilo
        else:
            return -2


def listar_nombres_por_tipo(lista:list, key:str, nombre:str):
    '''
    Brief: Lista los un string con estilo mostrando los pokemones
    que hay de cada tipo
    Parametros: Lista: Lista de pokemones
                Key: Representa 'tipo' de pokemon
                Nombre: Es la key nombre del diccionario de pokemon
    Return: Devuelve un string con los tipos y sus nombres
    si salió bien, o un false o n° negativo si no lo hizo
    '''

    lista_tipo_sin_repe = listar_tipos_sin_repetido(lista, key)
    if lista_tipo_sin_repe == False:
        return False
    elif lista_tipo_sin_repe == -3:
        return -3
    else:
        if key == "tipo":
            lista_cant_tipos = []
            for tipo in lista_tipo_sin_repe:
                tipo = sanitizar_string(tipo)
                lista_nombres = []

                coincidentes = verificar_lista(lista, key, nombre, tipo)
                if coincidentes == -2:
                    return -2
                else:
                    for pokemon in coincidentes:
                        linea = estilar_especifico_cinco(lista_nombres,
                                                        pokemon, nombre)
                    lista_cant_tipos.append(f"\n*{tipo}: \n{linea}\n")
            listado_final_str = "".join(lista_cant_tipos)
            return listado_final_str
        else:
            return False


def listar_pokemones_por_habilidad(lista:list, key:str, nombre:str):
    '''
    Brief: Pide al usuario una habilidad y muestra un string con
    formato de todos los pokemon que pertenecen a la misma
    Parametros: Lista: lista de pokemones 
                key: habilidades (key de diccionario)
                nombre: key nombre de diccionario
    Return: Devuelve un string con los pokemones que coinciden
    si salió bien, o un false o n° negativo si no lo hizo
    '''
    lista_habilidades = listar_tipos_sin_repetido(lista, key)
    if lista_habilidades == -3:
        return -3
    elif lista_habilidades == False:
        return False
    else:
        if key != 'habilidades':
            return False
        else:
            dato_ingresado = input("Ingrese una habilidad: ")
            dato_ingresado = sanitizar_string(dato_ingresado)

            contador = chequear_coincidencias(lista_habilidades, dato_ingresado)
            if contador != 0:
                lista_pokemones_coincidentes = [] 
                coincidentes = verificar_lista(lista, key, nombre, dato_ingresado)
                if coincidentes == -2:
                    return -2
                else:
                    for pokemon in coincidentes:
                        estilo = estilar_especifico_dos(pokemon)
                        lista_pokemones_coincidentes.append(estilo)
                    string_final = "\n".join(lista_pokemones_coincidentes)
                    return string_final
            else:
                return -1


def listar_pokemones_ordenados(lista:list, ataque:str, nombre:str):
    '''
    Brief: Ordena la lista por poder de ataque (de mayor a menor)
    o alfabeticamente si el parametro previo es identico
    Parametros: Lista: lista pokemones
                ataque: key 'ataque' de diccionario
                nombre: key 'nombre' de diccionario
    Return: Devuelve la misma reordenada y con algo de estilo 
    si salió bien, o un false o n° positivo si no lo hizo
    '''
    if type(lista) != list or len(lista) == 0:
        return False
    else:
        if ataque != "ataque" or nombre != "nombre":
            return -1
        else:
            for i in range(len(lista)):
                lista[i][nombre] = sanitizar_string(lista[i][nombre])
                for j in range(i+1, len(lista)):
                    lista[j][nombre] = sanitizar_string(lista[j][nombre])
                    if lista[i][ataque] < lista[j][ataque]:
                        auxiliar = lista[i]
                        lista[i] = lista[j]
                        lista[j] = auxiliar
                    elif lista[i][ataque] == lista[j][ataque]:
                        if lista[i][nombre] < lista[j][nombre]:
                            auxiliar = lista[i]
                            lista[i] = lista[j]
                            lista[j] = auxiliar

            estilo = estilar_especifico_seis(lista)
            return estilo


def guardar_json(lista:list, key:str, ataque:str, defensa:str):
    '''
    Brief: Crea un json con algunos datos formateados 
    de los pokemons de un tipo específico
    Parametros: lista: lista de pokemones
                key: será tipo si o si (del diccionario)
                ataque, defensa: Keys de diccionario tambien
    Return: Devuelve true si salio bien o si fue
    mal, un booleano o n° negativo
    '''
    if type(lista) != list or len(lista) == 0:
        return -3
    elif key != "tipo":
        return False
    else:
        tipo_ingresado = input("Ingrese un tipo de pokemon: ")
        tipo_ingresado = sanitizar_string(tipo_ingresado)

        lista_sin_repetido = listar_tipos_sin_repetido(lista, key)
        contador = chequear_coincidencias(lista_sin_repetido, tipo_ingresado)

        if contador != 0:
            if os.path.exists("pokemon"
                            f"es_tipo_{tipo_ingresado}.json"):
                return -1
            else:
                if ataque != "ataque" or defensa != "defensa":
                    return False
                else:
                    archivo_json = open('pokem'\
                    f'ones_tipo_{tipo_ingresado}'\
                    '.json', "w", encoding="utf-8")
                    diccionario_json = {}
                    lista_contenedor = []
                    for pokemon in lista:
                        lista_tipos_difs = sanitizar_lista(pokemon[key])
                        if tipo_ingresado in lista_tipos_difs:
                            if (pokemon[ataque]
                                > pokemon[defensa]):
                                line = estilar_especifico_cuatro(pokemon,
                                ataque, "Ataque")
                            elif (pokemon[ataque]
                                < pokemon[defensa]):
                                line = estilar_especifico_cuatro(pokemon,
                                defensa, "Defensa")
                            else:
                                line = estilar_especifico_cuatro(pokemon,
                                ataque, "Ambos")
                            lista_contenedor.append(line)
                    diccionario_json[tipo_ingresado] = lista_contenedor
                    json.dump(diccionario_json, 
                        archivo_json, indent=4, ensure_ascii=False)
                    return True
        else:
            return -2


def leer_json(msj_input):
    '''
    Brief: Pide un tipo de pokemon, y si fija si hay un json
    que contenga los pokemones del mismo para mostrarlo con
    formato
    Parametros: msj_input: Mensaje del input
    Return: Devuelve el contenido del json con formato
    si salió bien, o un false o n° negativo si no lo hizo
    '''
    input_dato = input(msj_input)
    input_dato = sanitizar_string(input_dato)
    if os.path.exists(f"pokemones_tipo_{input_dato}.json"):
        archivo_json = open(f"pokemones_tipo_{input_dato}.j"\
                            "son", "r", encoding="utf-8")
        texto = json.load(archivo_json)

        lista_json_contenido = []
        for pokemon in texto[input_dato]:
            if len(pokemon) != 3:
                return -5
            else:
                try:
                    linea = estilar_especifico_tres(pokemon)
                    lista_json_contenido.append(linea)
                except:
                    return -5
        texto_final = "\n".join(lista_json_contenido)
        archivo_json.close()
        return texto_final
    else:
        return False


#________________________________________________________________________________________________________


def pedir_string(msj:str):
    '''
    Brief: El usuario ingresa un string el cual será sanitizado 
    Parametros: msj: representa el mensaje que aparecerá por
                pantalla junto al input
    Return: devuelve el string si es correcto y falso si no lo es
    '''
    dato = input(msj)
    booleano = dato.isalpha()
    if booleano == False:
        return False
    else:
        dato = sanitizar_string(dato)
        return dato


def pedir_int_pokemon(msj:str)->int:
    '''
    Brief: El usuario ingresa un string que será pasado a
    entero
    Parametros: msj: representa el mensaje que aparecerá por
                pantalla junto al input
    Return: devuelve el string pasado a entero si es 
    correcto y falso si no lo es
    '''
    dato = input(msj)

    if dato.isdigit() == False:
        return False
    else:
        return int(dato)


def pedir_datos_pokemon(lista:list):
    '''
    Brief: Pide todos los datos requeridos para el nuevo pokemon
    y los agrega a una lista
    Parametros: lista: será la lista de pokemones
    Return: 
    '''
    lista_pokemones_inicial = []

    while True:
        n_poke = pedir_int_pokemon("Ingresa n° de pokedex: ")
        if n_poke == False or n_poke < 152:
            return False
        else:
            lista_pokemones_inicial.append(n_poke)

        nombre_poke = pedir_string("Ingresa nombre del pokemon: ")
        if nombre_poke == False:
            return False
        else:
            lista_pokemones_inicial.append(nombre_poke)

        tipo_poke = input("Ingrese el/los tipos del"\
                                    "pokemon separados por '/': ")
        lista_pokemones_inicial.append(tipo_poke)    

        ataque = pedir_int_pokemon("Poder de ataque: ")
        if ataque == False:
            return False
        else:
            lista_pokemones_inicial.append(ataque)

        defensa = pedir_int_pokemon("Poder de defensa: ")
        if defensa == False:
            return False
        else:
            lista_pokemones_inicial.append(defensa)

        habilid_poke = input("Ingrese la/las habilidades del"\
                                "pokemon separados por '|*|': ")
        lista_pokemones_inicial.append(habilid_poke)    

        nuevo_poke = estilar_diccionario_pokemon_basico(ataque, 
                                defensa, lista_pokemones_inicial)
        lista.append(nuevo_poke)

        while True:
            rta = pedir_string("Desea ingresar otro pokemon? (si o no): ")
            if rta != "si" and rta != "no":
                pass
            else:
                break
        if rta == "no":
            break


def nuevos_pokemones_a_string(lista:list):
    '''
    Brief: Convierte elementos de una lista a un 
    string con formato
    Parametros: lista: representa la lista de pokemons
    Return: Si sale mal, false, si no, el string con
    formato
    '''
    try:
        lista_nuevos_poke = []
        for pokemon in lista:
            linea = f"{pokemon['pokedex']},{pokemon['nombre']},"\
            f"{pokemon['tipo']},{pokemon['ataque']},"\
            f"{pokemon['defensa']},{pokemon['habilidades']}"
            lista_nuevos_poke.append(linea)
        string_pokemones_nuevos = "\n".join(lista_nuevos_poke)
        return string_pokemones_nuevos
    except:
        return False


def actualizar_csv(ruta:str, lista:list):
    '''
    Brief: Abre un csv y lo actualiza con lo nuevo
    Parametros: ruta: Ruta del csv de pokemones
    Return: Devuelve true si salio bien, y false o 
    n° negativo si salio mal
    '''
    if os.path.exists(ruta):
        if type(lista) != list or len(lista) == 0:
            return -1
        else:
            str_nuevos_pokes = nuevos_pokemones_a_string(lista)
            if str_nuevos_pokes == False:
                return False
            else:
                archivo = open(ruta, "w", encoding="utf-8")
                archivo.write(str_nuevos_pokes)
                archivo.close()
                return True
    else:
        return -5


