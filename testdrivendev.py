import unittest
import mojprogram
class TestTDD1(unittest.TestCase):
    def test_zwroc_100(self):
      wynik = mojprogram.zwroc_100()#tu 0
      self.assertEqual(wynik, 100)

    def test_zwroc_parametr(self):
        self.assertEqual(mojprogram.zwroc_parametr(124), 124)

    def test_zwroc_parametr(self):
        wynik = mojprogram.zwroc_parametr(0)
        self.assertEqual(wynik, 124)

    def test_helloworld(self):
        self.assertEqual(mojprogram.helloworld("hello world"), "hello world")

    def test_dodaj_2_2(self):
        self.assertEqual(mojprogram.dodaj(2,2), 4)

    def test_odejmij(self):
        self.assertEqual(mojprogram.odejmij(4,2), 3)

    def test_pomnoz(self):
        self.assertEqual(mojprogram.pomnoz(4,2), 8)

if __name__ == '__main__':
    unittest.main()
