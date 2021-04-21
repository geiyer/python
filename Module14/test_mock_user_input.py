import unittest
import unittest.mock as mock
import mock_user_input as t

class MyTestCase(unittest.TestCase):

    def test_quit(self):

        with mock.patch('builtins.input', return_value="yes"):
            assert t.yes_or_no() == "Sorry to see you go!"

        with mock.patch('builtins.input', return_value="no"):
            assert t.yes_or_no() == "Awesome!"

    def test_yah(self):
        with mock.patch('builtins.input', return_value="yah"):
            assert t.yes_or_no() == "BANG!"        

if __name__ == '__main__':
    unittest.main()