import unittest

ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_decimal(romano):
    # inicia el total en 0
    total = 0
    for letra in romano:
        # si  total todavia es 0, el anterior es el primer digito, para inicializar variable de comparacion
        if total == 0:
            anterior = romano[0]
        # si el anterior es cien y el valor actual es mil o quinientos, suma ese monto, pero
        # corrige el extra del anterior restando 200
        if anterior == "C" and (letra == "D" or letra == "M"):
            total -= 200
        # igual al caso anterior, resta la diferencia
        if anterior == "X" and (letra == "L" or letra == "C"):
            total -= 20
        if anterior == "I" and (letra == "V" or letra == "X"):
            total -= 2
        # una vez restado el monto correspondiente, suma el valor de la letra
        total += ROMANOS[letra]
        # asigna letra actual al anterior para futuras comparaciones
        anterior = letra
    return total