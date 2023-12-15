import tablero
import dado
import validaciones


import os
#POS: borra lo que estaba anteriormente en la matriz
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
    
#PRE:Las dos listas son listas de cadenas y tienen al menos un elemneto
#POS:elimina elementos de la lista_palabras
def eliminar_palabras_y_definiciones(lista_palabras_elegidas:list,lista_palabras:list)-> None:
    
    for palabra in lista_palabras_elegidas:
        if palabra in lista_palabras:
            lista_palabras.remove(palabra)  
    


def main():
    lista_palabras = ['PALA', 'ROJO', 'TAZA', 'COPA', 'MAMA', 'PAPA', 'HIJO', 'MIEL', 'AZUL', 'FINO',
                      'MOTO', 'PASO', 'KIEV', 'MATE', 'MASO', 'NUBE', 'FLOR', 'LAGO', 'TREN', 'PIÑA',
                      'MANI', 'RANA', 'CAMA', 'FRIO', 'LEON', 'PUMA', 'DUNA', 'FOCO', 'PELO', 'MOCO',
                      'UTIL', 'MESA', 'VINO', 'BICI', 'PIEL', 'COCA', 'FIAR', 'ARPA', 'PEON', 'FETO',
                      'GEMA', 'JUEZ', 'TIZA', 'VELA', 'ZONA', 'FASE', 'KILO', 'KIWI', 'SETA', 'AUTO']
    lista_definiciones=["Una herramienta manual utilizada para cavar o mover tierra, arena u otros materiales. ",
                        "A independiente le dicen el ",
                        "donde tomas el cafe y el te",
                        "Argentina gano la _____ del mundo del año 2023",
                        "Un término de cariño para una madre. En la serie de dibujos animados (Los Simpson), la madre de la familia",
                        "Un término de cariño para un padre. En la serie de dibujos animados (Los Simpson), el padre de la familia, Homer",
                        "Si alguien es papa de seguro tiene una hija o ",
                        "Un líquido dulce y viscoso producido por las abejas a partir del néctar de las flores",
                        "Los colres del escudo de san lorenzo son _____ y rojo",
                        "Que tiene una textura suave y delicada",
                        
                        "Un vehículo de dos ruedas con un motor que se utiliza para transportar a una o dos personas.",
                        "El acto de moverse de un lugar a otro o el espacio entre dos objetos que permite el movimiento",
                        "La capital y ciudad más grande de Ucrania",
                        "Una bebida tradicional rioplatense que se prepara con hojas secas de yerba mate y agua caliente",
                        "cuando no queres decir que te salio bien pero tmpoco mal decis ______ o menos",
                        "Una masa de vapor de agua visible en la atmósfera, que a menudo se asemeja a una forma de algodón",
                        "La parte reproductiva de una planta, que se compone de pétalos y estambres",
                        "Una masa de agua rodeada de tierra, generalmente más pequeña que un océano",
                        "Un medio de transporte que consta de vagones o coches que se mueven sobre raíles y son impulsados por una locomotora",
                        "donde vive bob esponja",
                        
                        "Una semilla comestible de una planta originaria de América del Sur, también conocida como cacahuete",
                        "Un anfibio de piel suave que se caracteriza por sus patas traseras largas y su habilidad para saltar",
                        "Un mueble utilizado para dormir, que se compone de un marco y un colchón",
                        "Una sensación de baja temperatura o falta de calor, opuesta al calor",
                        "Un felino grande y fuerte, conocido por su melena y su habilidad para cazar en grupo",
                        "Un felino de América del Norte, también conocido como león de montaña o cougar, que es ágil y tiene una buena capacidad de salto",
                        "Una colina de arena o tierra que se forma por la acción del viento",
                        "Un dispositivo de iluminación que concentra la luz en una dirección específica",
                        "Una estructura filamentosa que crece en la piel de los mamíferos, que les protege del frío y ayuda en la percepción sensorial",
                        "sustancia viscosa y pegajosa que se produce en las membranas mucosas de las cavidades nasales, los senos paranasales y otras partes del cuerpo para proteger y lubricar estas áreas",
                        
                        "Algo que es práctico o beneficioso para realizar una tarea o alcanzar un objetivo",
                        "Un mueble plano y horizontal, que se utiliza para colocar objetos o para comer",
                        "Una bebida alcohólica que se produce mediante la fermentación del jugo de uva",
                        "Abreviatura de bicicleta, un vehículo de dos ruedas impulsado por pedales que se utiliza para el transporte y el ejercicio",
                        "La capa externa del cuerpo de los animales vertebrados, que los protege del medio ambiente",
                        "la bebida favorita de papa noel es la ____ cola",
                        "Confiar en que alguien cumpla una promesa de pago en el futuro.",
                        "Un instrumento musical de cuerda, con una forma triangular y un conjunto de cuerdas que se tocan con los dedos",
                        "Un trabajador manual que realiza tareas básicas y rutinarias",
                        "El ser humano o animal en desarrollo desde la octava semana de gestación hasta el momento del nacimiento",
                       
                        "Es una piedra preciosa, generalmente transparente y de colores brillantes",
                        "Es una persona encargada de impartir justicia en un tribunal o juzgado",
                        "Es un trozo de carbonato de calcio utilizado para escribir en una pizarra o en una superficie similar",
                        "Es un objeto que se utiliza para proporcionar luz",
                        "Es un área geográfica o un espacio físico definido que tiene características específicas",
                        "Es un periodo específico en un proceso o ciclo",
                        "Es una unidad de medida de masa que equivale a mil gramos",
                        "Es una fruta pequeña y redonda con una piel marrón y peluda y una pulpa verde y jugosa",
                        "Es un tipo de hongo con un sombrero y un tallo característicos",
                        "vehículo de motor diseñado para transportar personas o bienes por carretera"
                       
        
    ]
    tupla_de_palabras_y_definiciones=tablero.eleccion_palabras_alazar(lista_palabras,lista_definiciones)
    lista_palabras_elegidas=tupla_de_palabras_y_definiciones[0]
    
    
    lista_definiciones_elegidas=tupla_de_palabras_y_definiciones[1]
    eliminar_palabras_y_definiciones(lista_palabras_elegidas,lista_palabras)
    eliminar_palabras_y_definiciones(lista_definiciones_elegidas,lista_definiciones)
    lista_abecedario=["a","b","c","d","e","f","g","h","i","j","k","l"]
    lista_vocales=["A","E","I","O","U"]
    lista_de_letras_acertadas=[]
    fila_y_columna=[]
    lista_palabras_adivinadas=[]
    contador=0
    numero_dado=0
    
    crucigrama = []
    for i in range(20):
        fila = []
        for j in range(20):
            fila.append('-')
        crucigrama.append(fila)    
    rellenar_crucigrama=tablero.rellenar_crucigrama(crucigrama,lista_abecedario,lista_palabras_elegidas)
    
    while contador<12 and numero_dado!=6:
        print()
        tablero.imprimir_crucigrama(crucigrama)
        tablero.imprimir_definiciones(lista_definiciones_elegidas,lista_abecedario)
        letra_a_responder=input("Escribe la letra, que marca cada definicion, que quieres responder primero: ")
        letra_a_responder=validaciones.verificar_letra_elegida(letra_a_responder,lista_abecedario)
        fila_y_columna=tablero.buscar_caracter_en_crucigrama(crucigrama,letra_a_responder,lista_abecedario)
        fila=fila_y_columna[0]  
        columna=fila_y_columna[1]
        indice_de_palabra=tablero.buscar_indice_de_letra(lista_abecedario,letra_a_responder)
        palabra_respondida=input("Escribe la palabra que crees que corresponde a ese lugar: ").upper()
  
        if palabra_respondida == lista_palabras_elegidas[indice_de_palabra]:
            if palabra_respondida not in lista_palabras_adivinadas:
                contador=contador+1
                lista_palabras_adivinadas.append(palabra_respondida)
            
            lista_de_letras_acertadas.append(letra_a_responder)
            if 0<=indice_de_palabra<=5:
                tablero.imprimir_vericales(crucigrama,fila,columna,palabra_respondida)
            elif 6<=indice_de_palabra<=11:
                tablero.imprimir_horizontales(crucigrama,fila,columna,palabra_respondida)
        elif palabra_respondida != lista_palabras_elegidas[indice_de_palabra] :
            numero_dado=dado.se_tira_dado()
            
            if numero_dado ==1 or numero_dado==2:
                if len(lista_de_letras_acertadas) >0:
                    contador=contador-1
                    dado.se_borra_una_de_las_palabras_completadas_y_se_agrega_otra(lista_de_letras_acertadas,lista_abecedario,lista_palabras_elegidas,lista_palabras,lista_definiciones,crucigrama,lista_definiciones_elegidas)
            elif numero_dado == 3 or numero_dado == 4:
                dado.se_descrubren_todas_las_vocales(lista_palabras_elegidas,lista_vocales,crucigrama,lista_abecedario,lista_de_letras_acertadas)
            elif numero_dado == 5:
                letra_de_palabra_comodin = input("Escribe la letra que quieres que se muestre: ")
                letra_de_palabra_comodin = validaciones.verificar_letra_elegida(letra_de_palabra_comodin, lista_abecedario)
                if palabra_respondida not in lista_palabras_adivinadas:
                    contador = contador + 1
                    lista_palabras_adivinadas.append(palabra_respondida)
                lista_de_letras_acertadas.append(letra_de_palabra_comodin)
                dado.se_muestra_palabra_comodin(lista_palabras_elegidas,crucigrama,lista_abecedario,letra_de_palabra_comodin)
        clear_screen()
        print(f"Por ahora vas adivinadas {contador} palabras")
            
        
        
            
              
    
    tablero.imprimir_crucigrama(crucigrama)
    if contador == 12:
        print("GANASTEEE")
    elif numero_dado == 6:
        print("PERDISTEEE")
    
    
    
    
    
    

        
main()