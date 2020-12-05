import unittest
import day4

class Day4TestCase(unittest.TestCase):
    def test_day4(self):
        self.assertEqual(day4.countValidPassports("test_input.txt"), 2)

if __name__ == '__main__':
    unittest.main()
