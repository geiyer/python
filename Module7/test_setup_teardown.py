import unittest


class TestListElements(unittest.TestCase):
    def setUp(self):
        self.initial_list = [1, 3, 5]
        self.expected_list = [1, 3, 5]

    def tearDown(self):
        self.initial_list = []
        self.expected_list = []

    def test_count_eq(self):        
        self.assertCountEqual(self.initial_list, self.expected_list)

    def test_list_eq(self):        
        self.assertListEqual(self.initial_list, self.expected_list)


if __name__ == '__main__':
    unittest.main()