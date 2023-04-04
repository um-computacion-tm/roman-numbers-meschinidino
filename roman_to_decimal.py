import unittest

ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_decimal(romano):
    # inicia el total en 0
    total = 0
    for letra in romano:
        # si  total todavia es 0, el anterior es el primer digito, para inicializar variable
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


class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, 1)

    def test_IV(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado, 4)

    def test_VII(self):
        resultado = roman_to_decimal("VII")
        self.assertEqual(resultado, 7)

    def test_IX(self):
        resultado = roman_to_decimal("IX")
        self.assertEqual(resultado, 9)

    def test_X(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado, 10)

    def test_XVII(self):
        resultado = roman_to_decimal("XVII")
        self.assertEqual(resultado, 17)

    def test_XXII(self):
        resultado = roman_to_decimal("XXII")
        self.assertEqual(resultado, 22)

    def test_XLIV(self):
        resultado = roman_to_decimal("XLIV")
        self.assertEqual(resultado, 44)

    def test_LV(self):
        resultado = roman_to_decimal("LV")
        self.assertEqual(resultado, 55)

    def test_LXX(self):
        resultado = roman_to_decimal("LXXVII")
        self.assertEqual(resultado, 77)

    def test_CXI(self):
        resultado = roman_to_decimal("CXI")
        self.assertEqual(resultado, 111)

    def test_CCXXII(self):
        resultado = roman_to_decimal("CCXXII")
        self.assertEqual(resultado, 222)

    def test_CCCXXXIII(self):
        resultado = roman_to_decimal("CCCXXXIII")
        self.assertEqual(resultado, 333)

    def test_CDXLIV(self):
        resultado = roman_to_decimal("CDXLIV")
        self.assertEqual(resultado, 444)

    def test_DLV(self):
        resultado = roman_to_decimal("DLV")
        self.assertEqual(resultado, 555)

    def test_DCLXVI(self):
        resultado = roman_to_decimal("DCLXVI")
        self.assertEqual(resultado, 666)

    def test_CMXCIX(self):
        resultado = roman_to_decimal("CMXCIX")
        self.assertEqual(resultado, 999)


if __name__ == '__main__':
    unittest.main()
