
from random import randint
#pre se recibe una letra con una lista de abecedario llena
#pos devuelve la letra hasta que este en la lista
def verificar_letra_elegida(letra:str,lista_abecedario:list)->str:
    while letra not in lista_abecedario:
        letra=input("Esa letra no es opcion, por favor intente de nuevo: ")
    return letra