#include "Menu.hpp"
using namespace std;

void Menu::imprimir_opciones()
{
    cout << "1. Mover personaje." << endl;
    cout << "2. Mostrar mejor recorrido." << endl;
    cout << "3. Recorrer mejor camino." << endl;
    cout << "4. Manejo de armas." << endl;
    cout << "5. Mostrar puntaje." << endl;
    cout << "6. Salir." << endl;
}

void Menu::termino_nivel(size_t &altura_arbol){
    if (personaje.nivel_terminado(interfaz))
    {
        altura_arbol = personaje.get_altura();
        if (altura_arbol == 0)
        {
            altura_arbol++;
        }
        interfaz.inicializar_tablero(altura_arbol);
    }
}

void Menu::flujo_juego()
{
    char opcion;
    size_t altura_arbol = personaje.get_altura();
    interfaz.inicializar_tablero(altura_arbol);
    vector<size_t> posicion_james1;
    vector<vector<size_t>> posicion_pyramidheads;
    bool tiene_arma;
    vector<vector<size_t>> coordenadas_camino_minimo;
    size_t puntaje_camino_minimo = 0;
    size_t puntaje_james = 0;
    size_t puntaje_total = 0;
    while (opcion != SALIR && interfaz.estado_juego(altura_arbol, tiene_arma) == 0)
    {
        interfaz.imprimir_tablero(TABLERO_1);
        imprimir_opciones();
        cout << "Ingrese una opcion: ";
        cin >> opcion;
        cout << endl;
        switch (opcion)
        {
        case MOVER_JUGADOR:
            personaje.interaccion_personaje(MOVER_PERSONAJE, interfaz);

            if (personaje.eliminar_pyramid_head(interfaz))
            {
                posicion_pyramidheads = personaje.obtener_posicion_pyramidhead(interfaz);
                interfaz.actualizar_tablero(posicion_pyramidheads[0][0], posicion_pyramidheads[0][1], ESPACIO_LIBRE);
                interfaz.actualizar_tablero(posicion_pyramidheads[1][0], posicion_pyramidheads[1][1], ESPACIO_LIBRE);
            }
            puntaje_james = personaje.obtener_puntaje_total();
            puntaje_total += puntaje_james;
            break;

        case MOSTRAR_MEJOR_RECORRIDO:
            posicion_james1 = personaje.obtener_posicion_james(interfaz);
            posicion_pyramidheads = personaje.obtener_posicion_pyramidhead(interfaz);
            tiene_arma = personaje.get_tiene_arma();
            coordenadas_camino_minimo = recorrido.encontrar_camino_minimo(posicion_james1, posicion_pyramidheads, altura_arbol, tiene_arma).first;
            interfaz.mostrar_coordenadas_camino_minimo(coordenadas_camino_minimo);
            cout << endl;
            cout << "-----------------------" << endl;
            break;

        case RECORRER_MEJOR_CAMINO:
            posicion_james1 = personaje.obtener_posicion_james(interfaz);
            posicion_pyramidheads = personaje.obtener_posicion_pyramidhead(interfaz);
            puntaje_camino_minimo = recorrido.encontrar_camino_minimo(posicion_james1, posicion_pyramidheads, altura_arbol, tiene_arma).second;
            puntaje_total += puntaje_camino_minimo;
            interfaz.terminar_nivel_automaticamente(posicion_james1);
            break;

        case MANEJO_ARMAS:
            personaje.interaccion_personaje(MANEJO_ARMAS, interfaz);
            tiene_arma = personaje.get_tiene_arma();
            break;

        case MOSTRAR_PUNTAJE:
            cout << "El puntaje actual es " << puntaje_total << endl;
            break;

        case SALIR:
            cout << "Gracias por jugar!" << endl;
            break;
        default:
            cout << "La opcion ingresada no es valida." << endl;
            break;
        }
        termino_nivel(altura_arbol);
    }
    if (interfaz.estado_juego(altura_arbol, tiene_arma) == 1)
    {
        cout << "Ganaste!" << endl;
        cout << "El puntaje final es " << puntaje_total << endl;
    }
    else if (interfaz.estado_juego(altura_arbol, tiene_arma) == 2)
    {
        cout << "Perdiste! No hay un camino posible" << endl;
        interfaz.imprimir_tablero(TABLERO_1);
    }
}
