###  I  M P O R T S
from colorama import *
from sortedlist_class import *
import helpers
from menu_class import *
from parsestr_class import *
from dijkstraflag_class import *

#
#   F U N C I O N E S
#

def mostrar_resultado(descripcion, resultado):
    print(Fore.WHITE + "> " + descripcion + Fore.YELLOW, resultado, Fore.WHITE)



def busqueda_dicotomica():   
    #Creamos una lista vacia de la nueva clase que incorpora la búsqueda dicotómica
    mi_lista = SortedList()

    # Añadimos elementos de ejemplo a la lista
    mi_lista.append("Uno")
    mi_lista.append("Dos")
    mi_lista.append("Tres")
    mi_lista.append("Cuatro")
    mi_lista.append("Cinco")
    mi_lista.append("Seis")
    mi_lista.append("Siete")
    mi_lista.append("Ocho")
    mi_lista.append("Nueve")
    mi_lista.append("Diez")
    print("Mi lista", mi_lista)

    # Hacemos unas cuantas búsqueda de ejemplo
    mostrar_resultado("Posición de 'Tres'", mi_lista.dichotomic_index("Tres"))
    mostrar_resultado("Posición del '1'", mi_lista.dichotomic_index("1"))
    mostrar_resultado("Posición del 'Dos'", mi_lista.dichotomic_index("Dos"))
    mostrar_resultado("Posición del 'Diez'", mi_lista.dichotomic_index("Diez"))
    mostrar_resultado("Posición del 'Uno'", mi_lista.dichotomic_index("Uno"))

def palindromos():
    # Ejemplo 1
    mi_cadena = ParseStr("Hola esto es una prueba")
    print("Frase de prueba 1 (" + str(len(mi_cadena)) + ") " +
          Fore.YELLOW + mi_cadena + Fore.WHITE)
    mostrar_resultado("Frase normalizada (" +
                      str(len(mi_cadena.normalized_str)) + ") ",  mi_cadena.normalized_str)
    mostrar_resultado("Es palindromo (iterativo)",
                      mi_cadena.is_palindrome_iterative())
    mostrar_resultado("Es palindromo (recursivo)",
                      mi_cadena.is_palindrome_recursive())
    print()

    # Ejemplo 2
    mi_cadena = ParseStr("Logré ver gol")
    print("Frase de prueba 2 (" + str(len(mi_cadena)) + ") " +
          Fore.YELLOW + mi_cadena + Fore.WHITE)
    mostrar_resultado("Frase normalizada (" +
                      str(len(mi_cadena.normalized_str)) + ") ",  mi_cadena.normalized_str)
    mostrar_resultado("Es palindromo (iterativo",
                      mi_cadena.is_palindrome_iterative())
    mostrar_resultado("Es palindromo (recursivo)",
                      mi_cadena.is_palindrome_recursive())
    print()

    # Ejemplo 3
    mi_cadena = ParseStr("Dábale arroz a la zorra el abad")
    print("Frase de prueba 3 (" + str(len(mi_cadena)) + ") " +
          Fore.YELLOW + mi_cadena + Fore.WHITE)
    mostrar_resultado("Frase normalizada (" +
                      str(len(mi_cadena.normalized_str)) + ") ",  mi_cadena.normalized_str)
    mostrar_resultado("Es palindromo (iterativo)",
                      mi_cadena.is_palindrome_iterative())
    mostrar_resultado("Es palindromo (recursivo)",
                      mi_cadena.is_palindrome_recursive())

def dijkstra_flag():
    flag = DijkstraFlag()

    flag.add_color(Color.BLUE)
    flag.add_color(Color.BLUE)
    flag.add_color(Color.RED)
    flag.add_color(Color.GREEN)
    flag.add_color(Color.RED)
    flag.add_color(Color.BLUE)
    flag.add_color(Color.GREEN)
    flag.add_color(Color.BLUE)
    flag.add_color(Color.BLUE)
    flag.add_color(Color.RED)
    flag.add_color(Color.RED)
    flag.add_color(Color.BLUE)
    flag.add_color(Color.BLUE)
    flag.add_color(Color.GREEN)
    flag.add_color(Color.RED)

    mostrar_resultado(
        "Bandera sin ordenar (" + str(len(flag)) + ")", flag.get_flag_str())

    flag.sort(True)

    mostrar_resultado(
        "Bandera ordenada        ", flag.get_flag_str())



#
#   I N I C I O   P R O G R A M A
#

helpers.clear()  # Limpia la terminal

mi_menu = Menu("TAREAS RECURSIVIDAD")
mi_menu.addOption("Búsqueda dicotómica recursiva", busqueda_dicotomica)
mi_menu.addOption("Palíndromos", palindromos)

mi_menu.start()