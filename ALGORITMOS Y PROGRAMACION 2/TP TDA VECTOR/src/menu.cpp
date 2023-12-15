#include "Menu.hpp"
#include <iostream>

using namespace std;

Menu::Menu()
{
    this->opciones[0] = "Agregar item";
    this->opciones[1] = "Eliminar item";
    this->opciones[2] = "Listar inventario";
    this->opciones[3] = "Guardar inventario";
    this->opciones[4] = "Salir";
}

void Menu::mostrar_menu()
{
    cout << "-------------------------------" << endl;
    for (size_t i = 0; i < MAX_MENU; i++)
    {
        cout << i + 1 << ") " << opciones[i] << endl;
    }
    cout << "-------------------------------" << endl;
}

string Menu::obtener_opcion()
{
    string opcion;
    cout << "Elija una opción: ";
    cin >> opcion;
    return opcion;
}
