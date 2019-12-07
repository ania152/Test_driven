import unittest
import program2
class TestTDD1(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(program2.upper("ania"), "ANIA")
    def test_lower(self):
        self.assertEqual(program2.lower("KOT"), "kot")
    def test_replace(self):
        self.assertEqual(program2.replace("E", "S", "EGGS"), "SGGS")
    def test_join(self):
        self.assertEqual(program2.join("EGG", "S"), "EGGS")
    def test_len(self):
        self.assertEqual(program2.len("EGGS"), 4)


if __name__ == '__main__':
    unittest.main()
