from sanitizacion_string import *


def listar_tipos_sin_repetido(lista:list, key:str):    
    '''
    Brief: Crea una lista sin repetidos de una key specífica
    Parametros: Lista: iterará sobre ella
                Key: Será si o si o habilidades o tipo, de 
                pokemon
    Return: Devuelve el set sin repetidos si salio bien 
    en tipo lista o false o -3 si ocurrió error
    '''
    if type(lista) != list or len(lista) == 0:
        return -3
    else:
        lista_tipo = []
        if key != "tipo" and key != "habilidades":
            return False
        else:
            for pokemon in lista:
                for tipo in pokemon[key]:
                    lista_tipo.append(tipo)
            lista_tipo_set = list(set(lista_tipo))
            return lista_tipo_set


def sanitizar_lista(lista:list):
    '''
    Brief: Recorre una lista y la sanitiza llamando a las
    funciones correspondientes
    Parametros: Lista: Una lista a sanitizar
    Return: Devuelve otra lista sanitizada en base a la 
    recibida por parametro
    '''
    if type(lista) != list or len(lista) == 0:
        return -3
    else:
        lista_sanitizada = []
        for item in lista:
            item = sanitizar_string(item)
            lista_sanitizada.append(item)
        return lista_sanitizada


def verificar_lista(lista:list, key:str, nombre:str, tipo:str):
    '''
    Brief: Si los parametros coinciden, los agrega a una lista
    Parametros: Lista: Lista de pokemones
                Key: será o tipo o habilidad (key del diccionario)
                nombre: será 'nombre' (key del diccionario)
                tipo: será un string que se comparará para ver si 
                está dentro de la lista sanitizada
    Return: devuelve una lista con los pokemones que coinciden con los
    parámetros indicados, o false o n° negativo si no cumple con 
    las verificaciones adecuadas
    '''
    if type(lista) != list or len(lista) == 0:
        return -3
    elif key != "tipo" and key != "habilidades":
        return -2
    elif nombre != "nombre":
        return -2
    else:
        coindidente = []
        for pokemon in lista:
            pokemon[nombre] = sanitizar_string(pokemon[nombre])
            lista_tipos = sanitizar_lista(pokemon[key])
            if tipo in lista_tipos:
                coindidente.append(pokemon)
        return coindidente


def chequear_coincidencias(lista:list, parametro_chequear:str)->int:
    '''
    Brief: Cuenta si hay coincidencias en un parametro string dentro
    de una lista
    Parametros: lista: Lista a recorrer; lista de pokemones
    Return: 
    '''
    contador_coincidencias = 0
    for habilidad in lista:
        habilidad = sanitizar_string(habilidad)
        if parametro_chequear == habilidad:
            contador_coincidencias += 1
    return contador_coincidencias