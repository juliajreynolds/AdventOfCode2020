import unittest
import day1

class Day1TestCase(unittest.TestCase):
    def test_day1(self):
        self.assertEqual(day1.find2020Product("test_input.txt"),514579)


if __name__ == '__main__':
    unittest.main()
