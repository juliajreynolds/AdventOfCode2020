import unittest
import day6

class Day6TestCase(unittest.TestCase):
    def test_day6(self):
        self.assertEqual(day6.findTotalUnanimousYes("test_input.txt"), 11)

if __name__ == '__main__':
    unittest.main()
