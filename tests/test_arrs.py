import unittest
import calc
from utils.arrs import get, my_slice


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([0, 1, 2], 0, "test"), 0)
        self.assertEqual(get([], 0, "test"), [])
        self.assertEqual(get([1, 2, 3], -1, "test"), "test")



    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], 2), [3, 4, 5])


if __name__ == '__main__':
    unittest.main()