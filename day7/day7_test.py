import unittest
import day7

class Day7TestCase(unittest.TestCase):
    def test_day7(self):
        self.assertEqual(day7.findTotalUnanimousYes("test_input.txt"), 11)

if __name__ == '__main__':
    unittest.main()
