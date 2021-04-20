import unittest
from calculate_area import area


class MyTestClass(unittest.TestCase):
    def test_areaforRectangle(self):
        self.assertEqual(area(12, 12), 144)


    def test_areaWithNegative(self):
        with self.assertRaises(ValueError): 
            self.assertEqual(area(12, -12), 144)

if __name__ == '__main__':
    unittest.main()