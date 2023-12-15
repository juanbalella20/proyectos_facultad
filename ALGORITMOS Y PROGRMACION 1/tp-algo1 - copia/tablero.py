from random import randint
import validaciones
#PRE:La longitud de lista_palabras es igual a la longitud de lista_definiciones,Todos los elementos de lista_palabras y lista_definiciones son cadenas de caracteres.
#POS: La función devuelve una tupla con dos listas, lista_palabras_elegidas y lista_definiciones_elegidas, que contienen 12 palabras elegidas al azar de lista_palabras y sus definiciones correspondientes de lista_definiciones.
#Cada palabra y su definición correspondiente en las listas de salida no se repiten.las listas de salida tienen longitud 12.

def eleccion_palabras_alazar(lista_palabras:list,lista_definiciones:list)->tuple:
    lista_palabras_elegidas=[]
    lista_definiciones_elegidas=[]
    numeros_repetidos=[]
    
    for i in range(12):
        posicion_palabra_alazar=randint(0,49)
        while posicion_palabra_alazar in numeros_repetidos:
            posicion_palabra_alazar = randint(0,49)  
        numeros_repetidos.append(posicion_palabra_alazar)          
        lista_palabras_elegidas.append(lista_palabras[posicion_palabra_alazar])
        lista_definiciones_elegidas.append(lista_definiciones[posicion_palabra_alazar])
       

    return lista_palabras_elegidas,lista_definiciones_elegidas

#PRe:se recibe un crucigrma lleno de guiones de 20x20 con una lista de palabras elegidas de 12 elementos y de mismos elemnetos la lista abecedario
#Pos: se devuelve el crucigrama con cada letra de la lista abecedario y con cada espacio en donde ira la palabra
def rellenar_crucigrama(crucigrama:list[list],lista_abecedario:list,lista_palabras_elegidas:list)-> None:
    lista_columnas_repetidas=[]
    lista_filas_repetidas=[]
    
    for i in range(len(lista_abecedario)//2):
        fila=randint(1,8)
        columna=randint(1,19)
        while columna in lista_columnas_repetidas:
            columna = randint(1,19)
            
        lista_columnas_repetidas.append(columna)          
    
        crucigrama[fila-1][columna]=lista_abecedario[i]
        for j in range(len(lista_palabras_elegidas[i])):
            crucigrama[fila][columna]=' '
            fila=fila+1
        
        
        
        
        
    for i in range(6,12):
        fila=randint(13,19)
        while fila in lista_filas_repetidas:
            fila=randint(13,19)
        lista_filas_repetidas.append(fila)
        columna=randint(1,15)
        crucigrama[fila][columna-1]=lista_abecedario[i]
        for j in range(len(lista_palabras_elegidas[i])):
            crucigrama[fila][columna]=' '
            columna=columna+1
#pre se recibe el crucigrama lleno
#pos: se imprime
def imprimir_crucigrama(crucigrama:list[list])->None:
    for fila in crucigrama:
        for elemento in fila:
            print(elemento, end=" ")
        print()
#pre se reciben 2 listas con la misma cantidad de elementos
#pos se imprime cada definicion
def imprimir_definiciones(lista_definiciones:list,lista_abecedario:list)->None:
    for i in range(len(lista_definiciones)):
        print(f"{lista_abecedario[i]}) {lista_definiciones[i]}")
#pre se recibe el crucigrama lleno con cada fla y columna de la letra del abecedrio y la palabra a llenar
#pos se añade la palabra al crucigrama verticalmente
def imprimir_vericales(crucigrama:list[list],fila:int,columna:int,palabra:str)->None:
    for letra in palabra:
        crucigrama[fila+1][columna]=letra
        fila=fila+1
#pre se recibe el crucigrama lleno con cada fla y columna de la letra del abecedrio y la palabra a llenar
#pos se añade la palabra al crucigrama horizontalmente
def imprimir_horizontales(crucigrama:list[list],fila:int,columna:int,palabra:str)->None:
    for letra in palabra:
        crucigrama[fila][columna+1]=letra
        columna=columna+1


    
#pre recibe una lista llena desde la a a la l y una letra 
#pos devuelve la posiscion de la letra
def buscar_indice_de_letra(lista_abecedario:list,letra:str)->int:
    for i in range(len(lista_abecedario)):
        if lista_abecedario[i]==letra:
            return i        
#pre recibe un lista de listas, una cadena que esta dentro de la lista de listasy otra lista, la lista de listas y la otra lista estan llenas
#pos devuelve la posicion de la cadena en la lista de listas
def buscar_caracter_en_crucigrama(crucigrama:list[list],letra_a_responder:str,lista_abecedario:list)->tuple:
    validaciones.verificar_letra_elegida(letra_a_responder,lista_abecedario)
    for fila in range(len(crucigrama)):
        for columna in range(len(crucigrama[fila])):
            if crucigrama[fila][columna] == letra_a_responder:
                return fila, columna
           