#Programa que convierte decimal a romano
import unittest
def decimal_to_roman(decimal):
    if decimal <= 3:
        return "I" * decimal
    if decimal == 4:
        return "IV"
    else:
        if decimal > 8:
            return ((10 - decimal) * "I") + "X"
        if decimal <= 8:
            return "V" + ((decimal - 5) * "I")
    

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

if __name__ == "__main__":
    unittest.main()