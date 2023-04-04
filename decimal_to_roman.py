# Programa que convierte decimal a romano
import unittest


def decimal_to_roman(decimal):
    return generar_numero(decimal)


def generar_numero(decimal):
    # usa diferentes funciones para componer un numero según su cantidad de dígitos
    # empieza desde 4 dígitos, convierte de izquierda a derecha
    numero = str(decimal)
    if len(numero) == 4:
        mil = cuatro_digitos(decimal)
        decimal = int(numero[1:])
        centena = tres_digitos(decimal)
        decimal = int(numero[2:])
        decena = dos_digitos(decimal)
        decimal = int(numero[-1])
        unidad = un_digito(decimal)
        return mil + centena + decena + unidad
    if len(numero) == 3:
        centena = tres_digitos(decimal)
        decimal = int(numero[1:])
        decena = dos_digitos(decimal)
        decimal = int(numero[-1])
        unidad = un_digito(decimal)
        return centena + decena + unidad
    if len(numero) == 2:
        decena = dos_digitos(decimal)
        decimal = int(numero[-1])
        unidad = un_digito(decimal)
        return decena + unidad
    if len(numero) == 1:
        return un_digito(decimal)


def un_digito(decimal):
    # convierte números del 1-9
    if decimal <= 3:
        return "I" * decimal
    if decimal == 4:
        return "IV"
    else:
        if decimal > 8:
            return ((10 - decimal) * "I") + "X"
        if decimal <= 8:
            return "V" + ((decimal - 5) * "I")


def dos_digitos(numero):
    # convierte números del 10-99
    decimal = int(str(numero)[0])
    if decimal <= 3:
        return "X" * decimal
    if decimal == 4:
        return "XL"
    else:
        if decimal > 8:
            return ((10 - decimal) * "X") + "C"
        if decimal <= 8:
            return "L" + ((decimal - 5) * "X")


def tres_digitos(numero):
    # convierte números del 100 - 999
    decimal = int(str(numero)[0])
    if decimal <= 3:
        return "C" * decimal
    if decimal == 4:
        return "CD"
    else:
        if decimal > 8:
            return ((10 - decimal) * "C") + "M"
        if decimal <= 8:
            return "D" + ((decimal - 5) * "C")


def cuatro_digitos(numero):
    # convierte números del 1000 - 9999
    decimal = int(str(numero)[0])
    if decimal <= 3:
        return "M" * decimal
    if decimal == 4:
        return "IV" + "*"
    else:
        if decimal > 8:
            return ((10 - decimal) * "I") + "X" + "*"
        if decimal <= 8:
            return "V" + ((decimal - 5) * "I" + "*")