import unittest

from tps.roman_numbers.decimal_to_roman import decimal_to_roman
from tps.roman_numbers.roman_to_decimal import roman_to_decimal


class MyTest(unittest.TestCase):
    def test_uno(self):
        self.assertEqual(decimal_to_roman(1), "I")

    def test_diez(self):
        self.assertEqual(decimal_to_roman(10), "X")

    def test_cinco(self):
        self.assertEqual(decimal_to_roman(5), "V")

    def test_siete(self):
        self.assertEqual(decimal_to_roman(7), "VII")

    def test_cuatro(self):
        self.assertEqual(decimal_to_roman(4), "IV")

    def test_nueve(self):
        self.assertEqual(decimal_to_roman(9), "IX")

    def test_treinta(self):
        self.assertEqual(decimal_to_roman(30), "XXX")

    def test_cuarentaycuatro(self):
        self.assertEqual(decimal_to_roman(44), "XLIV")

    def test_setentaysiete(self):
        self.assertEqual(decimal_to_roman(77), "LXXVII")

    def test_noventaynueve(self):
        self.assertEqual(decimal_to_roman(99), "XCIX")

    def test_cien(self):
        self.assertEqual(decimal_to_roman(100), "C")

    def test_199(self):
        self.assertEqual(decimal_to_roman(199), "CXCIX")

    def test_555(self):
        self.assertEqual(decimal_to_roman(555), "DLV")

    def test_999(self):
        self.assertEqual(decimal_to_roman(999), "CMXCIX")

    def test_5555(self):
        self.assertEqual(decimal_to_roman(5555), "V*DLV")

    def test_9999(self):
        self.assertEqual(decimal_to_roman(9999), "IX*CMXCIX")

    def test_I(self):
        self.assertEqual(roman_to_decimal("I"), 1)

    def test_IV(self):
        self.assertEqual(roman_to_decimal("IV"), 4)

    def test_VII(self):
        self.assertEqual(roman_to_decimal("VII"), 7)

    def test_IX(self):
        self.assertEqual(roman_to_decimal("IX"), 9)

    def test_X(self):
        self.assertEqual(roman_to_decimal("X"), 10)

    def test_XVII(self):
        self.assertEqual(roman_to_decimal("XVII"), 17)

    def test_XXII(self):
        self.assertEqual(roman_to_decimal("XXII"), 22)

    def test_XLIV(self):
        self.assertEqual(roman_to_decimal("XLIV"), 44)

    def test_LV(self):
        self.assertEqual(roman_to_decimal("LV"), 55)

    def test_LXX(self):
        self.assertEqual(roman_to_decimal("LXXVII"), 77)

    def test_CXI(self):
        self.assertEqual(roman_to_decimal("CXI"), 111)

    def test_CCXXII(self):
        self.assertEqual(roman_to_decimal("CCXXII"), 222)

    def test_CCCXXXIII(self):
        self.assertEqual(roman_to_decimal("CCCXXXIII"), 333)

    def test_CDXLIV(self):
        self.assertEqual(roman_to_decimal("CDXLIV"), 444)

    def test_DLV(self):
        self.assertEqual(roman_to_decimal("DLV"), 555)

    def test_DCLXVI(self):
        self.assertEqual(roman_to_decimal("DCLXVI"), 666)

    def test_CMXCIX(self):
        self.assertEqual(roman_to_decimal("CMXCIX"), 999)


if __name__ == "__main__":
    unittest.main()
