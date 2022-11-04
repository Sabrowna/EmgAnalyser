import unittest
import TestThis


class TestMethods(unittest.TestCase):

    def test_multiply(self):
        result = TestThis.multiply(1, 2)
        self.assertEqual(result, 2)

    def test_multiply2(self):
        result = TestThis.multiply(-99999999999999999999999, 0)
        self.assertEqual(result, 0)

    def test_multiply3(self):
        result = TestThis.multiply(-999999999999999, 1)
        self.assertEqual(result, -999999999999999)

    def test_multiply4(self):
        result = TestThis.multiply(-1, -1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
