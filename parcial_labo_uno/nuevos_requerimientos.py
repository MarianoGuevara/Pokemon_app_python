from sanitizacion_string import *
from estilos import *
from funcionalidades_del_menu import *


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


def lista_datos(lista:list, parametro):
    lista_especifico = []
    for pokemon in lista:
        lista_especifico.append(pokemon[parametro])
    return set(lista_especifico)

def listar_tipos_o_habilidades(lista, parametro):
    lista_especifico = []
    for pokemon in lista:
        for habil_o_tipo in pokemon[parametro]:
            lista_especifico.append(habil_o_tipo)
    return list(set(lista_especifico))


def pedir_datos_pokemon(lista:list):
    '''
    Brief: Pide todos los datos requeridos para el nuevo pokemon
    y los agrega a una lista
    Parametros: lista: será la lista de pokemones
    Return: 
    '''
    lista_pokedex = lista_datos(lista, 'pokedex')
    lista_nombre = lista_datos(lista, 'nombre')

    lista_pokemones_inicial = []

    n_poke = pedir_int_pokemon("Ingresa n° de pokedex: ")
    if n_poke == False or n_poke in lista_pokedex:
        return False
    else:
        lista_pokemones_inicial.append(n_poke)



    nombre_poke = pedir_string("Ingresa nombre del pokemon: ")
    if nombre_poke == False or nombre_poke in lista_nombre:
        return False
    else:
        nombre_poke = nombre_poke.capitalize()
        lista_pokemones_inicial.append(nombre_poke)


    tipo_poke = input("Ingrese el/los tipos del"\
                                "pokemon separados por '/': ")
    tipo_poke = re.split("/", tipo_poke)
    for tipo in tipo_poke:  
        tipo = tipo.capitalize()
    tipo_poke = "/".join(tipo_poke)
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
    habilid_poke = habilid_poke.split("|*|")
    for habilidad in habilid_poke:  
        habilidad = habilidad.capitalize()
    habilid_poke = "|*|".join(habilid_poke)
    lista_pokemones_inicial.append(habilid_poke)    

    nuevo_poke = estilar_diccionario_pokemon_basico(ataque, 
                            defensa, lista_pokemones_inicial)
    
    lista.append(nuevo_poke)


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
            habilidades = []
            for habilidad in pokemon['habilidades']:
                habilidades.append(habilidad)
            pokemon['habilidades'] = "|*|".join(habilidades)

            tipos = []
            for tipo in pokemon['tipo']:
                tipos.append(tipo)
            pokemon['tipo'] = "/".join(tipos)

            linea = f"{pokemon['pokedex']},{pokemon['nombre']},"\
            f"{pokemon['tipo']},{(pokemon['ataque'])},"\
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
            nuevo_poke = nuevos_pokemones_a_string(lista)
            if nuevo_poke == False:
                return False
            else:
                archivo = open(ruta, "w", encoding="utf-8")
                archivo.write(nuevo_poke)
                archivo.close()
                return True
    else:
        return -5