import unittest
import day3

class Day3TestCase(unittest.TestCase):
    def test_day3(self):
        self.assertEqual(day3.countTrees("test_input.txt"), 7)

if __name__ == '__main__':
    unittest.main()
