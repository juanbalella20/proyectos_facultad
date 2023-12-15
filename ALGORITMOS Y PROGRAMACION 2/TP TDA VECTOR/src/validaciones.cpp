#include "validaciones.hpp"
#include <iostream>

string validaciones::validar_tipo_item(string tipo)
{

    while (tipo != TIPO_CURATIVO && tipo != TIPO_MUNICION && tipo != TIPO_PUZZLE)
    {
        cout << "Ese tipo de item no existe, escribe uno apropiado por favor: " << endl;
        cin >> tipo;
    }
    return tipo;
}
