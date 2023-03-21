#Programa que convierte decimal a romano
import unittest
def decimal_to_roman(decimal):

def un_digito(numero):
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
    return letra
def tres_digitos(numero):
    return letra
def cuaatro_digitos(numero):
    return letra

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
if __name__ == "__main__":
    unittest.main()