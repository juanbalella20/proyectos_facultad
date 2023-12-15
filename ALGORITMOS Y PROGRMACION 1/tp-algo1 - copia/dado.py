from random import randint
import tablero
#pre:
#pos: se devuelve el numero del dado
def se_tira_dado()->int:
    dado=randint(1,6)
    return dado
#pre todaas las lsitas estan llenas junto con el crucigrama, lista abecedario,lista definiciones elegidas y lista palabras elegidas tienen los mismos elementos y las palabras totales y definiciones totales tambien
#pos elimina los caracteres de palabra a borrar en el crucigrama y luego elimina la palabra y su definicones de palabras totales y definiciones totales
def se_borra_una_de_las_palabras_completadas_y_se_agrega_otra(letras_acertadas:list,lista_abecedario:list,lista_palabras_elegidas:list,palabras_totales:list,definiciones_totales:list,crucigrama:list[list],lista_definiciones_elegidas:list)->None:
    indice_de_letra_al_azar=randint(0,len(letras_acertadas)-1)
    letra_al_azar=letras_acertadas[indice_de_letra_al_azar]
    indice_de_palabra_a_borrar=tablero.buscar_indice_de_letra(lista_abecedario,letra_al_azar)
    palabra_a_borrar=lista_palabras_elegidas[indice_de_palabra_a_borrar]
    definicion_a_borrar=lista_definiciones_elegidas[indice_de_palabra_a_borrar]
    lista_palabras_elegidas.pop(indice_de_palabra_a_borrar)
    lista_definiciones_elegidas.pop(indice_de_palabra_a_borrar)
    fila_y_columna=tablero.buscar_caracter_en_crucigrama(crucigrama,letra_al_azar,lista_abecedario)
    fila=fila_y_columna[0]
    columna=fila_y_columna[1]
    if 0<= indice_de_palabra_a_borrar<=5:
        for i in range(len(palabra_a_borrar)):
            crucigrama[fila+1][columna]=' '
            fila=fila+1
    elif 6<= indice_de_palabra_a_borrar<=11:
         for i in range(len(palabra_a_borrar)):
            crucigrama[fila][columna+1]=' '
            columna=columna+1
    indice_palabra_a_remplazar=randint(0,len(palabras_totales)-1)
    lista_palabras_elegidas.insert(indice_de_palabra_a_borrar, palabras_totales[indice_palabra_a_remplazar])
    lista_definiciones_elegidas.insert(indice_de_palabra_a_borrar,definiciones_totales[indice_palabra_a_remplazar])
    letras_acertadas.remove(letra_al_azar)
    palabras_totales.pop(indice_palabra_a_remplazar)
    definiciones_totales.pop(indice_palabra_a_remplazar)
    
        
#pre  las listas estan llenas y  lista palabras elegidas y lista abecedario tienen los mismo elementos
#pos muestra en la matriz todas las vocales de cada palabra de lista de palabras elegidas
def se_descrubren_todas_las_vocales(lista_palabras_elegidas:list, lista_vocales:list, crucigrama:list[list], lista_abecedario:list,letras_acertadas:list)->None:
    for i in range(len(lista_abecedario)):
        fila_y_columna=tablero.buscar_caracter_en_crucigrama(crucigrama,lista_abecedario[i],lista_abecedario)
        fila=fila_y_columna[0]
        columna=fila_y_columna[1]
        if 0<=i<=5 and lista_abecedario[i] not in letras_acertadas:
            for letra in lista_palabras_elegidas[i]:
                fila=fila+1
                if 0 <= fila < len(crucigrama) and 0 <= columna < len(crucigrama[0]):
                    if letra in lista_vocales:
                        crucigrama[fila][columna]=letra
        if 6<=i<=11 and lista_abecedario[i] not in letras_acertadas:
            for letra in lista_palabras_elegidas[i]:
                columna=columna+1
                if 0 <= fila < len(crucigrama) and 0 <= columna < len(crucigrama[0]):
                    if letra in lista_vocales:
                        crucigrama[fila][columna]=letra
                    
        

#pre recibe una lista de palabras elegidas de los mismos elementos  con losmismos elementos que la lista abecedario, una lista de listas llenos y una cadena
#pos  se añade al crucigrama la una palabra              

def se_muestra_palabra_comodin(lista_palabras_elegidas:list,crucigrama:list[list],lista_abecedario:list,letra_elegida:str)->None:
    
    indice_de_palabra=tablero.buscar_indice_de_letra(lista_abecedario,letra_elegida)
    palabra_a_mostrar=lista_palabras_elegidas[indice_de_palabra]
    fila_y_columna=tablero.buscar_caracter_en_crucigrama(crucigrama,letra_elegida,lista_abecedario)
    fila=fila_y_columna[0]
    columna=fila_y_columna[1]
    if 0<=indice_de_palabra<=5:
        tablero.imprimir_vericales(crucigrama,fila,columna,palabra_a_mostrar)
    elif 6<=indice_de_palabra<=11:
        tablero.imprimir_horizontales(crucigrama,fila,columna,palabra_a_mostrar)
        
        
        



