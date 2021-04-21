import unittest
import area as t


class AreaTestCase(unittest.TestCase):
    
    def test_area_of_rectangle(self):
        self.assertEqual(t.calculate_area(2, 3), 6)
        
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            t.calculate_area(-2, 3)
    
    def test_negative_width(self):
        with self.assertRaises(ValueError):
            t.calculate_area(2, -3)

    # def test_negative(self):
    #     with self.assertRaises(ValueError):
    #         t.calculate_area(-2, -3)        

    def test_length_string(self):
        with self.assertRaises(ValueError):
            t.calculate_area('s', 3)
    def test_width_string(self):
        with self.assertRaises(ValueError):
            t.calculate_area(3, 's')

if __name__ == '__main__':
    unittest.main()