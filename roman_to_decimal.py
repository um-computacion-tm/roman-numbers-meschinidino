import unittest

def main():
    return True

def roman_to_decimal(romano):


class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, 1)
    def test_IV(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado, 4)
    def test_VII(self):
        resultado = roman_to_decimal("VII")
        self.assertEqual((resultado, 7))
    def test_IX(self):
        resultado = roman_to_decimal("IX")
        self.assertEqual(resultado, 9)
    def test_X(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado, 10)


if __name__ == '__main__':
    unittest.main()