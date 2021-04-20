import unittest
from days_of_week import weekDay

class MyTestCase(unittest.TestCase):
    def test_getMonday(self):
        expected = 'Monday'
        actual  =weekDay(1)
        self.assertEqual(expected, actual)

    def test_getError(self):                
        with self.assertRaises(Exception) as err:
            actual  =weekDay(12)
