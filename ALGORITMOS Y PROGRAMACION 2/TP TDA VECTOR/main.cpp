#include <iostream>
#include "Item.hpp"
#include "inventario.hpp"
#include "validaciones.hpp"
#include <string>
#include "menu.hpp"

using namespace std;

int main()
{
    string op;
    Menu menu;

    Inventario inventario;
    validaciones validar;
    inventario.cargar_partida();
    menu.mostrar_menu();
    op = menu.obtener_opcion();

    while (op != SALIR)
    {
        if (op == "1")
        {
            string nombre, tipo;
            cout << "Escriba el nombre del item: ";
            cin >> nombre;
            cout << "Escriba el tipo del item: ";
            cin >> tipo;
            tipo = validar.validar_tipo_item(tipo);

            Item *nuevo_item = new Item(nombre, tipo);

            inventario.agregar_item(nuevo_item);
        }
        else if (op == "2")
        {

            string item_a_eliminar;
            cout << "Escriba el  item que usted desea eliminar";

            cin >> item_a_eliminar;
            inventario.eliminar_item(item_a_eliminar);
        }
        else if (op == "3")
        {
            cout << "Este es el inventario completo" << endl;
            inventario.listar_inventario();
        }
        else if (op == "4")
        {
            cout << "Guardar inventario" << endl;
            inventario.guardar_partida();
        }
        else
        {
            cout << "La opción elegida no existe" << endl;
        }
        menu.mostrar_menu();
        op = menu.obtener_opcion();
    }
    return 0;
}
