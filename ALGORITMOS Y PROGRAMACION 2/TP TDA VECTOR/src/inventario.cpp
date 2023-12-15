#include "Inventario.hpp"
#include <iostream>

using namespace std;

size_t Inventario::buscar_indice_de_item_a_eliminar(string item_a_eliminar)
{
    size_t indice;
    for (size_t i = 0; i < items.tamanio(); i++)
    {
        if (*items[i] == item_a_eliminar)
        {
            indice = i;
            return indice;
        }
    }
    return 20;
}

void Inventario::agregar_item(Item *item)
{
    if (items.tamanio() <= TAMANIO_MAX)
    {
        items.alta(item);
        cout << "Item agregado al inventario,recuerda guardar el inventario, por lo contrario perderas los cambios" << endl;
    }
    else
    {

        cout << "El inventario está lleno, no se puede agregar más items." << endl;
    }
}

void Inventario::eliminar_item(string item_a_eliminar)
{
    size_t indice;

    indice = buscar_indice_de_item_a_eliminar(item_a_eliminar);
    if (indice != 20)
    {
        Item *item_eliminado = items.baja(indice);
        cout << "el siguiente item sera eliminado, recuerda guardar el inventario, por lo contrario perderas los cambios: ";
        item_eliminado->listarInformacion();
        delete item_eliminado;
    }
    else
    {
        cout << "el elemento buscado no fue encontrado";
    }
}

void Inventario::listar_inventario()
{
    cout << "Inventario:" << std::endl;
    for (size_t i = 0; i < items.tamanio(); i++)
    {
        cout << i + 1 << ") ";
        items[i]->listarInformacion();
        cout << endl;
    }
}

void Inventario::cargar_partida()
{
    ifstream archivo("savefile.csv");
    string item_entero;
    while (getline(archivo, item_entero))
    {
        bool coma_no_encontrada = true;
        string nombre;
        string tipo;
        for (size_t i = 0; i < item_entero.size(); i++)
        {
            if (item_entero[i] != ',' && coma_no_encontrada == true)
            {
                nombre = nombre + item_entero[i];
            }
            else if (item_entero[i] != ',' && coma_no_encontrada == false)
            {
                tipo = tipo + item_entero[i];
            }
            else if (item_entero[i] == ',')
            {
                coma_no_encontrada = false;
            }
        }
        Item *nuevo_item = new Item(nombre, tipo);
        agregar_item(nuevo_item);
    }
    archivo.close();
}

void Inventario::guardar_partida()
{
    ofstream archivo("savefile.csv");

    for (size_t i = 0; i < items.tamanio(); i++)
    {
        archivo << *(items[i]) << endl;
    }

    archivo.close();
}

Inventario::~Inventario()
{

    for (size_t i = 0; i < items.tamanio(); i++)
    {
        delete items[i];
    }
}