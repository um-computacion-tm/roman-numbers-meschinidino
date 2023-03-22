#Programa que convierte decimal a romano
import unittest
def decimal_to_roman(decimal):
    return generar_numero(decimal)
def generar_numero(decimal):
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
    decimal = int(str(numero)[0])
    if decimal <= 3:
        return "C" * decimal
    if decimal == 4:
        return "CD"
    else:
        if decimal > 8:
            return ((10 - decimal) * "C") + "D"
        if decimal <= 8:
            return "D" + ((decimal - 5) * "C")
def cuatro_digitos(numero):
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
class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, "I")
    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")
    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, "V")
    def test_siete(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, "VII")
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, "IV")
    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, "IX")
    def test_treinta(self):
        resultado = decimal_to_roman(30)
        self.assertEqual(resultado, "XXX")
    def test_cuarentaycuatro(self):
        resultado = decimal_to_roman(44)
        self.assertEqual(resultado, "XLIV")
    def test_setentaysiete(self):
        resultado = decimal_to_roman(77)
        self.assertEqual(resultado, "LXXVII")
    def test_noventaynueve(self):
        resultado = decimal_to_roman(99)
        self.assertEqual(resultado, "XCIX")
    def test_cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, "C")
    def test_quinientoscincuentaycinco(self):
        resultado = decimal_to_roman(555)
        self.assertEqual(resultado, "DLV")
    def test_5555(self):
        resultado = decimal_to_roman(5555)
        self.assertEqual(resultado, "V*DLV")
if __name__ == "__main__":
    unittest.main()