import unittest
from calculate_taxes import calculate_tax, calculate_taxes
class MyTestCase(unittest.TestCase):
    def test_calculate_tax_22Percent(self):
        # Arrange
        expected = 17160
        # Act
        actual = calculate_tax('single', 78000)
        # Assert
        self.assertEqual(expected, actual)
    def test_calculate_tax_10Percent(self):
        # Arrange
        expected = 980
        # Act
        actual = calculate_tax('single', 9800)
        # Assert
        self.assertEqual(expected, actual)    

    def test_calculate_multiple_taxes(self):
        # Arrange
        income = [9800, 15000, 80000]
        expected = {9800: 980, 15000: 1800, 80000: 17600} 
        # Act        
        actual = calculate_taxes('single', income)
        # Assert
        #self.assertDictEqual(expected, actual) 
        self.assertAlmostEqual(expected, actual)    