#ifndef VALIDACIONES_H
#define VALIDACIONES_H

#include <string>
#include "Item.hpp"
using namespace std;

class validaciones
{
public:
    // PRE Se espera que el tipo de item sea tal cual escrito  MUNICION, CURATIVO o PUZZLE
    // POS deuelve el item verificado
    string validar_tipo_item(string tipo);
};
#endif