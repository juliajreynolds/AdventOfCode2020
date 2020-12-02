import unittest
import day2

class Day2TestCase(unittest.TestCase):
    def test_day2(self):
        self.assertEqual(day2.countValidPasswords("test_input.txt"), 1)


if __name__ == '__main__':
    unittest.main()
