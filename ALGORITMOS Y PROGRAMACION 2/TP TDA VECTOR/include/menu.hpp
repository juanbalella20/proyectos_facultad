#ifndef MENU_H
#define MENU_H

#include <string>
using namespace std;
const int MAX_MENU = 5;
const string SALIR = "5";

class Menu
{
private:
    string opciones[MAX_MENU];

public:
    // constructor
    Menu();

    // PRE
    // POS muestra el menu
    void mostrar_menu();

    // PRE
    // POS devuelve la opcion elegida por el usuario
    string obtener_opcion();
};
#endif