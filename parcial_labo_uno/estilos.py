from sanitizacion_string import *
import re

def estilar_diccionario_pokemon_basico(ataque:int, defensa:int,
                            elemento:list)->dict:
    '''
    Brief: Arma un diccionario con caracteristicas especificas
    Parametros: Ataque, defensa: 2 enteros que representan datos
    de ataque y defensa del pokemon
                elemento: La lista sobre la cual armar el diccionario
    Return: Devuelve el diccionario con formato
    '''
    diccionario = \
    {
    "pokedex" : elemento[0],
    "nombre" : elemento[1],
    "tipo" : elemento[2].split("/"),
    "ataque" : ataque,
    "defensa" : defensa,
    "habilidades" :  elemento[5].split("|*|")
    }
    return diccionario


def estilar_especifico_dos(diccionario:dict)->str:
    '''
    Brief: Le da un estilo específico a un diccionario
    Parametros: diccionario: representa el pokemon especifico
    sobre el cual hacer cambios
    Return: Devuelve un string con estilo específico
    '''
    promedio_poder = ((diccionario['ataque'] + 
                        diccionario['defensa']) / 2)
    tipo = " ".join(diccionario['tipo'])
    string = f"{diccionario['nombre']} | {tipo}"\
    f" | promedio AyD: {promedio_poder}"
    return string


def estilar_especifico_uno(lista_tipos:list, 
                        parametro_uno:int, parametro_dos:str)->str:
    '''
    Brief: Hace un string con estilo específico
    Parametros: lista_tipos: Representa la lista de tipos de 
                pokemones
                parametro_uno, parametro_dos: Parametros sobre los
                cuales realiza el string con estilo
    Return: Devuelve ese string con estio
    '''
    lista_tipos.append(f"{parametro_uno}: {parametro_dos}")
    listado_final_str = "\n".join(lista_tipos)
    return listado_final_str


def estilar_especifico_tres(diccionario:dict)->str:
    '''
    Brief: Otro tipo de estilo especifico en base a un diccionario,
    agregandolo a una lista
    Parametros: diccionario: será cada pokemon
    Return: Devuelve una lista con el string
    '''
    linea = f"{diccionario['nombre_poke']}"\
            f"-{diccionario['fortaleza']}"\
            f"-{diccionario['tipo_fortaleza']}"
    return linea


def estilar_especifico_cuatro(diccio:dict, parametro:int,
                            parametro_literal:str)->dict:
    '''
    Brief: Otro tipo de estilo especifico en base a un diccionario
    Parametros: diccio: un diccionario que representa a cada pokemon
                parametro: Parametro entero que representa el key
                ataque del diccionario 
                parametro_literal: Es un string del parametro int de
                arriba; ataque, defensa o ambos
    Return: Devuelve un diccionario con 3 key
    '''
    diccionario_lineas = {
    "nombre_poke" : diccio['nombre'],
    "fortaleza" : diccio[parametro],
    "tipo_fortaleza" : parametro_literal
    }
    return diccionario_lineas


def estilar_especifico_cinco(lista:list, diccio:dict, nombre:str)->str:
    '''
    Brief: Agrega una linea string con formato a una lista ya la une
    con un contrabarra n
    Parametros: lista: lista a la que añade la linea string
                diccio: Un diccionario que representa cada pokemon
                nombre: Representa el key nombre del diccionario
    Return: Devuelve un string unido con contrabarra n
    '''
    lista.append(\
    f"-{diccio[nombre]}"\
    " | Fueza de ataque: "\
    f"({diccio['ataque']})")
    nombres = "\n".join(lista)
    return nombres


def estilar_especifico_seis(lista:list)->str:
    '''
    Brief: Recorre una lista y reemplaza elementos por
    otros para dar un formato adecuado
    Parametros: lista: Sera la lista de pokemones
    Return: Devuelve el string  separado con contrabarra n
    '''
    lista_joined = []
    for pokemon in lista:
        pokemon = str(pokemon)
        pokemon = re.sub("[|}|'|\[|\]]", "", pokemon)
        pokemon = re.sub("[{]", "-", pokemon)
        lista_joined.append(pokemon)
    string_final = "\n".join(lista_joined)
    return string_final 