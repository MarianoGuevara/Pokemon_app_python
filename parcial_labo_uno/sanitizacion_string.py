import re

def reemplazar_tildes(string:str)->str:
    '''
    Brief: Recorre un string y si tiene tilde, se la saca
    Parametros: String: Un string a analizar
    Return: Devuelve el mismo sin tíldes
    '''
    for letra in string:
        if letra == "á":
            string = re.sub("á", "a", string)
        elif letra == "é":
            string = re.sub("é", "e", string)
        elif letra == "í":
            string = re.sub("í", "i", string)
        elif letra == "ó":
            string = re.sub("ó", "o", string)
        elif letra == "ú":
            string = re.sub("ú", "u", string)    
    return string


def reemplazar_caracter_especial_y_low(string:str)->str:
    '''
    Brief: Hace una lista y luego une todos los caracteres
    de un string segun un regex
    Parametros: string: Un string a analizar
    Return: Devuelve el string sin caracts especiales
    '''
    string = re.findall("[a-z|A-Z| ]+", string)
    string = "".join(string)
    string = string.lower()
    return string


def sanitizar_string(string:str)->str:
    '''
    Brief: Recibibe un string y lo sanitiza haciendo uso 
    de las 2 funciones correspondientes para ello
    Parametros: string: Recibe un string a analizar
    Return: El string sanitizado
    '''
    string = reemplazar_tildes(string)
    string = reemplazar_caracter_especial_y_low(string)
    return string

