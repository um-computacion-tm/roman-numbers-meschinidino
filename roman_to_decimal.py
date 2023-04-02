import unittest

def roman_to_decimal(romano):
    centenas = ["C",  "D", "M"]
    decenas = ["X", "L"]
    unidades = ["I", "V"]
    total = 0
    for letra in romano:
        if total == 0:
            anterior = romano[0]
        if letra in centenas:
            if letra == "M":
                if anterior == "C":
                    total -= 200
                total += 1000
            if letra == "C":
                if anterior == "X":
                    total -= 20
                total += 100
            if letra == "D":
                if anterior == "C":
                    total -= 200
                total += 500
        if letra in decenas:
            if letra == "X":
                if anterior == "I":
                    total -= 2
                total += 10
            if letra == "L":
                if anterior == "X":
                    total -= 20
                total += 50
        if letra in unidades:
            if letra == "I":
                total += 1
            if letra == "V":
                if anterior == "I":
                    total -= 2
                total += 5
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