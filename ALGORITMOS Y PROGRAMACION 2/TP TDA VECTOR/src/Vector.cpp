#include "Vector.hpp"

Vector::Vector() : datos(nullptr), cantidadDatos(0), tamanioMaximo(0) {}

void Vector::alta(Item *dato)
{
    if (cantidadDatos == tamanioMaximo)
    {
        size_t tamanio_actualizado;
        if (tamanioMaximo == 0)
        {
            tamanio_actualizado = 1;
        }
        else
        {
            tamanio_actualizado = tamanioMaximo * 2;
        }

        Item **nuevo_datos = new Item *[tamanio_actualizado];

        for (size_t i = 0; i < cantidadDatos; i++)
        {
            nuevo_datos[i] = datos[i];
        }

        delete[] datos;
        datos = nuevo_datos;
        tamanioMaximo = tamanio_actualizado;
    }

    datos[cantidadDatos] = dato;
    cantidadDatos++;
}

void Vector::alta(Item *dato, size_t indice)
{
    if (indice > cantidadDatos)
    {
        throw VectorException();
    }

    if (cantidadDatos == tamanioMaximo)
    {
        size_t tamanio_actualizado;
        if (tamanioMaximo == 0)
        {
            tamanio_actualizado = 1;
        }
        else
        {
            tamanio_actualizado = tamanioMaximo * 2;
        }
        Item **nuevo_datos = new Item *[tamanio_actualizado];

        for (size_t i = 0; i < indice; i++)
        {
            nuevo_datos[i] = datos[i];
        }

        nuevo_datos[indice] = dato;

        for (size_t i = indice; i < cantidadDatos; i++)
        {
            nuevo_datos[i + 1] = datos[i];
        }

        delete[] datos;
        datos = nuevo_datos;
        tamanioMaximo = tamanio_actualizado;
    }
    else
    {
        for (size_t i = cantidadDatos; i > indice; i--)
        {
            datos[i] = datos[i - 1];
        }

        datos[indice] = dato;
    }

    cantidadDatos++;
}

Item *Vector::baja()
{
    if (cantidadDatos == 0)
    {
        throw VectorException();
    }

    Item *elemento_eliminado = datos[cantidadDatos - 1];
    cantidadDatos--;

    if (cantidadDatos == 0)
    {
        tamanioMaximo = 0;
        delete[] datos;
        datos = nullptr;
    }
    else if (cantidadDatos == tamanioMaximo / 2)
    {
        tamanioMaximo /= 2;
        Item **nuevosDatos = new Item *[tamanioMaximo];
        for (size_t i = 0; i < cantidadDatos; i++)
        {
            nuevosDatos[i] = datos[i];
        }
        delete[] datos;
        datos = nuevosDatos;
    }

    return elemento_eliminado;
}

Item *Vector::baja(size_t indice)
{
    if (indice >= cantidadDatos)
    {
        throw VectorException();
    }

    Item *elemento_eliminado = datos[indice];

    for (size_t i = indice; i < cantidadDatos - 1; i++)
    {
        datos[i] = datos[i + 1];
    }

    cantidadDatos--;
    if (cantidadDatos == 0)
    {
        tamanioMaximo = 0;
        delete[] datos;
        datos = nullptr;
    }
    else if (cantidadDatos == tamanioMaximo / 2)
    {
        tamanioMaximo /= 2;
        Item **nuevosDatos = new Item *[tamanioMaximo];
        for (size_t i = 0; i < cantidadDatos; i++)
        {
            nuevosDatos[i] = datos[i];
        }
        delete[] datos;
        datos = nuevosDatos;
    }

    return elemento_eliminado;
}

bool Vector::vacio()
{
    return cantidadDatos == 0;
}

size_t Vector::tamanio()
{
    return cantidadDatos;
}

Item *&Vector::operator[](size_t indice)
{
    if (indice < 0 || indice >= cantidadDatos)
    {
        throw VectorException();
    }

    return datos[indice];
}

Vector::~Vector()
{
    delete[] datos;
}
