# parcial1_laboratorio1_python_pokemones
-Primer parcial de la materia laboratorio hecho con Python
(por consola)

CONSIGNA
Necesitamos crear un programa para poder gestionar nuestra mochila de
pokemones en PokemonGo.
Para ello disponemos de un archivo csv con el siguiente formato:
N° Pokedex,Nombre,Tipo,Poder de Ataque,Poder de Defensa,Habilidades
Por ejemplo:
149,Dragonite,Dragón/Volador,134,95,Enjambre|*|Cambio color
Consignas a desarrollar
Realizar un menú que permita al usuario trabajar con las siguientes opciones:
1. Traer datos desde archivo: guardará el contenido del archivo
pokemones.csv en una colección. Tener en cuenta que tanto tipos y
habilidades deben estar guardadas en algún tipo de colección, debido a que
un pokemón puede tener más de un tipo y más de una habilidad.
2. Listar cantidad por tipo: mostrará todos los tipos indicando la cantidad de
pokemones que corresponden a ese tipo.
3. Listar pokemones por tipo: mostrará cada tipo indicando el nombre y poder
de ataque de cada pokemon que corresponde a ese tipo.
4. Listar pokemones por habilidad: el usuario ingresa la descripción de una
habilidad y el programa deberá mostrar nombre, tipo y promedio de poder
entre ataque y defensa.
5. Listar pokemones ordenados: mostrará todos los datos de los pokemones
ordenados por poder de ataque y en caso de coincidir en el valor, por nombre
de la A-Z.
6. Guardar Json: Generará un archivo de tipo Json con los pokemones de un
tipo específico (lo ingresa el usuario). En el mismo se guardará el nombre del
pokemon, el mayor valor entre los puntos de ataque y defensa, y por último el
tipo de poder. Por ejemplo:
012,Butterfree,Bicho,Volador,167,137
Butterfree-167-”Ataque”
014,Kakuna,Bicho,Veneno,46,75
Kakuna-75-”Defensa”
048,Venonat,Bicho,Veneno,100,100
Venonat-100-”Ambos”
7. Leer Json: permitirá mostrar un listado con los pokemones guardados en el
archivo Json de la opción 5.
8. Salir del program
