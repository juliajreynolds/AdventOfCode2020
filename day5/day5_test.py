import unittest
import day5

class Day5TestCase(unittest.TestCase):
    def test_day5(self):
        self.assertEqual(day5.findMaxSeatID("test_input.txt"), 820)

if __name__ == '__main__':
    unittest.main()
