#ifndef INVENTARIO_H
#define INVENTARIO_H

#include "Vector.hpp"
#include <string>
#include <fstream>
using namespace std;

const int TAMANIO_MAX = 15;

class Inventario
{
private:
    Vector items;
    // PRE Se espera a que el item_a_eliminar este dentro del vector,
    // POS Devuelve la posicion del item en el vector
    size_t buscar_indice_de_item_a_eliminar(string item_a_eliminar);

public:
    // PRE se espera que el tipo de item sea PUZZLE,MUNICION o CURACION y el que el tamanio del vector sea menor a TAMANIO_MAX
    // POS agrega el item al vector items, y se suma cantidadDatos
    void agregar_item(Item *item);

    // PRE Se espera a que el item_a_eliminar este dentro del vector
    // POS elimina al item del vector
    void eliminar_item(string item_a_eliminar);

    // PRE
    // POS imrpime todos los elementos del vector items
    void listar_inventario();

    // PRE
    // POS guarda los elementos en los elemnetos en el vector
    void cargar_partida();

    // PRE
    // POS guarda los elementos en el archivo
    void guardar_partida();

    // Destructor
    ~Inventario();
};

#endif
