import unittest
import day4

class Day4TestCase(unittest.TestCase):
    def test_day4(self):
        self.assertEqual(day3.countTrees("test_input.txt"), 7)

if __name__ == '__main__':
    unittest.main()
